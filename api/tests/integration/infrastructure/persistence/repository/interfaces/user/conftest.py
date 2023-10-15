from sqlalchemy.ext.asyncio import AsyncSession

import pytest

from src.verdantech_api.domain.interfaces.persistence.user.repository import AbstractUserRepository
from src.verdantech_api.infrastructure.persistence.repository.alchemy.user import (
    provide_user_alchemy_repository,
)
from tests.unit.domain.models.user.conftest import user 

@pytest.fixture(params=[(provide_user_alchemy_repository, "alchemy_db_session")])
def user_repo(request, alchemy_db_session: AsyncSession) -> AbstractUserRepository:
    provider, session_name = request.param
    if session_name == "alchemy_db_session":
        return provider(db_session=alchemy_db_session)
