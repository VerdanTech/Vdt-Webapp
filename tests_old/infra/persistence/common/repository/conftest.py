# Standard Library
from typing import AsyncGenerator

# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

# VerdanTech Source
from src.user.adapters.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.user.interfaces.persistence.user.user import AbstractUserRepository
from tests.user.unit.conftest import user  # noqa: F401 - pytest fixture
from tests_old.infra.persistence.sqlalchemy.repository.lifespan import (
    function_scoped_sql_transaction,
    session_scoped_sql_connection,
)


def provide_user_alchemy_repository(transaction: AsyncSession) -> UserAlchemyRepository:
    return UserAlchemyRepository(transaction=transaction)


@pytest.fixture(params=[(provide_user_alchemy_repository, "sql_transaction")])
def user_repo(request, sql_transaction: AsyncSession) -> AbstractUserRepository:
    provider, transaction_name = request.param
    if transaction_name == "sql_transaction":
        return provider(transaction=sql_transaction)


@pytest.fixture(scope="session")
async def sql_connection() -> AsyncGenerator[AsyncConnection, None]:
    async with session_scoped_sql_connection() as connection:
        yield connection


@pytest.fixture(scope="function")
async def sql_transaction(
    sql_connection: AsyncConnection,
) -> AsyncGenerator[AsyncSession, None]:
    async with function_scoped_sql_transaction(
        connection=sql_connection
    ) as transaction:
        yield transaction
