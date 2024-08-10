# Standard Library
import uuid

# VerdanTech Source
from src.common.domain import Event, event_transform


@event_transform
class UserCreatedEvent(Event):
    """
    Emitted when a new user is created.
    """

    userid: uuid.UUID
    username: str
    email_address: str


@event_transform
class EmailPendingConfirmationEvent(Event):
    """
    Emitted when a new email confirmation is required.
    """

    username: str
    email_address: str


@event_transform
class PasswordPendingResetEvent(Event):
    """
    Emitted when a new password reset is required.
    """

    user_id: uuid.UUID
    username: str
    email_address: str


@event_transform
class EmailConfirmationCreatedEvent(Event):
    """
    Emitted when an email confirmation has been created
    and is pending a notification.
    """

    email_address: str
    username: str
    key: uuid.UUID


@event_transform
class PasswordResetConfirmationCreatedEvent(Event):
    """
    Emitted when an passwor reset confirmation has been created
    and is pending a notification.
    """

    user_id: uuid.UUID
    email_address: str
    username: str
    key: uuid.UUID
