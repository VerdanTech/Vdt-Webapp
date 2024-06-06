# Standard Library
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.sql import text

# VerdanTech Source
from src.infra.persistence.sqlalchemy.mapper.model import Base
from src.infra.persistence.sqlalchemy.repository.client import AlchemyClient

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
)


@asynccontextmanager
async def function_scoped_sql_transaction(
    alchemy_uri: str,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Generates a SqlAlchemy transaction for testing.

    It is assumed that a single engine and transaction is used per test.

    Autocommit is used to avoid having to commit transactions
    during tests.

    Args:
        alchemy_uri (str): uri to connect to.

    Returns:
        AsyncGenerator[AsyncSession, None]: the sqlalchemy transaction.
    """
    engine = create_async_engine(alchemy_uri, echo=True, isolation_level="AUTOCOMMIT")
    client = AlchemyClient(engine=engine)
    await client.init()
    async with sessionmaker(bind=engine) as transaction:
        yield transaction

    async with client.engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)

    await client.close()
