# Standard Library
from typing import List

# VerdanTech Source
from src.common.domain import EntityIdType
from src.common.interfaces.persistence.exceptions import ObjectNotFound
from src.user.domain import User
from src.user.interfaces.repository import AbstractUserRepository

from .base_repo_mock import MockBaseRepository


class MockUserRepository(MockBaseRepository[User], AbstractUserRepository):
    """Implementation of a mock user repository for testing"""

    entity = User
    touched_entities: list[User] = list()

    async def add(self, user: User) -> User:
        """
        Persist a new user entity to the repository.

        Args:
            user (User): the user entity to add.

        Returns:
            User: the user entity after persistence.
        """
        return self._add(user)

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
                self.touched_entities.append(user)
                return user
        raise ObjectNotFound("The user does not presently exist in the repository")

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
        """
        Given a user id, return the user to whom it belongs.

        Args:
            id (EntityIdType): the id to search for.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        raise NotImplementedError

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
        users = []
        for user in self.collection:
            if isinstance(usernames, str) and user.username == usernames:
                return user
            elif isinstance(usernames, list) and user.username in usernames:
                users.append(user)
        return users or None

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
        users = []
        for user in self.collection:
            for email in user.emails:
                if (
                    isinstance(email_addresses, str)
                    and email.address == email_addresses
                ):
                    return user
                elif (
                    isinstance(email_addresses, list)
                    and email.address in email_addresses
                ):
                    users.append(user)
        return users or None

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
