# Standard Library
from typing import AsyncGenerator, Callable

# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

# VerdanTech Source
from src.user.adapters.sqlalchemy import UserAlchemyRepository
from src.user.interfaces import AbstractUserRepository
from tests.common.adapters.persistence.sqlalchemy import (
    function_scoped_sql_transaction,
    session_scoped_sql_connection,
)
from tests.mocks.persistence.user_mock import MockUserRepository
from tests.user.domain.conftest import user  # noqa: F401 - pytest fixture


def provide_user_alchemy_repository(
    sqlalchemy_session: AsyncSession,
) -> UserAlchemyRepository:
    return UserAlchemyRepository(session=sqlalchemy_session)


def provide_user_mock_repository() -> MockUserRepository:
    return MockUserRepository()


@pytest.fixture(
    params=[
        (provide_user_mock_repository, "mock"),
        (provide_user_alchemy_repository, "sqlalchemy"),
    ]
)
async def user_repo(request, sql_connection: AsyncConnection) -> AbstractUserRepository:
    provider: Callable[..., AbstractUserRepository]
    provider_type: str
    provider, provider_type = request.param

    match provider_type:
        case "mock":
            return provider()
        case "sqlalchemy":
            async with function_scoped_sql_transaction(
                connection=sql_connection
            ) as session:
                return provider(session)

    raise ValueError(f"Unknown provider type for repository tests: {provider_type}")


@pytest.fixture(scope="session")
async def sql_connection() -> AsyncGenerator[AsyncConnection, None]:
    async with session_scoped_sql_connection() as connection:
        yield connection


@pytest.fixture(scope="function")
async def sqlalchemy_session(
    sql_connection: AsyncConnection,
) -> AsyncGenerator[AsyncSession, None]:
    async with function_scoped_sql_transaction(
        connection=sql_connection
    ) as transaction:
        yield transaction
