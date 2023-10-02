from src.verdantech_api import settings

from .client import aioSMTPLibEmailClient

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_aiosmtplib_client() -> aioSMTPLibEmailClient:
    return aioSMTPLibEmailClient(
        hostname=settings.EMAIL_CLIENT_HOSTNAME,
        port=settings.EMAIL_CLIENT_PORT,
        username=settings.EMAIL_CLIENT_USERNAME,
        password=settings.EMAIL_CLIENT_PASSWORD,
        sender=settings.EMAIL_CLIENT_SENDER,
    )


# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Base provider
aiosmtplib_client_provider = {settings.EMAIL_CLIENT_PK: provide_aiosmtplib_client}
