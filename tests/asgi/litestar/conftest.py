# External Libraries
import pytest
from litestar.testing import AsyncTestClient
# VerdanTech Source
from src.asgi.litestar.app import create_app

transaction_state_key = "sql_transaction"


@pytest.fixture
async def litestar_client() -> AsyncTestClient:
    app = create_app()
    async with AsyncTestClient(app=app, raise_server_exceptions=True) as litestar_client:

        #svcs_plugin = litestar_client.app.plugins.get(SvcsPlugin)
        #registry_state_key = svcs_plugin._config.registry_state_key
        #registry = getattr(litestar_client.app.state, registry_state_key, None)
        #assert registry is not None
        yield litestar_client