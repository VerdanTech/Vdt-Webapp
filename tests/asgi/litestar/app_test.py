import pytest
from src.asgi.litestar.app import create_app

def test_create_app() -> None:
    app = create_app()
    assert app is not None