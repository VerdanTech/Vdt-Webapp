import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.persistence.repository.alchemy.user import (
    provide_user_alchemy_repository_sync,
)
from src.interfaces.persistence.user.repository import AbstractUserRepository
from tests.unit.domain.user.conftest import UserMake, user


@pytest.fixture(params=[(provide_user_alchemy_repository_sync, "alchemy_db_session")])
def user_repo(request, alchemy_db_session: AsyncSession) -> AbstractUserRepository:
    provider, session_name = request.param
    if session_name == "alchemy_db_session":
        return provider(db_session=alchemy_db_session)
