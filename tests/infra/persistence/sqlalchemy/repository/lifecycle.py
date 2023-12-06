# Standard Library
import subprocess
from typing import AsyncGenerator

# External Libraries
import pytest
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# VerdanTech Source
from src import settings
from src.infra.persistence.sqlalchemy.repository import AlchemyClient

# ======================================
# SQLALCHEMY
# ======================================


@pytest.fixture
def alchemy_db_client() -> AlchemyClient:
    engine = create_async_engine(settings.ALCHEMY_URI, echo=True)
    sessionmaker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return AlchemyClient(engine=engine, sessionmaker=sessionmaker)


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
