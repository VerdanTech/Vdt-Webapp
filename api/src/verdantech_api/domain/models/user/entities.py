from dataclasses import field
from datetime import datetime, timedelta
from typing import List, Optional

from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt

from ..common.entities import RootEntity
from ..garden.values import GardenMembershipRef
from .exceptions import EmailConfirmationKeyNotFound, PasswordAlreadySetError
from .values import Email, PasswordResetConfirmation


class User(RootEntity):
    """User entity model"""

    username: str
    username_norm: Optional[str] = None
    _password_hash: Optional[str] = None
    emails: Optional[List[Email]] = None
    memberships: Optional[List[GardenMembershipRef]] = None
    is_active: bool = True
    is_superuser: bool = False
    password_reset_confirmation: Optional[PasswordResetConfirmation] = None
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if self.username_norm is None:
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

    def new_email_verification(self, address: str, key: str) -> None:
        """Given an email address and confirmation key,
            generate a new confirmation and replace the email

        Args:
            address (str): email address to make confirmation for
            key (str): confirmation key to make confirmation with
        """
        for index, email in enumerate(self.emails):
            if email.address == address:
                email = email.new_confirmation(key=key)
                self.emails[index] = email

    def new_password_reset(self, key: str) -> None:
        """Given a verification key, open a new password reset
            confirmation request on the user object

        Args:
            key (str): the key to set on the reset confirmation
        """
        self.password_reset_confirmation = PasswordResetConfirmation(key=key)

    def verify_email(self, key: str) -> None:
        """Given a verification key, verify the email
            and set it as primary, ensuring the email
            confirmation is not expired

        Args:
            key (str): email confirmation key
        """
        email = self.get_email_by_confirmation_key(key=key)
        email.check_confirmation_expired()
        email = email.verify()
        self.set_primary_email(email)

    async def reset_password(
        self, new_password: str, password_crypt: AbstractPasswordCrypt
    ) -> None:
        """Close a password reset request by setting the new password

        Args:
            new_password (str): the new password to set
            password_crypt (AbstractPasswordCrypt): password crypt interface
        """
        await self.set_password(
            password=new_password, password_crypt=password_crypt, overwrite=True
        )
        self.password_reset_confirmation = None

    def get_email_by_confirmation_key(self, key: str) -> Email:
        """Given an email confirmation key, return the
            email on the user with a matching key,
            or raise an exception if not found

        Args:
            key (str): the key to search for

        Raises:
            EmailConfirmationKeyNotFound: if a matching
                email is not found

        Returns:
            Email: the matching email
        """
        email_with_key = None
        for email in self.emails:
            if email.confirmation is not None and email.confirmation.key == key:
                email_with_key = email
        if email_with_key is None:
            raise EmailConfirmationKeyNotFound(
                "The email verification key does not exist"
            )
        return email_with_key

    def set_primary_email(self, new_primary_email: Email) -> None:
        """Make the given email the only email in the user's
            list of email with primary=True

        Args:
            new_primary_email (Email): the email to make primary
        """
        # Remove primary status on other emails
        emails = [
            email.make_unprimary()
            for email in self.emails
            if email != new_primary_email
        ]

        # Add new primary email to emails
        new_primary_email = new_primary_email.make_primary()
        emails.insert(0, new_primary_email)
        self.emails = emails

    def remove_oldest_emails(self, max_emails: int) -> None:
        """Remove the emails that were verified the longest
            time ago and which put the user over their max emails

        Args:
            max_emails (int): application setting
        """
        remaining_emails = sorted(
            self.emails,
            key=lambda email: email.verified_at,
            reverse=True,
        )[:max_emails]
        self.emails = [email for email in self.emails if email in remaining_emails]

    def is_verified(self) -> bool:
        """True if user has at least one verified email

        Returns:
            bool: verified result
        """
        for email in self.emails:
            if email.verified:
                return True
        return False

    def is_expired(self, expiry_time_hours: int) -> bool:
        """True if age of user is longer than
            expiry_time_hours and user is not verified

        Args:
            expiry_time_hours (int): application setting

        Returns:
            bool: whether the user is expired
        """

        return not self.is_verified() and (
            datetime.now() - self.created_at
        ) > timedelta(hours=expiry_time_hours)

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
            bool: true if the passwords match
        """
        return await password_crypt.verify_password(
            plain_password=password, hashed_password=self._password_hash
        )
