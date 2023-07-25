from dataclasses import field
from datetime import datetime
from typing import Callable, List

from src.verdantech_api.infrastructure.security.interfaces import AbstractPasswordCrypt
from src.verdantech_api.infrastructure.validators2.interfaces import (
    AbstractObjectValidator,
)

from ..common.entities import RootEntity
from ..garden.values import GardenMembershipRef
from .exceptions import PasswordAlreadySetException
from .values import Email, PasswordResetConfirmation


class User(RootEntity):
    """User entity model"""

    username: str = field(metadata={"validators": ["MinLength"]})
    username_norm: str
    _password_hash: str | None = None
    emails: set[Email] = {}
    memberships: set[GardenMembershipRef] = {}
    is_active: bool = True
    is_superuser: bool = False
    password_reset_confirmation: PasswordResetConfirmation | None = None
    created_at: datetime = field(default_factory=datetime.now)

    def add_email(self, address: str, primary: bool, key: str) -> None:
        """Default new email. Verified is false and new confirmation is
            created

        Args:
            address (str): address of email
            primary (bool): whether email is the user's primary. Should
                be true for user creation and false elsewhere
            key (str): verification key to assign to email confirmation
        """
        email = Email(address=address, primary=primary, verified=False)
        email.new_confirmation(key=key)
        self.emails.add(email)

    def add_verified_email(self, address: str, primary: bool) -> None:
        """Bypass verification new email. Verified is true

        Args:
            address (str): address of email
            primary (bool): whether email is the user's primary. Should
                be true for user creation and false elsewhere
        """
        email = Email(address=address, primary=primary, verified=True)
        self.emails.add(email)

    async def set_password(
        self,
        password: str,
        password_crypt: AbstractPasswordCrypt,
        overwrite: bool = False,
    ) -> None:
        """Generate and set hashed password given plaintext password

        Args:
            password (str): plaintext password to hash and set
            password_crypt (AbstractPasswordCrypt): encryption class
            overwrite (bool): whether to allow overwriting existing password

        Raises:
            PasswordAlreadySetException: is password is already set,
                but the function was called with overwrite=False
        """
        if not self._password_hash and not overwrite:
            raise PasswordAlreadySetException(
                """Password set attempt failed: 
                called with overwrite=False 
                but password already set
                """
            )
        password_hash = await password_crypt.get_password_hash(password)
        self.password_hash = password_hash

    async def verify_password(
        self, password: str, password_crypt: AbstractPasswordCrypt
    ) -> bool:
        """Check input password against user's password

        Args:
            password (str): the password to check
            password_crypt (AbstractPasswordCrypt): encryption class

        Returns:
            bool: the result of the password match
        """
        return await password_crypt.verify_password(
            plain_password=password, hashed_password=self._password_hash
        )
