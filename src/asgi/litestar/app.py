# External Libraries
from litestar import Litestar
from litestar.datastructures import State

# VerdanTech Source
from src import settings
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import (
    litestar_alchemy_client_lifespan,
)

from .auth import jwt_cookie_auth
from .dependencies import svcs_plugin
from .openapi import openapi_config
from .router import create_base_router


def create_app(alchemy_uri: str = settings.ALCHEMY_URI) -> "Litestar":
    base_router = create_base_router()

    return Litestar(
        route_handlers=[base_router],
        lifespan=[litestar_alchemy_client_lifespan],
        plugins=[svcs_plugin],
        openapi_config=openapi_config,
        on_app_init=[jwt_cookie_auth.on_app_init],
        state=State({"alchemy_uri": alchemy_uri}),
        debug=True,
    )
