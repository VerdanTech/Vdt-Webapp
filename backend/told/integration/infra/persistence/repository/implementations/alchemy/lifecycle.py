import subprocess
from typing import AsyncGenerator

import pytest
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src import settings
from src.infra.persistence.repository.alchemy import AlchemyClient

# ======================================
# SQLALCHEMY
# ======================================


@pytest.fixture
async def alchemy_db_session(
    alchemy_db_client: AlchemyClient,
) -> AsyncGenerator[AsyncSession, None]:
    """Yield a session with a savepoint, that
    rolls back after every test case

    https://www.core27.co/post/transactional-unit-tests-with-pytest-and-async-sqlalchemy
    """
    connection = await alchemy_db_client.engine.connect()
    db_transaction = await connection.begin()
    session = alchemy_db_client.sessionmaker(bind=connection)
    nested = await connection.begin_nested()

    @event.listens_for(session.sync_session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.sync_connection.begin_nested()

    yield session

    await db_transaction.rollback()
    await session.close()
    await connection.close()


@pytest.fixture
def alchemy_db_client() -> AlchemyClient:
    engine = create_async_engine(settings.ALCHEMY_URI, echo=True)
    sessionmaker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return AlchemyClient(engine=engine, sessionmaker=sessionmaker)


# ======================================
# POSTGRES
# ======================================


def check_postgres_running():
    try:
        existing_services = subprocess.run(
            ["pgrep", "postgres"], stdout=subprocess.PIPE, check=True
        )
        pids = existing_services.stdout.decode().strip().split("\n")
        print(f"PostgreSQL is running with PIDs: {', '.join(pids)}")
        return True
    except subprocess.CalledProcessError as e:
        print("PostgreSQL is not running")
        return False


def start_postgres():
    try:
        subprocess.run(["sudo", "service", "postgresql", "start"], check=True)
        print("Successfully started PostgreSQL")
    except subprocess.CalledProcessError as error:
        print(f"Failed to start PostgreSQL: {error}")


@pytest.fixture(scope="session", autouse=True)
def postgres_setup(request) -> None:
    marker = request.node.get_closest_marker("databases")
    if marker:
        if not check_postgres_running():
            start_postgres()
