# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.app import create_app


@pytest.fixture(scope="function")
async def litestar_client() -> AsyncTestClient:
    app = create_app()
    async with AsyncTestClient(app=app) as client:
        yield client
