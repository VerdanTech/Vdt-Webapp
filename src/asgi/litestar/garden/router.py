# External Libraries
from litestar import Router

from . import urls
from .controllers import attributes, membership, write


def create_garden_router() -> Router:
    """
    Configure the garden router.
    """
    garden_router = Router(
        path=urls.GARDEN_ROUTER_URL_BASE,
        route_handlers=[
            attributes.GardenAttrsApiController,
            membership.GardenMembershipApiController,
            write.GardenWriteApiController,
        ],
    )
    return garden_router
