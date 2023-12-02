# Standard Library
from typing import List

# VerdanTech Source
from src.domain.common import EntityIDType
from src.domain.user.entities import User

from ..generic import AbstractAsyncRepository


class AbstractUserRepository(AbstractAsyncRepository[User]):
    """Data persistence interface for the User domain model"""

    entity = User

    async def add(self, user: User) -> User:
        """Persist a new user object to the repository

        Args:
            user (User): the user object to add

        Returns:
            User: the resultant persisted user object
        """
        ...

    async def add_many(self, users: List[User]) -> List[User]:
        """Persist a list of new user objects to the repository

        Args:
            users (List[User]): the user objects to add

        Returns:
            List[User]: the resultant persisted user objects
        """
        ...

    async def update(self, user: User) -> User:
        """Persist an existing user object to the repository

        Args:
            user (User): user object to update

        Returns:
            User: the resultant persisted user object
        """
        ...

    async def get_user_by_email_address(self, email_address: str) -> User | None:
        """Given an email address, return the user with the
            email to whom it belongs

        Args:
            email_address (str): the address to search for

        Returns:
            User | None: the found user, or None if no user was found
        """
        ...

    async def get_user_by_email_confirmation_key(
        self, email_confirmation_key: str
    ) -> User | None:
        """Given an email confirmation key, return the user with
            the email to whom it belongs

        Args:
            key (str): email confirmation key

        Returns:
            User | None: the found user, or None if no user was found
        """
        ...

    async def get_user_by_password_reset_confirmation(
        self, user_id: EntityIDType, password_reset_confirmation_key: str
    ) -> User | None:
        """Given a password reset key and user ID, return the user with
            the password reset confirmation and ID to whom they belong

        Args:
            user_id (EntityIDType): the user's ID
            key (str): password reset confirmation key

        Returns:
            User | None: the found user, or None if no user was found
        """
        ...

    async def username_exists(self, username: str) -> bool:
        """Check the existence of a username in the repository.
            Username comparison should be case insensitive.

        Args:
            username (str): the username to check uniqueness of

        Returns:
            bool: true if the username exists
        """
        ...

    async def email_exists(self, email_address: str) -> bool:
        """Check the existence of an email_address in the repository

        Args:
            email (str): the email to check uniqueness of

        Returns:
            bool: true if the email exists
        """
        ...

    async def email_confirmation_key_exists(self, key: str) -> bool:
        """Check the existence of an email confirmatiion key in the repository

        Args:
            key (str): the email confirmation key to check uniqueness of

        Returns:
            bool: true if the email confirmation key exists
        """
        ...

    async def password_reset_confirmation_key_exists(self, key: str) -> bool:
        """Check the existence of an password reset confirmatiion key
            in the repository

        Args:
            key (str): the password reset confirmation key to
                check uniqueness of

        Returns:
            bool: true if the password reset confirmation key exists
        """
        ...
