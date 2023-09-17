import pytest
from src.verdantech_api.domain.models.user.services.verification import (
    VerificationService,
)
from src.verdantech_api.infrastructure.persistence.repository.mock.user.repository import (
    MockUserRepository,
)


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()


@pytest.fixture
def verification_service():
    return VerificationService()
