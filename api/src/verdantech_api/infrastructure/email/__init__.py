from litestar import Request
from src.verdantech_api.domain.interfaces.email.client import AbstractEmailClient

from .aiosmtplib import provide_aiosmtplib_client
from .litestar_emitter import EmailEmitter

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_litestar_email_emitter(
    email_client: AbstractEmailClient, request: Request
) -> EmailEmitter:
    """Litestar email emitter bo be injected into route handler

    Args:
        request (Request): the litestar request object,
            registered automatically when injected as
            dependency into route handler

    Returns:
        EmailEmitter: email emitter callable
    """
    return EmailEmitter(client=email_client, request=request)
