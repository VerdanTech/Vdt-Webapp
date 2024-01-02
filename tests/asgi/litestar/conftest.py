# Standard Library
from typing import AsyncGenerator

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from pytest_mock import MockerFixture

# VerdanTech Source
from src.asgi.litestar.app import create_app

from .lifespan_overrides import (
    function_scoped_get_alchemy_transaction,
    function_scoped_litestar_alchemy_client_lifespan,
)



@pytest.fixture
async def litestar_client(
    mocker: MockerFixture,
) -> AsyncGenerator[AsyncTestClient, None]:
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
    mocker.patch(
        "src.asgi.litestar.app.litestar_alchemy_client_lifespan",
        new=function_scoped_litestar_alchemy_client_lifespan,
    )
    mocker.patch(
        "src.dependencies.factories.infra.persistence.sqlalchemy.get_alchemy_transaction",
        new=function_scoped_get_alchemy_transaction,
    )

    app = create_app()

    async with AsyncTestClient(
        app=app, raise_server_exceptions=True
    ) as litestar_client:
        yield litestar_client
