# External Libraries
from litestar import Router

from . import urls
from .commands import UserCommandController
from .queries import UserViewController


def create_user_router() -> Router:
    """
    Configure the user router.
    """
    user_router = Router(
        path=urls.USER_ROUTER_URL_BASE,
        route_handlers=[UserCommandController, UserViewController],
    )
    return user_router
