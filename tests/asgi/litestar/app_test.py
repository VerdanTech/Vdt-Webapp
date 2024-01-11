# External Libraries
import pytest

# VerdanTech Source
from src.asgi.litestar.app import create_app

pytestmark = [pytest.mark.asgi]


def test_create_app() -> None:
    """
    Ensure the litestar app can be instantiated with no errors.
    """
    app = create_app()
    assert app is not None
