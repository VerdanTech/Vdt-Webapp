# External Libraries
import pytest

# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository
from src.ops.user.controllers.write import UserWriteOpsController


@pytest.fixture
def user_write_ops_controller() -> UserWriteOpsController:
    return UserWriteOpsController(user_repo=MockUserRepository())
