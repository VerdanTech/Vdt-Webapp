# External Libraries
import pytest
from litestar.testing import AsyncTestClient
# VerdanTech Source
from src.asgi.litestar.app import create_app

transaction_state_key = "sql_transaction"


@pytest.fixture
async def litestar_client() -> AsyncTestClient:
    app = create_app()
    async with AsyncTestClient(app=app, raise_server_exceptions=True) as client:
        yield client

async def provide_alchemy_client_override() -> AlchemyClient:
    state = await svcs_container.aget(State)
    client = getattr(state, settings.ALCHEMY_CLIENT_NAME, None)
    if client is None:
        raise ClientLifecycleError(
            "SqlAlchemy client was expected to be initialized but no initialization has occured."
        )
    yield client