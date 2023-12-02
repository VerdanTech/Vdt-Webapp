# External Libraries
from litestar import Request as LitestarRequest

# VerdanTech Source
from src.interfaces.email.client import AbstractEmailClient

from .litestar import LitestarEmailEmitter


async def provide_litestar_email_emitter(
    email_client: AbstractEmailClient, request: LitestarRequest
) -> LitestarEmailEmitter:
    """
    Litestar email emitter to be injected into route handler.

    Args:
        request (LitestarRequest): the litestar request object,
            registered automatically when injected as
            dependency into route handler.

    Returns:
        EmailEmitter: email emitter callable.
    """
    return LitestarEmailEmitter(client=email_client, app=request.app)
