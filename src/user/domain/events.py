# VerdanTech Source
from src.common.domain import EntityIdType, Event, event_transform


@event_transform
class UserCreated(Event):
    """
    Emitted when a new user is created.
    """

    userid: EntityIdType
    username: str
    email: str


@event_transform
class EmailPendingConfirmation(Event):
    """
    Emitted when a new email confirmation is required.
    """

    username: str
    email: str


@event_transform
class PasswordPendingReset(Event):
    """
    Emitted when a new password reset is required.
    """

    username: str
    email: str


@event_transform
class UserUpdated(Event):
    """
    Emitted when a user changes their username, email, or password.
    """

    userid: EntityIdType
    new_username: str | None
    new_email: str | None
