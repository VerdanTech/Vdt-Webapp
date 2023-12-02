import pytest
from backend.mocks.infra.persistence.generic.repository.user.repository import MockUserRepository
from src.ops.user.controllers.verification import UserVerificationOpsController
from src.ops.user.controllers.write import UserWriteOpsController


@pytest.fixture
def user_write_operations(mock_user_repo: MockUserRepository) -> UserWriteOpsController:
    return UserWriteOpsController(user_repo=mock_user_repo)


@pytest.fixture
def user_verification_operations(
    mock_user_repo: MockUserRepository,
) -> UserVerificationOpsController:
    return UserVerificationOpsController(user_repo=mock_user_repo)
