# Standard Library
from typing import AsyncGenerator

# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from testcontainers.postgres import PostgresContainer

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository

from .sqlalchemy import function_scoped_sql_transaction


@pytest.fixture
def postgres():
    with PostgresContainer() as postgres:
        postgres.driver = "asyncpg"
        connection_details = postgres.get_connection_url()
        print(connection_details)
        yield postgres


@pytest.fixture
async def alchemy_transaction(postgres) -> AsyncGenerator[AsyncSession, None]:
    async with function_scoped_sql_transaction(
        alchemy_uri=postgres.get_connection_url()
    ) as transaction:
        yield transaction


@pytest.fixture
def user_repo(alchemy_transaction: AsyncSession) -> AbstractUserRepository:
    user_repo = UserAlchemyRepository(transaction=alchemy_transaction)
    return user_repo
