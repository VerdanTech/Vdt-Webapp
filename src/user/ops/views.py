# Standard Library
import uuid
from datetime import datetime

# VerdanTech Source
from src.user.domain import Email, User
from src.common.ops.common import schema

"""
Note: The UUID class is used directly instead of the EntityIdType alias
because Litestar schema generation currently types it as Any. 
"""


@schema
class EmailSchema:
    """Schema for returning a detailed representation of an Email."""

    address: str
    primary: bool
    verified: bool

    @classmethod
    def from_model(cls, email: Email) -> "EmailSchema":
        """
        Create an instance of the schema from an Email.

        Args:
            email (Email): the email to convert.

        Returns:
            EmailOutput: the schema result.
        """
        return cls(
            address=email.address,
            primary=email.primary,
            verified=email.verified,
        )


@schema
class UserFullSchema:
    """
    Schema for returning a detailed representation of a User
    to that User.
    """

    id: uuid.UUID
    username: str
    emails: list[EmailSchema]
    is_superuser: bool
    created_at: datetime | None

    @classmethod
    def from_model(cls, user: User) -> "UserFullSchema":
        """
        Create an instance of the schema from a User.

        Args:
            user (User): the user to convert.

        Returns:
            UserSelfOutput: the schema result.
        """
        return cls(
            id=user.id_or_error(),
            username=user.username,
            emails=[
                EmailSchema(
                    address=email.address,
                    primary=email.primary,
                    verified=email.verified,
                )
                for email in user.emails
            ],
            is_superuser=user.is_superuser,
            created_at=user.created_at,
        )


@schema
class UserPublicSchema:
    """
    Schema for returning a detailed representation of a User,
    to other Users.
    """

    id: uuid.UUID
    username: str

    @classmethod
    def from_model(cls, user: User) -> "UserPublicSchema":
        """
        Create an instance of the schema from a User.

        Args:
            user (User): the user to convert.

        Returns:
            UserSelfOutput: the schema result.
        """
        return cls(
            id=user.id_or_error(),
            username=user.username,
        )



# Standard Library
from typing import Optional

# VerdanTech Source
from src.common.domain import EntityIdType
from src.user.domain import User
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.ops.user.schemas.read import UserFullSchema, UserPublicSchema


class UserReadOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def profiles(
        self, client: User, user_ids: Optional[list[EntityIdType]]
    ) -> list[UserPublicSchema] | UserFullSchema:
        """
        Returns the client's full profile or a list of public profiles
        if a list of IDs is given.

        Args:
            client (User): the client user.
            user_ids (Optional[list[EntityIdType]]): an optional list of
                user profiles to retrieve.

        Returns:
            list[UserPublicSchema] | UserFullSchema: the full schema of the client
                or the public schemas of the requested IDs.
        """
        if user_ids is None:
            user_schema = UserFullSchema.from_model(client)
            return user_schema
        else:
            users = await self.user_repo.get_users_by_ids(
                ids=user_ids, return_first_none=True
            )
            if users is None:
                raise
            user_schemas = [UserPublicSchema.from_model(user) for user in users]
            return user_schemas
