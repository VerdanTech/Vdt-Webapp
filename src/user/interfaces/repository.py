# Standard Library
from typing import Protocol

# VerdanTech Source
from src.common.domain import EntityIdType
from src.common.interfaces.persistence import AbstractRepository
from src.user.domain import User


class AbstractUserRepository(AbstractRepository[User], Protocol):
    """Data persistence interface for the User domain model"""

    entity = User

    async def add(self, user: User) -> User:
        """
        Persist a new user entity to the repository.

        Args:
            user (User): the user entity to add.

        Returns:
            User: the user entity after persistence.
        """
        ...

    async def update(self, user: User) -> User:
        """
        Persist an existing user entity to the repository.

        Args:
            user (User): user entity to update.

        Returns:
            User: the user entity after persistence.
        """
        ...

    async def get_by_ids(
        self, ids: EntityIdType | list[EntityIdType]
    ) -> User | list[User] | None:
        """
        Given an ID or list of IDs, return the user or users to whom they belong.

        Args:
            ids (EntityIdType | list[EntityIdType]): the ids to search for.

        Returns:
            User | list[User] | None: the found user or users, or None if no
                users were found.
        """
        ...

    async def get_by_usernames(
        self,
        usernames: str | list[str],
    ) -> User | list[User] | None:
        """
        Given a username or list of usernames, return the users to whom they belong.

        Args:
            usernames (str | list[str]): the usernames to search for.

        Returns:
            User | list[User] | None: the found user or users, or None if no
                users were found.
        """
        ...

    async def get_by_email_addresses(
        self, email_addresses: str | list[str]
    ) -> User | list[User] | None:
        """
        Given an email address list of email adresses,
        return the users to whom they belong.

        Args:
            email_addresss (str | list[str]): the email_addresss to search for.

        Returns:
            User | list[User] | None: the found user or users, or None if no
                users were found.
        """
        ...

    async def get_user_by_email_confirmation_key(
        self, email_confirmation_key: str
    ) -> User | None:
        """
        Given an email confirmation key, return the user with
        the email to whom it belongs.

        Args:
            key (str): email confirmation key.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        ...

    async def get_user_by_password_reset_confirmation(
        self, user_id: EntityIdType, password_reset_confirmation_key: str
    ) -> User | None:
        """
        Given a password reset key and user ID, return the user with
        the password reset confirmation and ID to whom they belong.

        Args:
            user_id (EntityIdType): the user's ID.
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
        Check the existence of an email_address in the repository.

        Args:
            email (str): the email to check uniqueness of.

        Returns:
            bool: true if the email exists.
        """
        ...

    async def email_confirmation_key_exists(self, key: str) -> bool:
        """
        Check the existence of an email confirmatiion key in the repository.

        Args:
            key (str): the email confirmation key to check uniqueness of.

        Returns:
            bool: true if the email confirmation key exists.
        """
        ...

    async def password_reset_confirmation_key_exists(self, key: str) -> bool:
        """
        Check the existence of an password reset confirmatiion key
        in the repository.

        Args:
            key (str): the password reset confirmation key to
                check uniqueness of.

        Returns:
            bool: true if the password reset confirmation key exists.
        """
        ...
