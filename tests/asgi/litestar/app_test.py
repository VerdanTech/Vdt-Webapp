# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.app import create_app


def test_create_app() -> None:
    """
    Ensure the litestar app can be instantiated with no errors.
    """
    app = create_app()
    assert app is not None


async def test_test_client() -> None:
    """
    Ensure a test client can be created.
    """
    app = create_app()
    async with AsyncTestClient(app=app):
        pass
