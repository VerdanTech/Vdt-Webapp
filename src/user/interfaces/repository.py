# Standard Library
from typing import Protocol

# VerdanTech Source
from src.common.domain import EntityIdType
from src.user.domain import User

from src.common.interfaces.persistence import AbstractRepository


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

    async def add_many(self, users: list[User]) -> list[User]:
        """
        Persist a list of new user entities to the repository.

        Args:
            users (list[User]): the user entities to add.

        Returns:
            list[User]: the user entities after persistence.
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

    async def get_user_by_id(self, id: EntityIdType) -> User | None:
        """
        Given a user id, return the user to whom it belongs.

        Args:
            id (EntityIdType): the id to search for.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        ...

    async def get_users_by_ids(
        self, ids: list[EntityIdType], return_first_none: bool = False
    ) -> list[User] | None:
        """
        Given a list of user ids, return the users to whom they belong.

        Args:
            isd (list[EntityIdType]): the ids to search for.
            return_first_none (bool): if True, None is returned upon
                discerning that a username was provided that does
                not exist. Otherwise, a list is returned.

        Returns:
            list[User]: the found users, or None if any usernames
                did not exist and return_first_none is True.
        """
        ...

    async def get_user_by_username(self, username: str) -> User | None:
        """
        Given a username, return the user to whom it belongs.

        Args:
            username (str): the username to search for.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        ...

    async def get_users_by_usernames(
        self, usernames: list[str], return_first_none: bool = False
    ) -> list[User] | None:
        """
        Given a list of user usernames, return the users to whom they belong.

        Args:
            usernames (list[str]): the usernames to search for.
            return_first_none (bool): if True, None is returned upon
                discerning that a username was provided that does
                not exist. Otherwise, a list is returned.

        Returns:
            list[User]: the found users, or None if any usernames
                did not exist and return_first_none is True.
        """
        ...

    async def get_user_by_email_address(self, email_address: str) -> User | None:
        """
        Given an email address, return the user with the
        email to whom it belongs

        Args:
            email_address (str): the address to search for.

        Returns:
            User | None: the found user, or None if no user was found.
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
