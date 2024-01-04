# Standard Library
from dataclasses import field
from datetime import datetime, timedelta
from typing import List, Optional

# VerdanTech Source
from src.domain import exceptions as domain_exceptions
from src.domain.common import EntityIdType, RootEntity, root_entity_dataclass
from src.interfaces.security.crypt import AbstractPasswordCrypt

from . import exceptions
from .values import Email, PasswordResetConfirmation


@root_entity_dataclass
class User(RootEntity):
    """User entity model"""

    username: str
    emails: List[Email] = field(default_factory=list)
    _password_hash: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    password_reset_confirmation: Optional[PasswordResetConfirmation] = None

    def email_create(
        self,
        address: str,
        max_emails: int,
        verification: Optional[bool] = False,
        email_confirmation_key: Optional[str] = None,
    ) -> None:
        """
        Add a new email to the user. The verification process is optional.
        The behaviour of the email creation process depends on whether
        it is the first email to be created and whether the verification process
        is being used:

        First email, no verification:
            - Email begins verified.
            - Email begins primary.

        First email, verification:
            - Email begins unverified.
            - Email begins primary.

        Non-first email, no verification:
            - Email begins verified.
            - Email begins primary.
            - All other emails are made unprimary.
            - Oldest emails are trimmed.

        Non-first email, verification:
            - Email begins unverified.
            - Email begins unprimary
            - Upon verification, is made primary and oldest emails are trimmed.

        Args:
            address (str): the address of the email to add.
            max_emails (int): maximum emails stored in a User, application setting.
            verification (Optional[bool]): whether to undergo email
                confirmation process on the new email.
            email_confirmation_key (Optional[str]): the confirmation key,
                if verification is True.
        """
        # If verification is not being performed,
        # the email begins verified
        begin_verified = not verification

        # Email is only made primary if it is the first
        # to be added or if it is already verified
        first_email = self.emails == []
        begin_primary = first_email or begin_verified

        email = Email(address=address, primary=begin_primary, verified=begin_verified)

        # Create a new email confirmation if required
        if verification:
            if email_confirmation_key is None:
                raise ValueError(
                    """Argument email_confirmation_key is required 
                    if argument verification is True; None was passed."""
                )
            email = email.new_confirmation(key=email_confirmation_key)

        self.emails.append(email)

        # If other emails exist, and the new email is already
        # verified, the primary status of all emails must be
        # updated and the oldest emails must be trimmed.
        if not first_email and begin_verified:
            self._set_primary_email(email)
            self._trim_oldest_emails(max_emails=max_emails)

    def get_primary_email(self) -> Email:
        """
        Return the user's primary email

        Raises:
            UserIntegrityError: if the user has no primary emails.

        Returns:
            Email: the primary email.
        """
        for email in self.emails:
            if email.primary is True:
                return email
        raise exceptions.UserIntegrityError("User has zero emails with primary = True")

    def email_confirmation_create(self, address: str, key: str) -> None:
        """
        Given an existing email address and confirmation key,
        generate a new confirmation and replace the email.

        Args:
            address (str): email address to make confirmation for.
            key (str): confirmation key to make confirmation with.
        """
        for index, email in enumerate(self.emails):
            if email.address == address:
                email = email.new_confirmation(key=key)
                self.emails[index] = email
                return
        raise domain_exceptions.FieldNotFound(
            "The email address provided does not exist on this User."
        )

    def email_confirmation_confirm(
        self, key: str, max_emails: int, expiry_time_hours: int
    ) -> None:
        """
        Given a verification key, verify the email
        and set it as primary, ensuring the email
        confirmation is not expired.

        Args:
            key (str): email confirmation key.
            max_emails (int): maximum emails stored in a User, application setting.
            expiry_time_hours (int): the amount of hours an EmailConfirmation
                can exist before it expires. Application setting.
        """
        email = self._get_email_by_confirmation_key(key=key)
        email.check_confirmation_expired(expiry_time_hours=expiry_time_hours)
        email = email.verify()
        self._set_primary_email(email)
        self._trim_oldest_emails(max_emails=max_emails)

    async def set_password(
        self,
        password: str,
        password_crypt: AbstractPasswordCrypt,
        overwrite: bool = False,
    ) -> None:
        """
        Generate and set hashed password given plaintext password.
        Require overwrite as True if password already exists to
        prevent accidental overwrite.

        Args:
            password (str): plaintext password to hash and set.
            password_crypt (AbstractPasswordCrypt): encryption interface.
            overwrite (bool): whether to allow overwriting existing password.
                Defaults to False.

        Raises:
            PasswordAlreadySetException: raised if password is already set,
                but the function was called with overwrite=False.
        """
        if self._password_hash is not None and not overwrite:
            raise exceptions.PasswordAlreadySetError(
                """Password set attempt failed: 
                called with overwrite=False 
                but password already set.
                """
            )
        self._password_hash = await password_crypt.get_password_hash(
            plain_password=password
        )

    def password_reset_create(self, key: str) -> None:
        """
        Given a verification key, open a new password reset
        confirmation request on the user object.

        Args:
            key (str): the key to set on the reset confirmation.
        """
        self.password_reset_confirmation = PasswordResetConfirmation(key=key)

    async def password_reset_confirm(
        self,
        user_id: EntityIdType,
        key: str,
        new_password: str,
        password_crypt: AbstractPasswordCrypt,
    ) -> None:
        """
        Confirm and close a password reset request by setting the new password
        only if the provided key is correct.

        Args:
            user_id (EntityIdType): the id of the user on the password reset confirmation.
            key (str): the password reset confirmation key.
            new_password (str): the new password to set.
            password_crypt (AbstractPasswordCrypt): password crypt interface.
        """
        if not user_id == self.id:
            raise exceptions.PasswordResetConfirmationNotValid(
                "The provided password reset confirmation is not correct."
            )

        if self.password_reset_confirmation is None:
            raise exceptions.PasswordResetConfirmationNotFound(
                "No password reset requests are associated with this User."
            )

        if not self.password_reset_confirmation.key == key:
            raise exceptions.PasswordResetConfirmationNotValid(
                "The provided password reset key is not correct."
            )

        await self.set_password(
            password=new_password, password_crypt=password_crypt, overwrite=True
        )
        self.password_reset_confirmation = None

    async def verify_password(
        self, password: str, password_crypt: AbstractPasswordCrypt
    ) -> bool:
        """
        Check input password against user's password.

        Args:
            password (str): the password to check.
            password_crypt (AbstractPasswordCrypt): encryption class.

        Returns:
            bool: true if the passwords match.
        """
        if self._password_hash is None:
            return False
        return await password_crypt.verify_password(
            plain_password=password, hashed_password=self._password_hash
        )

    def is_verified(self) -> bool:
        """
        True if user has at least one verified email.

        Returns:
            bool: verified result.
        """
        for email in self.emails:
            if email.verified:
                return True
        return False

    def is_expired(self, expiry_time_hours: int) -> bool:
        """
        True if age of user is longer than
        expiry_time_hours and user is not verified

        Args:
            expiry_time_hours (int): amount of hours it takes for an
                unverified User to expire, application setting.

        Returns:
            bool: whether the user is expired.
        """
        if self.created_at is None:
            return False
        return not self.is_verified() and (
            datetime.now() - self.created_at
        ) > timedelta(hours=expiry_time_hours)

    def _get_email_by_confirmation_key(self, key: str) -> Email:
        """
        Given an email confirmation key, return the
        email on the user with a matching key,
        or raise an exception if not found.

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
            raise exceptions.EmailConfirmationKeyNotFound(
                "The email verification key does not exist"
            )
        return email_with_key

    def _set_primary_email(self, new_primary_email: Email) -> None:
        """
        Make the given email the only email in the user's
        list of email with primary=True. The email may
        or may not already exist.

        Args:
            new_primary_email (Email): the email to make primary.
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

    def _trim_oldest_emails(self, max_emails: int) -> None:
        """
        Remove the emails that were verified the longest
        time ago and which put the user over their max emails.

        Args:
            max_emails (int): the maximum amount of emails able to be
                stored on a User, application setting.
        """
        remaining_emails = sorted(
            self.emails,
            key=lambda email: email.verified_at or datetime.min,
            reverse=True,
        )[:max_emails]
        self.emails = [email for email in self.emails if email in remaining_emails]
