# Standard Library
from typing import AsyncGenerator
from contextlib import asynccontextmanager

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

engine = create_async_engine(settings.ALCHEMY_URI, echo=True)

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

alchemy_client = AlchemyClient(engine=engine)

@pytest.fixture
async def sql_transaction() -> AsyncGenerator[AsyncSession, None]:
    """Yield a session with a savepoint, that
    rolls back after every test case

    https://www.core27.co/post/transactional-unit-tests-with-pytest-and-async-sqlalchemy
    <https://github.com/sqlalchemy/sqlalchemy/issues/5811>
    """
    connection = await alchemy_client.engine.connect()
    db_transaction = await connection.begin()
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
        await db_transaction.rollback()
        await transaction.close()
        await connection.close()