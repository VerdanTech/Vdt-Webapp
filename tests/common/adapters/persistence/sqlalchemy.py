# Standard Library
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from sqlalchemy import event
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# VerdanTech Source
from src import settings
from src.common.adapters.persistence.sqlalchemy import AlchemyClient

# ======================================
# SQLALCHEMY
# ======================================

engine = create_async_engine(settings.ALCHEMY_URI, echo=True)

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
    autoflush=True,
)

alchemy_client = AlchemyClient(engine=engine)


@asynccontextmanager
async def function_scoped_sql_transaction(
    connection: AsyncConnection, close_transaction: bool = True
) -> AsyncGenerator[AsyncSession, None]:
    """Yield a session with a savepoint, that
    rolls back after every test case

    https://www.core27.co/post/transactional-unit-tests-with-pytest-and-async-sqlalchemy

    https://github.com/sqlalchemy/sqlalchemy/issues/5811
    """
    transaction = sessionmaker(bind=connection)
    nested = await connection.begin_nested()

    @event.listens_for(transaction.sync_session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.sync_connection.begin_nested()

    try:
        yield transaction
    finally:
        if close_transaction:
            await transaction.close()


@asynccontextmanager
async def session_scoped_sql_connection(
    client: AlchemyClient = alchemy_client,
) -> AsyncGenerator[AsyncConnection, None]:
    await client.init()
    connection = await client.engine.connect()
    connection_transaction = await connection.begin()
    try:
        yield connection

    finally:
        await connection_transaction.rollback()
        await connection.close()
