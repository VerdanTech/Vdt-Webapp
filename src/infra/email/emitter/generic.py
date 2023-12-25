# Standard Library
from typing import Optional

# VerdanTech Source
from src import settings
from src.domain.common import EntityIDType
from src.interfaces.email.client import AbstractEmailClient


class BaseEmailEmitter:
    """
    Base class for implementing Email Emitter interface.

    Subclasses must implement the _send() method.
    """

    def __init__(self, client: AbstractEmailClient) -> None:
        self.client = client

    async def _send(
        self,
        filepath: str,
        receiver: str,
        subject: str,
        queue: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """
        Send the email or emit the email send event into an event queue.

        Args:
            filepath (str): filepath of the email.
            receiver (str): recipient email address.
            subject (str): email subject line.
            queue (Optional[bool]): if True, emits the email send
                into an event queue. If false, awaits the
                sending of the email within this method. Defaults to False.

        Raises:
            ValueError: if queue=True and no queue was supplied to the emitter.
        """
        raise NotImplementedError

    async def emit_user_email_confirmation(
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

        await self._send(
            filepath=filepath,
            receiver=email_address,
            subject=subject,
            queue=False,
            username=username,
            client_base_url=client_base_url,
            verification_url=verification_url,
        )

    async def emit_user_password_reset(
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

        await self._send(
            filepath=filepath,
            receiver=email_address,
            subject=subject,
            queue=True,
            username=username,
            user_id=user_id,
            client_base_url=client_base_url,
            verification_url=verification_url,
        )
