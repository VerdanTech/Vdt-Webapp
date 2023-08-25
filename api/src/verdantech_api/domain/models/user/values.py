from __future__ import annotations

from dataclasses import field, replace
from datetime import datetime

from ..common.values import Ref, Value
from .exceptions import EmailAlreadyVerifiedError


class UserRef(Ref):
    """User ID value object"""

    pass


class Email(Value):
    """Email value object"""

    address: str
    verified: bool = False
    primary: bool = False
    confirmation: "EmailConfirmation" | None = None

    def new_confirmation(self, key: str) -> Email:
        """Create a new email confirmation and return
            new email

        Args:
            key (str): the verification key to set

        Raises:
            EmailAlreadyVerifiedException: raised when email
                is already verified

        Returns:
            Email: A new email object with confirmation replaced
        """
        if self.verified:
            raise EmailAlreadyVerifiedError(
                "Email confirmation attempt on already verified email"
            )

        confirmation = EmailConfirmation(key=key)
        return replace(self, confirmation=confirmation)


class BaseConfirmation(Value):
    """Base value object for verification through email"""

    key: str
    created_at: datetime = field(default_factory=datetime.now)


class EmailConfirmation(BaseConfirmation):
    """Email confirmation value object"""

    pass


class PasswordResetConfirmation(BaseConfirmation):
    """Password reset confirmation value object"""

    password_hash: str
