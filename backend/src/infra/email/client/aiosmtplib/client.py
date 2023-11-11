from email.mime.multipart import MIMEMultipart

from aiosmtplib import send as aiosmtp_send
from aiosmtplib.errors import SMTPException
from litestar.exceptions import InternalServerException

from ..client.generic import BaseEmailClient


class aioSMTPLibEmailClient(BaseEmailClient):
    async def send(
        self,
        message: MIMEMultipart,
    ) -> None:
        """Send the email using the client

        Args:
            message (MIMEMultipart): the email object to send

        Raises:
            InternalServerException: if the client's send
                protocal raises an exception
        """
        try:
            await aiosmtp_send(
                message,
                hostname=self.client_hostname,
                port=self.client_port,
                username=self.client_username,
                password=self.client_password,
                use_tls=True,
            )
        except SMTPException as exc:
            # log
            raise InternalServerException(
                detail="Email client execption", extra=str(exc)
            )
