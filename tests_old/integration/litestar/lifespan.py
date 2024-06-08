# Standard Library
import pdb
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from litestar import Litestar
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool
from svcs import Container

# VerdanTech Source
from src import settings
from src.adapters.persistence.sqlalchemy.mapper.common import Base
from src.adapters.persistence.sqlalchemy.repository import AlchemyClient

function_scoped_alchemy_transaction_key = "function_scoped_alchemy_transaction"
session_scoped_alchemy_connection_key = "session_scoped_alchemy_connection"

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
    autoflush=False,
)


@asynccontextmanager
async def session_scoped_sql_client() -> AsyncGenerator[AlchemyClient, None]:
    engine = create_async_engine(
        settings.ALCHEMY_URI, echo=True, isolation_level="AUTOCOMMIT"
    )
    client = AlchemyClient(engine=engine)
    await client.init()
    try:
        yield client

    finally:
        # Delete database
        async with client.engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
        await client.close()


@asynccontextmanager
async def function_scoped_sql_transaction(
    client: AlchemyClient,
) -> AsyncGenerator[AsyncSession, None]:
    """one transaction per test function"""
    await client.init()
    async with sessionmaker(bind=client.engine) as session:
        session.begin()
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            # Delete database
            async with client.engine.begin() as connection:
                await connection.run_sync(Base.metadata.drop_all)
            await client.close()


@asynccontextmanager
async def alchemy_isolation(client: AlchemyClient) -> AsyncGenerator[None, None]:
    await client.init()
    yield
    async with client.engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
