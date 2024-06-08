# Standard Library
import uuid
from datetime import datetime

# VerdanTech Source
from src.domain.user import Email, User
from src.ops.common import schema

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
