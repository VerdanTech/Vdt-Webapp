# Standard Library
import asyncio
import pdb
from functools import partial
from typing import AsyncGenerator
from unittest import mock

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from testcontainers.postgres import PostgresContainer

# VerdanTech Source
from src.asgi.litestar.app import create_app
from tests.infra.persistence.sqlalchemy.repository.lifespan import (
    function_scoped_sql_transaction,
)


@pytest.fixture(scope="function")
async def litestar_client(postgres) -> AsyncGenerator[AsyncTestClient, None]:
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
    app = create_app(alchemy_uri=postgres.get_connection_url())

    async with AsyncTestClient(
        app=app,
        raise_server_exceptions=True,
    ) as litestar_client:
        # Retrieve svcs registry from litestar
        # svcs_plugin = litestar_client.app.plugins.get(SvcsPlugin)
        # registry_state_key = svcs_plugin._config.registry_state_key
        # registry = getattr(litestar_client.app.state, registry_state_key, None)
        # assert registry is not None
        # registry.register_factory(AsyncSession, provide_alchemy_transaction)

        yield litestar_client
