# External Libraries
from litestar import Router

from . import urls
from .auth import UserAuthController
from .commands import UserCommandController
from .queries import UserQueryController


def create_user_router() -> Router:
    """
    Configure the user router.
    """
    user_router = Router(
        path=urls.USER_ROUTER_URL_BASE,
        route_handlers=[UserCommandController, UserQueryController, UserAuthController],
    )
    return user_router
