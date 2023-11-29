# External Libraries
from litestar import Router

from . import urls
from .controllers import (
    UserAuthController,
    UserReadController,
    UserVerificationController,
    UserWriteController,
)


def create_user_router() -> Router:
    user_router = Router(
        path=urls.USER_ROUTER_URL_BASE,
        route_handlers=[
            UserReadController,
            UserWriteController,
            # UserAuthController,
            # UserVerificationController,
        ],
    )
    return user_router
