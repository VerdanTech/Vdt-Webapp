# Standard Library
from typing import List

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.user.entities import User
from src.interfaces.persistence.exceptions import ObjectNotFound
from src.interfaces.persistence.user.repository import AbstractUserRepository

from .base_mock import MockBaseRepository


class MockUserRepository(MockBaseRepository[User], AbstractUserRepository):
    """Implementation of a mock user repository for testing"""

    entity = User

    async def add(self, user: User) -> User:
        """
        Persist a new user entity to the repository.

        Args:
            user (User): the user entity to add.

        Returns:
            User: the user entity after persistence.
        """
        return self._add(user)

    async def add_many(self, users: List[User]) -> List[User]:
        """
        Persist a list of new user entities to the repository.

        Args:
            users (list[User]): the user entities to add.

        Returns:
            list[User]: the user entities after persistence.
        """
        return self._add_many(users)

    async def update(self, user: User) -> User:
        """
        Persist an existing user entity to the repository.

        Args:
            user (User): user entity to update.

        Returns:
            User: the user entity after persistence.
        """
        for i, existing_user in enumerate(self.collection):
            if existing_user.id == user.id:
                self.collection[i] = user
                return user
        raise ObjectNotFound("The user does not presently exist in the repository")

    async def get_user_by_id(self, id: EntityIdType) -> User | None:
        """
        Given a user id, return the user to whom it belongs.

        Args:
            id (EntityIdType): the id to search for.

        Returns:
            User | None: the found user, or None if no user was found.
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
        for user in self.collection:
            for email in user.emails:
                if email.address == email_address:
                    return user
        return None

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
        for user in self.collection:
            for email in user.emails:
                if (
                    email.confirmation is not None
                    and email.confirmation.key == email_confirmation_key
                ):
                    return user
        return None

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
        for user in self.collection:
            if user.password_reset_confirmation is not None:
                if (
                    user.id == user_id
                    and user.password_reset_confirmation.key
                    == password_reset_confirmation_key
                ):
                    return user
        return None

    async def username_exists(self, username: str) -> bool:
        """
        Check the existence of a username in the repository.
        Username comparison should be case insensitive.

        Args:
            username (str): the username to check uniqueness of.

        Returns:
            bool: true if the username exists.
        """
        for user in self.collection:
            if user.username.lower() == username.lower():
                return True
        return False

    async def email_exists(self, email_address: str) -> bool:
        """
        Check the existence of an email_address in the repository.

        Args:
            email (str): the email to check uniqueness of.

        Returns:
            bool: true if the email exists.
        """
        for user in self.collection:
            for email in user.emails:
                if email.address == email_address:
                    return True
        return False

    async def email_confirmation_key_exists(self, key: str) -> bool:
        """
        Check the existence of an email confirmatiion key in the repository.

        Args:
            key (str): the email confirmation key to check uniqueness of.

        Returns:
            bool: true if the email confirmation key exists.
        """
        for user in self.collection:
            for email in user.emails:
                if email.confirmation is not None and email.confirmation.key == key:
                    return True
        return False

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
        for user in self.collection:
            if (
                user.password_reset_confirmation is not None
                and user.password_reset_confirmation.key == key
            ):
                return True
        return False
