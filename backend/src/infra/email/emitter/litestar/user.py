from src import settings
from src.domain.common.entities import EntityIDType

from .generic import BaseLitestarEmailEmitter


class LitestarEmailEmitter(BaseLitestarEmailEmitter):
    async def emit_email_confirmation(
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

    async def emit_password_reset(
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
