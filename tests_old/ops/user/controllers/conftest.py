# External Libraries
import pytest
from svcs import Container

# VerdanTech Source
from src.ops.user.controllers.auth import UserAuthOpsController
from src.ops.user.controllers.verification import UserVerificationOpsController
from src.ops.user.controllers.write import UserWriteOpsController


@pytest.fixture
async def user_auth_ops_controller(
    svcs_container: Container,
) -> UserAuthOpsController:
    controller = await svcs_container.aget(UserAuthOpsController)
    return controller


@pytest.fixture
async def user_write_ops_controller(
    svcs_container: Container,
) -> UserWriteOpsController:
    controller = await svcs_container.aget(UserWriteOpsController)
    return controller


@pytest.fixture
async def user_verification_ops_controller(
    svcs_container: Container,
) -> UserVerificationOpsController:
    controller = await svcs_container.aget(UserVerificationOpsController)
    return controller
