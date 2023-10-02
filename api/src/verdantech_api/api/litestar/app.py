from litestar import Litestar, get

from .dependencies import application_layer_dependencies
from .lifecycle import lifecycle
from .router import base_router

@get("/")
async def hello_world() -> dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}

def create_app() -> Litestar:
    return Litestar(
        # lifespan=[lifecycle],
        route_handlers=[hello_world],
        #dependencies=application_layer_dependencies,
    )
