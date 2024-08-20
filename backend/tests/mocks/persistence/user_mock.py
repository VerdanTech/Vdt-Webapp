# Standard Library
import uuid

# VerdanTech Source
from src.user.domain import User
from src.user.interfaces.repository import AbstractUserRepository

from .base_repo_mock import MockBaseRepository


class MockUserRepository(MockBaseRepository[User], AbstractUserRepository):
    """Implementation of a mock user repository for testing"""

    async def get_by_id(self, id: uuid.UUID) -> User | None:
        """
        Given an ID return the user to whom it belongs.

        Args:
            id (uuid.UUID): the id to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        for user in self.collection:
            if user.id == id:
                return user
        return None

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
        for user in self.collection:
            if user.username == username:
                return user
        return None

    async def get_by_email_address(self, email_address: str) -> User | None:
        """
        Given an email address return the user to whom it belongs.

        Args:
            email_address (str): the email addresss to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        for user in self.collection:
            for email in user.emails:
                if email.address == email_address:
                    return user
        return None

    async def get_by_email_confirmation_key(self, key: uuid.UUID) -> User | None:
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
                if email.confirmation is not None and email.confirmation.key == key:
                    return user
        return None

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
        for user in self.collection:
            if user.password_reset_confirmation is not None:
                if user.id == user_id and user.password_reset_confirmation.key == key:
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

    # ======================================
    # Query-focused methods
    # ======================================

    async def get_by_ids(self, ids: list[uuid.UUID]) -> list[User]:
        """
        Given a list of IDs return the users to whom they belong.

        Args:
            ids (list[uuid.UUID]): the ids to search for.

        Returns:
            list[User]: the found users.
        """
        return [user for user in self.collection if user.id in ids]

    async def get_by_usernames(self, usernames: list[str]) -> list[User]:
        """
        Given a list of usernames return the users to whom they belong.

        Args:
            usernames (list[str]): the usernames to search for.

        Returns:
            list[User]: the found users.
        """
        usernames_lower = [username.lower() for username in usernames]
        return [user for user in self.collection if user.id in usernames_lower]
