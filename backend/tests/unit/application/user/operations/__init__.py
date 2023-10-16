import pytest
from src.application.user.operations.write import UserWriteOperations


@pytest.fixture
def user_write_operations(mock_user_repo):
    return UserWriteOperations(user_repo=mock_user_repo)
