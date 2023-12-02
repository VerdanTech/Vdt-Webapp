# Standard Library
from typing import Any, Dict

# External Libraries
from litestar import Litestar
from litestar.events import listener

# VerdanTech Source
from src import settings
from src.domain.common import EntityIDType
from src.interfaces.email.client import AbstractEmailClient

from .generic import BaseEmailEmitter


@listener("emit_email")
async def emit_email_emitter(
    client: AbstractEmailClient,
    filepath: str,
    receiver: str,
    subject: str,
    **kwargs: Dict[str, Any],
) -> None:
    """Register the email client send function in Litestar's event system

    Args:
        filepath (str): the path to the email file
        receiver (str): the receiver of the message
        subject (str): the subject of the message
        kwargs (Dict[str, Any]): arguments to insert into html
    """
    await client.compile_and_send(
        filepath=filepath, receiver=receiver, subject=subject, **kwargs
    )


class LitestarEmailEmitter(BaseEmailEmitter):
    """Implementation of email emitter interface defined in interfaces"""

    def __init__(self, client: AbstractEmailClient, app: Litestar):
        self.client = client
        self.app = app

    def _emit(
        self, filepath: str, receiver: str, subject: str, **kwargs: Dict[str, Any]
    ) -> None:
        """Call the email emit event using request and client configured in __init__"""
        self.app.emit(
            "emit_email",
            client=self.client,
            filepath=filepath,
            receiver=receiver,
            subject=subject,
            **kwargs,
        )

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
        filepath = settings.EMAIL_FILEPATH_EMAIL_CONFIRMATION
        subject = settings.EMAIL_SUBJECT_EMAIL_CONFIRMATION
        client_base_url = settings.CLIENT_BASE_URL
        verification_url = settings.CLIENT_EMAIL_VERIFICATION_URL + key

        self._emit(
            filepath=filepath,
            receiver=email_address,
            subject=subject,
            username=username,
            client_base_url=client_base_url,
            verification_url=verification_url,
        )

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
        filepath = settings.EMAIL_FILEPATH_PASSWORD_RESET
        subject = settings.EMAIL_SUBJECT_PASSWORD_RESET
        client_base_url = settings.CLIENT_BASE_URL
        verification_url = settings.CLIENT_EMAIL_VERIFICATION_URL + key

        self._emit(
            filepath=filepath,
            receiver=email_address,
            subject=subject,
            username=username,
            user_id=user_id,
            client_base_url=client_base_url,
            verification_url=verification_url,
        )
