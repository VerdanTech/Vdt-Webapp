from typing import List

from src.verdantech_api.domain.models.user.entities import User

from ..generic import MockBaseRepository


class MockUserRepository(MockBaseRepository[User]):
    """Implementation of a mock user repository for testing"""

    entity = User

    async def add(self, user: User) -> User:
        """Persist a user object to the repository

        Args:
            user (User): the user object to add

        Returns:
            User: the resultant persisted user object
        """
        return self._add(user)

    async def add_many(self, users: List[User]) -> List[User]:
        """Persist a list of user objects to the repository

        Args:
            users (List[User]): the user objects to add

        Returns:
            List[User]: the resultant persisted user objects
        """
        return self._add_many(users)

    async def username_exists(self, username: str) -> bool:
        """Check the existence of a username in the repository

        Args:
            username (str): the username to check uniqueness of

        Returns:
            bool: true if the username exists
        """
        for user in self.collection:
            if user.username == username:
                return True
        return False

    async def email_exists(self, email: str) -> bool:
        """Check the existence of an email in the repository

        Args:
            email (str): the email to check uniqueness of

        Returns:
            bool: true if the email exists
        """
        for user in self.collection:
            for email in user.emails:
                if email.address == email:
                    return True
        return False

    async def email_confirmation_key_exists(self, key: str) -> bool:
        """Check the existence of an email confirmatiion key in the repository

        Args:
            key (str): the email confirmation key to check uniqueness of

        Returns:
            bool: true if the email confirmation key exists
        """
        for user in self.collection:
            for email in user.emails:
                if email.confirmation.key == key:
                    return True
        return False

    async def password_reset_confirmation_key_exists(self, key: str) -> bool:
        """Check the existence of an password reset confirmatiion key
            in the repository

        Args:
            key (str): the password reset confirmation key to
                check uniqueness of

        Returns:
            bool: true if the password reset confirmation key exists
        """
        for user in self.collection:
            if user.password_reset_confirmation.key == key:
                return True
        return False
