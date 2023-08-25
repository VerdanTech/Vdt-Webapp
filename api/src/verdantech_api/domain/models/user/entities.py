from dataclasses import field
from datetime import datetime
from typing import List

from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt

from ..common.entities import RootEntity
from ..garden.values import GardenMembershipRef
from .exceptions import PasswordAlreadySetError
from .values import Email, PasswordResetConfirmation


class User(RootEntity):
    """User entity model"""

    username: str
    username_norm: str = None
    _password_hash: str | None = None
    emails: List[Email] = None
    memberships: List[GardenMembershipRef] = None
    is_active: bool = True
    is_superuser: bool = False
    password_reset_confirmation: PasswordResetConfirmation | None = None
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        self.set_username(username=self.username)
        self.emails = []
        self.memberships = []

    def set_username(self, username: str) -> None:
        """Manage normalized username setting

        Args:
            username (str): case sensitive username
        """
        self.username = username
        self.username_norm = username.lower()

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
        email = email.new_confirmation(key=key)
        self.emails.append(email)

    def add_verified_email(self, address: str, primary: bool) -> None:
        """Bypass verification new email. Verified is true

        Args:
            address (str): address of email
            primary (bool): whether email is the user's primary. Should
                be true for user creation and false elsewhere
        """
        email = Email(address=address, primary=primary, verified=True)
        self.emails.append(email)

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
        if self._password_hash is not None and not overwrite:
            raise PasswordAlreadySetError(
                """Password set attempt failed: 
                called with overwrite=False 
                but password already set
                """
            )
        self._password_hash = await password_crypt.get_password_hash(
            plain_password=password
        )

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
