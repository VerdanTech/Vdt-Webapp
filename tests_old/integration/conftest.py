# Standard Library
from typing import AsyncGenerator, Generator

# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src import settings
from src.adapters.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.interfaces.persistence.user.user import AbstractUserRepository

from .sqlalchemy import function_scoped_sql_transaction


@pytest.fixture
async def alchemy_transaction() -> AsyncGenerator[AsyncSession, None]:
    """
    Creates a new SqlAlchemy transaction for every test.
    Runs independently from the application transactions.
    """
    async with function_scoped_sql_transaction(
        alchemy_uri=settings.ALCHEMY_URI
    ) as transaction:
        yield transaction


@pytest.fixture
def user_repo(alchemy_transaction: AsyncSession) -> AbstractUserRepository:
    """
    Creates a new UserRepo for every test.
    """
    user_repo = UserAlchemyRepository(transaction=alchemy_transaction)
    return user_repo
