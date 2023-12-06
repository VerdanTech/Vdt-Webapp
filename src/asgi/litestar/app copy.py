# Standard Library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # External Libraries
    from litestar import Litestar

# from .dependencies import application_layer_dependencies
# from .lifecycle import lifecycle
# from .router import base_router


def create_app() -> "Litestar":
    # External Libraries
    # External Libraries
    # from src.asgi.litestar.dependencies import application_layer_dependencies
    # from src.asgi.litestar.router import create_base_router
    # base_router = create_base_router()
    # TODO: fix litestar
    from litestar import Litestar, Rou

    app = Litestar(
        route_handlers=[base_router],
        # dependencies=application_layer_dependencies
    )
    return app
