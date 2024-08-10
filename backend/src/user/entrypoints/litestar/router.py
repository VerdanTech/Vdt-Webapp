# External Libraries
from litestar import Router

from .auth import UserAuthController
from .commands import UserCommandController
from .queries import UserQueryController


def create_user_router() -> Router:
    """
    Configure the user router.
    """
    user_router = Router(
        path="users",
        route_handlers=[UserCommandController, UserQueryController, UserAuthController],
    )
    return user_router
