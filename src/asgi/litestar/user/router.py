# External Libraries
from litestar import Router

from . import urls
from .controllers import auth, read, verification, write


def create_user_router() -> Router:
    """
    Configure the user router.
    """
    user_router = Router(
        path=urls.USER_ROUTER_URL_BASE,
        route_handlers=[
            read.UserReadController,
            write.UserWriteApiController,
            auth.UserAuthApiController,
            verification.UserVerificationApiController,
        ],
    )
    return user_router
