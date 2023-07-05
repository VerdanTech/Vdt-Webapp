from verdantech_api import settings

from .aiosmtplib import aioSMTPLibEmailClient


def provide_email_client() -> aioSMTPLibEmailClient:
    return aioSMTPLibEmailClient(
        hostname=settings.EMAIL_CLIENT_HOSTNAME,
        port=settings.EMAIL_CLIENT_PORT,
        username=settings.EMAIL_CLIENT_USERNAME,
        password=settings.EMAIL_CLIENT_PASSWORD,
        sender=settings.EMAIL_CLIENT_SENDER,
    )
