# Standard Library
from email.mime.multipart import MIMEMultipart
from unittest.mock import Mock

# VerdanTech Source
from src import settings
from src.adapters.email.client.aiosmtplib import AioSmtplibEmailClient


class MockEmailClient(AioSmtplibEmailClient):
    async def send(
        self,
        message: MIMEMultipart,
    ) -> None:
        return


async def provide_aiosmtplib_client() -> AioSmtplibEmailClient:
    return MockEmailClient(
        hostname=settings.EMAIL_CLIENT_HOSTNAME,
        port=settings.EMAIL_CLIENT_PORT,
        username=settings.EMAIL_CLIENT_USERNAME,
        password=settings.EMAIL_CLIENT_PASSWORD,
        sender=settings.EMAIL_CLIENT_SENDER,
    )
    # Todo: implement a test smtp server
    """
    return AioSmtplibEmailClient(
        hostname=settings.EMAIL_CLIENT_HOSTNAME,
        port=settings.EMAIL_CLIENT_PORT,
        username=settings.EMAIL_CLIENT_USERNAME,
        password=settings.EMAIL_CLIENT_PASSWORD,
        sender=settings.EMAIL_CLIENT_SENDER,
    )
    """
