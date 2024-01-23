from __future__ import annotations

# Standard Library
from dataclasses import field, replace
from datetime import datetime, timedelta
from typing import Optional

# VerdanTech Source
from src.exceptions import ExceptionResponseEnum

from ..common import Ref, Value, value_dataclass
from .exceptions import EmailAlreadyVerifiedError, EmailConfirmationExpired


@value_dataclass
class Email(Value):
    """Email value object"""

    address: str
    verified: bool = False
    primary: bool = False
    confirmation: Optional["EmailConfirmation"] = None
    verified_at: Optional[datetime] = None

    def new_confirmation(self, key: str) -> Email:
        """
        Create a new email confirmation on email.

        Args:
            key (str): the verification key to set.

        Raises:
            EmailAlreadyVerifiedException: raised when email
                is already verified.

        Returns:
            Email: resultant email with new confirmation.
        """
        if self.verified:
            raise EmailAlreadyVerifiedError(
                "Email confirmation attempt on already verified email"
            )

        confirmation = EmailConfirmation(key=key)
        return replace(self, confirmation=confirmation)

    def verify(self) -> Email:
        """
        Set the verification flag to True.

        Returns:
            Email: resultant email
        """
        if self.verified:
            raise EmailAlreadyVerifiedError(
                "Email verification attempt on already verified email",
                response=ExceptionResponseEnum.CLIENT_ERROR,
            )
        return replace(
            self, verified=True, confirmation=None, verified_at=datetime.now()
        )

    def make_primary(self) -> Email:
        """
        Set the primary flag to True.

        Returns:
            Email: resultant email.
        """
        return replace(self, primary=True)

    def make_unprimary(self) -> Email:
        """
        Set the primary flag to False.

        Returns:
            Email: resultant email.
        """
        return replace(self, primary=False)

    def check_confirmation_expired(self, expiry_time_hours: int) -> None:
        """
        Raise an exception if the email's confirmation is expired.

        Args:
            expiry_time_hours (int): the amount of hours an EmailConfirmation
                can exist before it expires. Application setting.

        Raises:
            EmailConfirmationExpired: raised if the confirmation is exprired.
        """
        if self.confirmation is None:
            return
        if not self.confirmation.is_valid(expiry_time_hours=expiry_time_hours):
            raise EmailConfirmationExpired(
                "The email confirmation key is expired",
                response=ExceptionResponseEnum.CLIENT_ERROR,
            )


@value_dataclass
class BaseConfirmation(Value):
    """Base value object for verification through email"""

    key: str
    created_at: datetime = field(default_factory=datetime.now)

    def is_valid(self, expiry_time_hours: int) -> bool:
        """
        Computes whether the confirmation has expired.

        Args:
            expiry_time_hours (int): amount of hours before an email
                confirmation should expire, application setting.

        Returns:
            bool: false if not expired.
        """
        return not (datetime.now() - self.created_at) > timedelta(
            hours=expiry_time_hours
        )


class EmailConfirmation(BaseConfirmation):
    """Email confirmation value object"""

    pass


class PasswordResetConfirmation(BaseConfirmation):
    """Password reset confirmation value object"""

    pass
