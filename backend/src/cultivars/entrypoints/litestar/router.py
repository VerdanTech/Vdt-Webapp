# External Libraries
from litestar import Router

from .commands import CultivarCommandController


def create_cultivar_router() -> Router:
    """
    Configure the cultivar router.
    """
    return Router(
        path="cultivars",
        route_handlers=[CultivarCommandController],
    )
