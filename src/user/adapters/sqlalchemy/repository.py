# Standard Library
import uuid

# External Libraries
from sqlalchemy import func, select

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy.repository import BaseAlchemyRepository
from src.user.domain import User
from src.user.domain.models import Email
from src.user.interfaces.repository import AbstractUserRepository

from .mapper import user_email_table, user_table


class UserAlchemyRepository(BaseAlchemyRepository[User], AbstractUserRepository):
    """SQLAlchemy implementation of user repository"""

    # ======================================
    # General methods
    # ======================================

    async def _add(self, entity: User) -> User:
        """
        Persist a new entity to the repository.

        Args:
            entity (User): the entity to add.

        Returns:
            User: the entity after persistence.
        """
        self.session.add(entity)
        return entity

    async def _update(self, entity: User) -> User:
        """
        Update an existing entity to the repository.

        Args:
            entity (User): the entity to update.

        Returns:
            User: the entity after persistence.
        """
        entity = await self.session.merge(entity)
        return entity

    async def _delete(self, entity: User) -> None:
        """
        Delete an existing entity from a repository.

        Args:
            entity (RootEntityT): the entity to delete.
        """
        await self.session.delete(entity)

    async def get_by_id(self, id: uuid.UUID) -> User | None:
        """
        Given an ID return the user to whom it belongs.

        Args:
            id (uuid.UUID): the id to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        statement = select(User).filter(user_table.c.id == id)
        query = await self.session.execute(statement)
        user = query.unique().scalar_one_or_none()
        return user

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
        statement = select(User).filter(
            func.lower(user_table.c.username) == username.lower()
        )
        query = await self.session.execute(statement)
        user = query.unique().scalar_one_or_none()

        if user is None:
            return None

        return user

    async def get_by_email_address(self, email_address: str) -> User | None:
        """
        Given an email address return the user to whom it belongs.

        Args:
            email_address (str): the email addresss to search for.

        Returns:
            User | None: the found user, or None if no
                user was found.
        """
        statement = (
            select(User)
            .join(user_email_table)
            .filter(user_email_table.c.address == email_address)
        )
        query = await self.session.execute(statement)
        user = query.unique().scalar_one_or_none()

        if user is None:
            return None

        return user

    async def get_by_email_confirmation_key(self, key: uuid.UUID) -> User | None:
        """
        Given an email confirmation key, return the user with
        the email to whom it belongs.

        Args:
            key (str): email confirmation key.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        statement = (
            select(User)
            .join(user_email_table)
            .filter(user_email_table.c.confirmation_key == key)
        )
        query = await self.session.execute(statement)
        user = query.unique().scalar_one_or_none()

        if user is None:
            return None

        return user

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
        statement = (
            select(User)
            .join(user_email_table)
            .filter(user_table.c.id == user_id)
            .filter(user_table.c.password_reset_confirmation_key == key)
        )
        query = await self.session.execute(statement)
        user = query.unique().scalar_one_or_none()
        return user

    async def username_exists(self, username: str) -> bool:
        """
        Check the existence of a username in the repository.
        Username comparison should be case insensitive.

        Args:
            username (str): the username to check uniqueness of.

        Returns:
            bool: true if the username exists.
        """
        statement = select(User).filter(
            func.lower(user_table.c.username) == func.lower(username)
        )
        query = await self.session.execute(statement)
        user = query.scalar_one_or_none()

        return user is not None

    async def email_exists(self, email_address: str) -> bool:
        """
        Check the existence of an email address in the repository.

        Args:
            email_address (str): the email to check existence of.

        Returns:
            bool: true if the email exists.
        """
        statement = select(Email).filter(user_email_table.c.address == email_address)
        query = await self.session.execute(statement)
        email = query.scalar_one_or_none()

        return email is not None

    # ======================================
    # Query-only methods
    # ======================================

    async def get_by_ids(self, ids: list[uuid.UUID]) -> list[User]:
        """
        Given a list of IDs return the users to whom they belong.

        Args:
            ids (list[uuid.UUID]): the ids to search for.

        Returns:
            list[User]: the found users.
        """
        statement = select(User).filter(user_table.c.id.in_(ids))
        query = await self.session.execute(statement)
        users = query.scalars().all()

        return list(users)