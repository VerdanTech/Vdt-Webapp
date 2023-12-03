import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository
from tests.domain.user.conftest import user
from tests.infra.persistence.sqlalchemy.repository.lifecycle import (
    alchemy_db_client,
    alchemy_db_session,
)


def provide_user_alchemy_repository(db_session: AsyncSession) -> AbstractUserRepository:
    return UserAlchemyRepository(session=db_session)


@pytest.fixture(params=[(provide_user_alchemy_repository, "alchemy_db_session")])
def user_repo(request, alchemy_db_session: AsyncSession) -> AbstractUserRepository:
    provider, session_name = request.param
    if session_name == "alchemy_db_session":
        return provider(db_session=alchemy_db_session)
