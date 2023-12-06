# External Libraries
from litestar import Litestar, get


@get("/")
async def hello_world() -> dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}


def create_app() -> "Litestar":
    app = Litestar(route_handlers=[hello_world])
    return app
