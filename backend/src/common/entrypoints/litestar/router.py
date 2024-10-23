# Standard Library
from typing import List

# External Libraries
from litestar import Router

# VerdanTech Source
from src import settings
from src.cultivars.entrypoints.litestar.router import create_cultivar_router
from src.garden.entrypoints.litestar.router import create_garden_router
from src.user.entrypoints.litestar.router import create_user_router
from src.workspace.entrypoints.litestar.router import create_workspace_router

# List of all router factories
router_factories = [
    create_user_router,
    create_garden_router,
    create_cultivar_router,
    create_workspace_router,
]


def create_routers() -> List[Router]:
    """
    Create all router instances from factories.
    """
    routers = []
    for router_factory in router_factories:
        routers.append(router_factory())
    return routers


def create_base_router() -> Router:
    """
    Configure base router to plug into application root.
    """
    sub_routers = create_routers()
    base_router = Router(path=settings.API_URL_BASE, route_handlers=sub_routers)
    return base_router
