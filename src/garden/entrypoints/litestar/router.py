# External Libraries
from litestar import Router

from . import urls
from .commands import GardenCommandController
from .queries import GardenQueryController


def create_garden_router() -> Router:
    """
    Configure the garden router.
    """
    garden_router = Router(
        path=urls.GARDEN_ROUTER_URL_BASE,
        route_handlers=[GardenCommandController, GardenQueryController],
    )
    return garden_router
