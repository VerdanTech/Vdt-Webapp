# Standard Library
import uuid

# VerdanTech Source
from src.common.domain import EntityIdType, Event, event_transform


@event_transform
class UserCreated(Event):
    """
    Emitted when a new user is created.
    """

    userid: EntityIdType
    username: str
    email_address: str


@event_transform
class EmailPendingConfirmation(Event):
    """
    Emitted when a new email confirmation is required.
    """

    username: str
    email_address: str


@event_transform
class PasswordPendingReset(Event):
    """
    Emitted when a new password reset is required.
    """

    user_id: EntityIdType
    username: str
    email_address: str


@event_transform
class EmailConfirmationCreated(Event):
    """
    Emitted when an email confirmation has been created
    and is pending a notification.
    """

    email_address: str
    username: str
    key: uuid.UUID


@event_transform
class PasswordResetConfirmationCreated(Event):
    """
    Emitted when an passwor reset confirmation has been created
    and is pending a notification.
    """

    user_id: EntityIdType
    email_address: str
    username: str
    key: uuid.UUID
