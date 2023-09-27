import pytest
from src.verdantech_api.application.user.operations.verification import (
    UserVerificationOperations,
)
from src.verdantech_api.application.user.operations.write import UserWriteOperations
from src.verdantech_api.infrastructure.persistence.repository.mock.user.repository import (
    MockUserRepository,
)


@pytest.fixture
def user_write_operations(mock_user_repo: MockUserRepository) -> UserWriteOperations:
    return UserWriteOperations(user_repo=mock_user_repo)


@pytest.fixture
def user_verification_operations(
    mock_user_repo: MockUserRepository,
) -> UserVerificationOperations:
    return UserVerificationOperations(user_repo=mock_user_repo)
