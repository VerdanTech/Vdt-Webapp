# Standard Library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # External Libraries
    from litestar import Litestar


def create_app() -> "Litestar":
    # External Libraries
    from litestar import Litestar

    # VerdanTech Source
    from src.asgi.litestar.dependencies import svcs_plugin
    from src.asgi.litestar.exceptions import exception_handlers
    from src.asgi.litestar.lifespan import lifespan
    from src.asgi.litestar.router import create_base_router

    base_router = create_base_router()

    return Litestar(
        route_handlers=[base_router],
        lifespan=lifespan,
        plugins=[svcs_plugin],
        exception_handlers=exception_handlers,
        debug=True,
    )
