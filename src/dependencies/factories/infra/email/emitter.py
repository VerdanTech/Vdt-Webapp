# External Libraries
from litestar import Request as LitestarRequest
from svcs import Container

# VerdanTech Source
from src.infra.email.emitter.litestar import LitestarEmailEmitter
from src.interfaces.email.client import AbstractEmailClient

# async def provide_litestar_email_emitter(
#    svcs_container: Container, request: LitestarRequest
# ) -> LitestarEmailEmitter:
"""
Litestar email emitter to be injected into route handler.

Args:
    request (LitestarRequest): the litestar request object,
        registered automatically when injected as
        dependency into route handler.

Returns:
    EmailEmitter: email emitter callable.
"""
#    email_client = await svcs_container.aget_abstract(AbstractEmailClient)
#    return LitestarEmailEmitter(client=email_client, app=request.app)
