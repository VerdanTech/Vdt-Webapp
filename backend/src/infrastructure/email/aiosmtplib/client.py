from email.mime.multipart import MIMEMultipart

from aiosmtplib import send as aiosmtp_send
from aiosmtplib.errors import SMTPException
from litestar.exceptions import InternalServerException

from ..generic import BaseEmailClient


class aioSMTPLibEmailClient(BaseEmailClient):
    async def send(
        self,
        message: MIMEMultipart,
        client_hostname: str,
        client_port: int,
        client_username: str,
        client_password: str,
    ) -> None:
        """Send the email using the client

        Args:
            message (MIMEMultipart): the email object to send
            hostname (str): SMTP server hostname
            port (int): SMTP server port
            username (str): client username
            password (str): client password

        Raises:
            InternalServerException: if the client's send
                protocal raises an exception
        """
        try:
            await aiosmtp_send(
                message,
                hostname=self.client_hostname,
                port=client_port,
                username=client_username,
                password=client_password,
                use_tls=True,
            )
        except SMTPException as exc:
            # log
            raise InternalServerException(
                detail="Email client execption", extra=str(exc)
            )
