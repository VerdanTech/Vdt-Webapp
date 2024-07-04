# Standard Library
import uuid
from typing import Protocol

# VerdanTech Source
from src.common.interfaces.persistence import AbstractRepository
from src.user.domain import User


class AbstractUserRepository(AbstractRepository[User], Protocol):
    """Data persistence interface for the User domain model"""

    # ======================================
    # General methods
    # ======================================

    async def get_by_id(self, id: uuid.UUID) -> User | None:
        """
        Given an ID return the user to whom it belongs.

        Args:
            id (uuid.UUID): the id to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        ...

    async def get_by_username(
        self,
        username: str,
    ) -> User | None:
        """
        Given a username, return the users to whom it belongs.

        Args:
            username (str): the username to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        ...

    async def get_by_email_address(self, email_address: str) -> User | None:
        """
        Given an email address return the user to whom it belongs.

        Args:
            email_address (str): the email addresss to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        ...

    async def get_by_email_confirmation_key(self, key: uuid.UUID) -> User | None:
        """
        Given an email confirmation key, return the user with
        the email to whom it belongs.

        Args:
            key (str): email confirmation key.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        ...

    async def get_by_password_reset_confirmation(
        self, user_id: uuid.UUID, key: uuid.UUID
    ) -> User | None:
        """
        Given a password reset key and user ID, return the user with
        the password reset confirmation and ID to whom they belong.

        Args:
            user_id (uuid.UUID): the user's ID.
            key (str): password reset confirmation key.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        ...

    async def username_exists(self, username: str) -> bool:
        """
        Check the existence of a username in the repository.
        Username comparison should be case insensitive.

        Args:
            username (str): the username to check uniqueness of.

        Returns:
            bool: true if the username exists.
        """
        ...

    async def email_exists(self, email_address: str) -> bool:
        """
        Check the existence of an email address in the repository.

        Args:
            email_address (str): the email to check existence of.

        Returns:
            bool: true if the email exists.
        """
        ...

    # ======================================
    # Query-only methods
    # ======================================
