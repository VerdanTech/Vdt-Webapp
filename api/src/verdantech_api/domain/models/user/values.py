from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from litestar.contrib.repository.abc import AbstractAsyncRepository
from src.verdantech_api import settings

from ..common.values import Ref, Value
from .exceptions import EmailAlreadyVerifiedException


class UserRef(Ref):
    """User ID value object"""

    pass


class Email(Value):
    """Email value object"""

    address: str
    verified: bool = False
    primary: bool = False
    confirmation: "EmailConfirmation" | None

    def new_confirmation(self, key: str) -> None:
        """Create a new email confirmation

        Args:
            key (str): the verification key to set

        Raises:
            EmailAlreadyVerifiedException: raised when email
                is already verified
        """
        if self.verified:
            raise EmailAlreadyVerifiedException(
                "Email confirmation attempt on already verified email"
            )

        confirmation = EmailConfirmation(key=key)
        self.confirmation = confirmation


class BaseConfirmation(Value):
    """Base value object for verification through email"""

    key: str
    created_at: datetime = field(default_factory=datetime.now)


class EmailConfirmation(BaseConfirmation):
    """Email confirmation value object"""

    pass


class PasswordResetConfirmation(BaseConfirmation):
    """Password reset confirmation value object"""

    hashed_password: str
