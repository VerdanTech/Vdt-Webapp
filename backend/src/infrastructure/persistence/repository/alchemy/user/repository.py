from typing import List

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from src.domain.common.entities import EntityIDType
from src.domain.user.entities import User
from src.infrastructure.persistence.mapper.alchemy.user import (
    UserAlchemyMapper,
)
from src.infrastructure.persistence.mapper.alchemy.user.model import (
    EmailAlchemyModel,
    UserAlchemyModel,
)

from ..exceptions import alchemy_exception_map
from ..generic import BaseAlchemyRepository


class UserAlchemyRepository(BaseAlchemyRepository[User]):
    """SQLAlchemy implementation of user repository"""

    entity = User
    mapper = UserAlchemyMapper

    async def add(self, user: User) -> User:
        """Persist a new user object to the repository

        Args:
            user (User): the user object to add

        Returns:
            User: the resultant persisted user object
        """
        # async with alchemy_exception_map():
        user_model = self._entity_to_model(user)
        self.session.add(user_model)
        await self.session.flush()
        self.session.expunge(user_model)
        user = self._model_to_entity(user_model)
        return user

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
        statement = (
            select(EmailAlchemyModel)
            .options(joinedload(EmailAlchemyModel.user))
            .filter(EmailAlchemyModel.address == email_address)
        )
        query = await self.session.execute(statement)
        email_model = query.scalar_one_or_none()

        if email_model is None:
            return None

        user_model = email_model.user

        user = self._model_to_entity(user_model)
        return user

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
        """Check the existence of a username in the repository

        Args:
            username (str): the username to check uniqueness of

        Returns:
            bool: true if the username exists
        """
        statement = select(UserAlchemyModel).filter(
            UserAlchemyModel.username == username
        )
        query = await self.session.execute(statement)
        user_model = query.scalar_one_or_none()

        return user_model is not None

    async def email_exists(self, email_address: str) -> bool:
        """Check the existence of an email address in the repository

        Args:
            email (str): the email to check uniqueness of

        Returns:
            bool: true if the email exists
        """
        statement = select(EmailAlchemyModel).filter(
            EmailAlchemyModel.address == email_address
        )
        query = await self.session.execute(statement)
        email_model = query.scalar_one_or_none()

        return email_model is not None

    async def email_confirmation_key_exists(self, key: str) -> bool:
        """Check the existence of an email confirmatiion key in the repository

        Args:
            key (str): the email confirmation key to check uniqueness of

        Returns:
            bool: true if the email confirmation key exists
        """
        statement = select(EmailAlchemyModel).filter(
            EmailAlchemyModel.confirmation_key == key
        )
        query = await self.session.execute(statement)
        email_model = query.scalar_one_or_none()

        return email_model is not None


    async def password_reset_confirmation_key_exists(self, key: str) -> bool:
        """Check the existence of an password reset confirmatiion key
            in the repository

        Args:
            key (str): the password reset confirmation key to
                check uniqueness of

        Returns:
            bool: true if the password reset confirmation key exists
        """
        statement = select(UserAlchemyModel).filter(
            UserAlchemyModel.password_reset_confirmation_key == key
        )
        query = await self.session.execute(statement)
        user_model = query.scalar_one_or_none()

        return user_model is not None
