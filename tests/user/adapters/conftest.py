# Standard Library
from typing import AsyncGenerator

# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

# VerdanTech Source
# from src.user.adapters.sqlalchemy import UserAlchemyRepository
from src.user.interfaces import AbstractUserRepository
from tests.mocks.persistence.user_mock import MockUserRepository
from tests.user.domain.conftest import user  # noqa: F401 - pytest fixture

# from tests_old.infra.persistence.sqlalchemy.repository.lifespan import (
# function_scoped_sql_transaction,
# session_scoped_sql_connection,
# )


def provide_user_alchemy_repository(
    transaction: AsyncSession,
) -> "UserAlchemyRepository":
    pass
    # return UserAlchemyRepository(transaction=transaction)


def provide_user_mock_repository() -> MockUserRepository:
    return MockUserRepository()


@pytest.fixture(
    params=[
        (provide_user_mock_repository, "mock"),
        (provide_user_mock_repository, "sqlalchemy"),
    ]
)
def user_repo(request) -> AbstractUserRepository:
    provider, provider_type = request.param
    print(provider)
    if provider_type == "mock":
        return provider()
    elif provider_type == "sqlalchemy":
        return provider()


# TODO fix test transactions
"""
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
"""
