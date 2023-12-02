# Standard Library
from typing import Protocol

# VerdanTech Source
from src.domain.common import EntityIDType


class AbstractEmailEmitter(Protocol):
    """Interface for configuring and emitting emails into an event stream"""

    def emit_user_email_confirmation(
        self, email_address: str, username: str, key: str
    ) -> None:
        """
        The email confirmation email provides a url to a page on the
        client that hits the email_confirmation_confirm endpoint,
        allowing emails to be verified.

        Args:
            email_address (str): the email address to send to
            username (str): the username of the user
        """
        ...

    def emit_user_password_reset(
        self, email_address: str, username: str, user_id: EntityIDType, key: str
    ) -> None:
        """
        The password reset email provides a url to a page on the client
        that allows hitting the password_reset_confirm endpoint with a
        user id, key, and new password.

        Args:
            email_address (str): the email address to send to
            username (str): the username of the user
            user_id (EntityIDType): the ID of the user
        """
        ...
