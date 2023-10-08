from typing import List

from litestar import Router
from src.verdantech_api import settings

from .user.router import create_user_router

router_factories = [create_user_router]


def create_routers() -> List[Router]:
    routers = []
    for router_factory in router_factories:
        routers.append(router_factory())
    return routers


def create_base_router() -> Router:
    sub_routers = create_routers()
    base_router = Router(path=settings.API_URL_BASE, route_handlers=sub_routers)
    return base_router
