# Standard Library
from typing import List

# External Libraries
from sqlalchemy import func, select
from sqlalchemy.orm import make_transient_to_detached, noload, selectinload

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.user import User
from src.infra.persistence.sqlalchemy.mapper.user import UserAlchemyMapper
from src.infra.persistence.sqlalchemy.mapper.user.model import (
    EmailAlchemyModel,
    UserAlchemyModel,
)

from ..generic import BaseAlchemyRepository


class UserAlchemyRepository(BaseAlchemyRepository[User, UserAlchemyModel]):
    """SQLAlchemy implementation of user repository"""

    entity = User
    mapper = UserAlchemyMapper

    async def add(self, user: User) -> User:
        """
        Persist a new user entity to the repository.

        Args:
            user (User): the user entity to add.

        Returns:
            User: the user entity after persistence.
        """
        user_model = self._entity_to_model(user)
        self.transaction.add(user_model)
        await self.transaction.flush()
        self.transaction.expunge(user_model)
        user = self._model_to_entity(user_model)
        return user

    async def add_many(self, users: List[User]) -> List[User]:
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
        user_model = self._entity_to_model(user)
        make_transient_to_detached(user_model)
        user_model = await self.transaction.merge(user_model)
        self.transaction.add(user_model)
        await self.transaction.flush()
        user = self._model_to_entity(user_model)
        return user

    async def get_user_by_id(self, id: EntityIdType) -> User | None:
        """
        Given a user id, return the user to whom it belongs.

        Args:
            id (EntityIdType): the id to search for.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        statement = (
            select(UserAlchemyModel)
            .options(selectinload(UserAlchemyModel.emails))
            .filter(UserAlchemyModel.id == id)
        )
        query = await self.transaction.execute(statement)
        user_model = query.unique().scalar_one_or_none()

        if user_model is None:
            return None

        user = self._model_to_entity(user_model)
        return user

    async def get_user_by_email_address(self, email_address: str) -> User | None:
        """
        Given an email address, return the user with the
        email to whom it belongs

        Args:
            email_address (str): the address to search for.

        Returns:
            User | None: the found user, or None if no user was found.
        """
        statement = (
            select(EmailAlchemyModel)
            .options(selectinload(EmailAlchemyModel.user))
            .filter(EmailAlchemyModel.address == email_address)
        )
        query = await self.transaction.execute(statement)
        email_model = query.unique().scalar_one_or_none()

        if email_model is None:
            return None
        user_model = email_model.user

        user = self._model_to_entity(user_model)
        return user

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
        statement = (
            select(UserAlchemyModel)
            .filter(func.lower(UserAlchemyModel.username) == func.lower(username))
            .options(noload(UserAlchemyModel.emails))
        )
        query = await self.transaction.execute(statement)
        user_model = query.scalar_one_or_none()

        return user_model is not None

    async def email_exists(self, email_address: str) -> bool:
        """
        Check the existence of an email_address in the repository.

        Args:
            email (str): the email to check uniqueness of.

        Returns:
            bool: true if the email exists.
        """
        statement = (
            select(EmailAlchemyModel)
            .filter(EmailAlchemyModel.address == email_address)
            .options(noload(EmailAlchemyModel.user))
        )
        query = await self.transaction.execute(statement)
        email_model = query.scalar_one_or_none()

        return email_model is not None

    async def email_confirmation_key_exists(self, key: str) -> bool:
        """
        Check the existence of an email confirmatiion key in the repository.

        Args:
            key (str): the email confirmation key to check uniqueness of.

        Returns:
            bool: true if the email confirmation key exists.
        """
        statement = (
            select(EmailAlchemyModel)
            .filter(EmailAlchemyModel.confirmation_key == key)
            .options(noload(EmailAlchemyModel.user))
        )
        query = await self.transaction.execute(statement)
        email_model = query.scalar_one_or_none()

        return email_model is not None

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
        statement = (
            select(UserAlchemyModel)
            .filter(UserAlchemyModel.password_reset_confirmation_key == key)
            .options(noload(UserAlchemyModel.emails))
        )
        query = await self.transaction.execute(statement)
        user_model = query.scalar_one_or_none()

        return user_model is not None
