import pytest
from functools import partial

from litestar.contrib.repository.testing.generic_mock_repository import (
    GenericAsyncMockRepository,
)

from src.verdantech_api.domain.utils.key_generator import key_generator
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services.verification import VerificationService



class MockUserRepository(GenericAsyncMockRepository[User]):
    model_type = User


@pytest.fixture
def mock_user_repo():
    return MockUserRepository(id_factory=partial(key_generator, length=8))

@pytest.fixture
def verification_service():
    return VerificationService()