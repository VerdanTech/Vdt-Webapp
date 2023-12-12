# External Libraries
import pytest
from svcs import Container

# VerdanTech Source
from src.ops.user.controllers.write import UserWriteOpsController


@pytest.fixture
async def user_write_ops_controller(svcs_container: Container) -> UserWriteOpsController:
    controller = await svcs_container.aget(UserWriteOpsController)
    return controller
