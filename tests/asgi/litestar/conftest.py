# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.app import create_app

transaction_state_key = "sql_transaction"


@pytest.fixture
async def litestar_client() -> AsyncTestClient:
    app = create_app()
    async with AsyncTestClient(
        app=app, raise_server_exceptions=True
    ) as litestar_client:
        yield litestar_client
