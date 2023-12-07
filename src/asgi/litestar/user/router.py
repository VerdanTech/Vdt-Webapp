# External Libraries
from litestar import Router

from . import urls
from .controllers import write


def create_user_router() -> Router:
    """
    Configure the user router.
    """
    user_router = Router(
        path=urls.USER_ROUTER_URL_BASE,
        route_handlers=[
            # UserReadController,
            write.UserWriteApiController,
            # UserAuthController,
            # UserVerificationController,
        ],
    )
    return user_router
