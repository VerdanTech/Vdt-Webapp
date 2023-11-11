import pytest
from src.ops.user.controllers.write import UserWriteOpsController


@pytest.fixture
def user_write_operations(mock_user_repo):
    return UserWriteOpsController(user_repo=mock_user_repo)
