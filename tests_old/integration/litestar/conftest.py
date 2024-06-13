# Standard Library
from typing import AsyncGenerator

# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src import settings
from src.entrypoints.litestar.app import create_app


@pytest.fixture(scope="function")
async def litestar_client(alchemy_transaction) -> AsyncGenerator[AsyncTestClient, None]:
    """
    Set up a test client for testing litestar routes.

    Replaces the SqlAlchemy client and transaction lifespan
    methods on the test client to allow for test-scoped transactions.

    Args:
        mocker (MockerFixture): pytest-mock

    Yields:
        Iterator[AsyncGenerator[AsyncTestClient, None]]: test client
            instance.
    """
    app = create_app(alchemy_uri=settings.ALCHEMY_URI)

    async with AsyncTestClient(
        app=app,
        raise_server_exceptions=True,
    ) as litestar_client:
        yield litestar_client
