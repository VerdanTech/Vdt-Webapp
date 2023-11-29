from typing import ContextManager

import pytest
from pytest_mock import MockerFixture
from src.domain.user.entities import User
from src.domain.user.exceptions import (
    EmailConfirmationKeyNotFound,
    PasswordResetConfirmationNotFound,
    UserNotFound,
)
from src.domain.user.values import Email, EmailConfirmation, PasswordResetConfirmation
from src.ops.user.controllers.verification import UserVerificationOpsController
from src.ops.user.schemas import verification as schemas
from src.utils.sanitizers.object import ObjectSanitizer

pytestmark = [pytest.mark.unit]


class TestUserVerificationOpsController:
    pass
