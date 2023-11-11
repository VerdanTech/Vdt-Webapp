import pytest
from pytest_mock import MockerFixture
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.user.controllers.write import UserWriteOpsController
from src.ops.user.schemas.write import UserCreateInput
from src.utils.sanitizers.object import ObjectSanitizer

pytestmark = [pytest.mark.unit]


class TestUserWriteOperations:
    pass
