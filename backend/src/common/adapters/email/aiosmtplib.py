# Standard Library
from email.mime.multipart import MIMEMultipart

# External Libraries
from aiosmtplib import send as aiosmtp_send
from aiosmtplib.errors import SMTPException

# VerdanTech Source
from src.common.interfaces.email import exceptions

from .common import BaseEmailClient


class AioSmtplibEmailClient(BaseEmailClient):
    """
    Completes Implementation of the AbstractEmailClient interface
    using the aiosmtplib library.
    """

    async def send(
        self,
        message: MIMEMultipart,
    ) -> None:
        """
        Send the email using the client.

        Args:
            message (MIMEMultipart): the email object to send

        Raises:
            EmailError: if the client's send
                protocal raises an exception.
        """
        try:
            await aiosmtp_send(
                message,
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                use_tls=True,
            )
        except SMTPException as exc:
            raise exceptions.EmailError from exc
