# Standard Library
from typing import AsyncGenerator, Generator

# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from testcontainers.postgres import PostgresContainer

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository

from .sqlalchemy import function_scoped_sql_transaction


@pytest.fixture
def postgres() -> Generator[PostgresContainer, None, None]:
    """
    Creates a new postgres container for
    every test.
    """
    with PostgresContainer() as postgres:
        postgres.driver = "asyncpg"
        yield postgres


@pytest.fixture
async def alchemy_transaction(postgres: PostgresContainer) -> AsyncGenerator[AsyncSession, None]:
    """
    Creates a new SqlAlchemy transaction for every test.
    Runs independently from the application transactions.
    """
    async with function_scoped_sql_transaction(
        alchemy_uri=postgres.get_connection_url()
    ) as transaction:
        yield transaction


@pytest.fixture
def user_repo(alchemy_transaction: AsyncSession) -> AbstractUserRepository:
    """
    Creates a new UserRepo for every test.
    """
    user_repo = UserAlchemyRepository(transaction=alchemy_transaction)
    return user_repo
