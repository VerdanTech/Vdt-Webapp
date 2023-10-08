from __future__ import annotations

from dataclasses import field, replace
from datetime import datetime, timedelta
from typing import Optional

from ..common.values import Ref, Value
from .exceptions import EmailAlreadyVerifiedError, EmailConfirmationExpired


class UserRef(Ref):
    """User ID value object"""

    pass


class Email(Value):
    """Email value object"""

    address: str
    verified: bool = False
    primary: bool = False
    confirmation: Optional["EmailConfirmation"] = None
    verified_at: Optional[datetime] = None

    def new_confirmation(self, key: str) -> Email:
        """Create a new email confirmation and return
            new email

        Args:
            key (str): the verification key to set

        Raises:
            EmailAlreadyVerifiedException: raised when email
                is already verified

        Returns:
            Email: resultant mutated email
        """
        if self.verified:
            raise EmailAlreadyVerifiedError(
                "Email confirmation attempt on already verified email"
            )

        confirmation = EmailConfirmation(key=key)
        return replace(self, confirmation=confirmation)

    def verify(self) -> Email:
        """Set the verification flag to true

        Returns:
            Email: resultant mutated email
        """
        if self.verified:
            raise EmailAlreadyVerifiedError(
                "Email verification attempt on already verified email"
            )
        return replace(
            self, verified=True, confirmation=None, verified_at=datetime.now()
        )

    def make_primary(self) -> Email:
        """Set the primary flag to true

        Returns:
            Email: resultant mutated email
        """
        return replace(self, primary=True)

    def make_unprimary(self) -> Email:
        """Set the primary flag to false

        Returns:
            Email: resultant mutated email
        """
        return replace(self, primary=False)

    def check_confirmation_expired(self) -> None:
        if self.confirmation is None:
            return
        if not self.confirmation.is_valid():
            raise EmailConfirmationExpired("The email confirmation key is expired")


class BaseConfirmation(Value):
    """Base value object for verification through email"""

    key: str
    created_at: datetime = field(default_factory=datetime.now)

    def is_valid(self, expiry_time_hours: int) -> bool:
        """Computes whether the confirmation has expired

        Args:
            expiry_time_hours (int): application setting

        Returns:
            bool: false if not expired
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
