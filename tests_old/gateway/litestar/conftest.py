# Standard Library
from typing import AsyncGenerator

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from litestar_svcs import SvcsPlugin
from svcs import Container, Registry

# VerdanTech Source
from mocks.dependencies.registry import configure_registry
from src import settings
from src.gateway.litestar.app import create_app
from src.interfaces.persistence.user.user import AbstractUserRepository

from .service_overrides import (
    provide_user_mock_repository,
    session_scoped_mock_user_repository,
)


@pytest.fixture(scope="function")
def mock_registry() -> Registry:
    registry = configure_registry()
    registry.register_factory(AbstractUserRepository, provide_user_mock_repository)
    return registry


@pytest.fixture(scope="function")
async def svcs_container(mock_registry: Registry) -> Container:
    return Container(registry=mock_registry)


@pytest.fixture(scope="function")
async def litestar_client(
    mock_registry: Registry,
) -> AsyncGenerator[AsyncTestClient, None]:
    """
    Set up a test client for testing litestar routes.

    Replaces the user repository dependency with a session-scoped

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
        # Retrieve and replace svcs registry from litestar
        svcs_plugin = litestar_client.app.plugins.get(SvcsPlugin)
        registry_state_key = svcs_plugin._config.registry_state_key
        registry = getattr(litestar_client.app.state, registry_state_key, None)
        assert registry is not None
        setattr(litestar_client.app.state, registry_state_key, mock_registry)
        yield litestar_client

    # Reset session-scoped services
    session_scoped_mock_user_repository.collection = []
