# Standard Library
from typing import AsyncGenerator
from unittest import mock
import asyncio
# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from litestar_svcs import SvcsPlugin
from sqlalchemy.ext.asyncio import AsyncSession
from functools import partial

# VerdanTech Source
from src import settings
from src.asgi.litestar.app import create_app
from tests.infra.persistence.sqlalchemy.repository.lifespan import (
    function_scoped_sql_transaction,
)

from .lifespan_overrides import (
    provide_alchemy_transaction,
    litestar_alchemy_client_lifespan,
    session_scoped_alchemy_connection_key,
)

@pytest.fixture(scope="function")
async def sql_transaction(litestar_client: AsyncTestClient) -> AsyncGenerator[AsyncSession, None]:
    alchemy_client = getattr(litestar_client.app.state, settings.ALCHEMY_CLIENT_NAME)
    if not hasattr(alchemy_client, session_scoped_alchemy_connection_key):
        raise ValueError(
            "Session scoped connection non-existant on application client lifespan."
        )
    connection = getattr(alchemy_client, session_scoped_alchemy_connection_key)

    async with litestar_client.blocking_portal.call(partial(function_scoped_sql_transaction, connection=connection)) as transaction:
        return transaction
    #async with function_scoped_sql_transaction(connection=connection) as transaction:
        #yield transaction



@pytest.fixture(scope="session")
async def litestar_client() -> AsyncGenerator[AsyncTestClient, None]:
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

    app = create_app(lifespan=[litestar_alchemy_client_lifespan])

    async with AsyncTestClient(
        app=app, raise_server_exceptions=True, 
    ) as litestar_client:
        # Retrieve svcs registry from litestar
        svcs_plugin = litestar_client.app.plugins.get(SvcsPlugin)
        registry_state_key = svcs_plugin._config.registry_state_key
        registry = getattr(litestar_client.app.state, registry_state_key, None)
        assert registry is not None
        registry.register_factory(AsyncSession, provide_alchemy_transaction)

        yield litestar_client
