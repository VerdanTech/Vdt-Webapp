# VerdanTech Source
from src import settings

from .aiosmtplib import AioSmtplibEmailClient


async def provide_aiosmtplib_client() -> AioSmtplibEmailClient:
    return AioSmtplibEmailClient(
        hostname=settings.EMAIL_CLIENT_HOSTNAME,
        port=settings.EMAIL_CLIENT_PORT,
        username=settings.EMAIL_CLIENT_USERNAME,
        password=settings.EMAIL_CLIENT_PASSWORD,
        sender=settings.EMAIL_CLIENT_SENDER,
    )
