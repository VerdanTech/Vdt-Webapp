# Standard Library
import uuid
from datetime import datetime

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.user.entities import User, UserRef
from src.domain.user.values import Email
from src.ops.common import schema_dataclass

"""
Note: The UUID class is used directly instead of the EntityIdType alias
because Litestar schema generation currently types it as Any. 
"""


@schema_dataclass
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


@schema_dataclass
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
            id=user.id,
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


@schema_dataclass
class UserPublicSchema:
    """
    Schema for returning a detailed representation of a User,
    to other Users.
    """

    id: uuid.UUID
    username: str

    @classmethod
    def from_model(cls, user: User | UserRef) -> "UserPublicSchema":
        """
        Create an instance of the schema from a User.

        Args:
            user (User): the user to convert.

        Returns:
            UserSelfOutput: the schema result.
        """
        if user is User:
            return cls(
                id=user.id,
                username=user.username,
            )
        elif user is UserRef:
            return cls(
                id=user.id,
                username=user.username,
            )
        else:
            raise ValueError("Value of user argument must be of type User or UserRef.")
