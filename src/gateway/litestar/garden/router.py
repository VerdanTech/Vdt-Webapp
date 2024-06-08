# External Libraries
from litestar import Router

from . import urls
from .controllers import membership, write


def create_garden_router() -> Router:
    """
    Configure the garden router.
    """
    garden_router = Router(
        path=urls.GARDEN_ROUTER_URL_BASE,
        route_handlers=[
            membership.GardenMembershipApiController,
            write.GardenWriteApiController,
        ],
    )
    return garden_router
