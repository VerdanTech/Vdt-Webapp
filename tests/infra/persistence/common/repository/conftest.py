# External Libraries
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository
from tests.domain.user.conftest import user
from tests.infra.persistence.sqlalchemy.repository.lifecycle import sql_transaction


def provide_user_alchemy_repository(transaction: AsyncSession) -> UserAlchemyRepository:
    return UserAlchemyRepository(transaction=transaction)


@pytest.fixture(params=[(provide_user_alchemy_repository, "sql_transaction")])
def user_repo(request, sql_transaction: AsyncSession) -> AbstractUserRepository:
    provider, transaction_name = request.param
    if transaction_name == "sql_transaction":
        return provider(transaction=sql_transaction)
