# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from litestar_svcs import SvcsPlugin
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.asgi.litestar.app import create_app
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import get_alchemy_client
from src.infra.persistence.sqlalchemy.repository.client import AlchemyClient
from src.infra.persistence.sqlalchemy.repository.exceptions import alchemy_exception_map
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import sessionmaker

@pytest.fixture
async def litestar_client() -> AsyncTestClient:
    app = create_app()
    async with AsyncTestClient(app=app, raise_server_exceptions=True) as client:
        # Replace the normal Sqlalchemy transaction to rollback transactions
        # on the scope of a test function.
        svcs_plugin = client.app.plugins.get(SvcsPlugin)
        registry_state_key = svcs_plugin._config.registry_state_key
        registry = getattr(client.app.state, registry_state_key, None)
        assert registry is not None

        alchemy_client = await get_alchemy_client(state=client.app.state)
        async with sessionmaker(bind=alchemy_client.engine) as session:
            session.begin()
            registry.register_value(AsyncSession, session) 
            try:
                with alchemy_exception_map():
                    yield client
            except:
                await session.rollback()
                raise

            session.rollback()

async def alchemy_test_transaction(client: AlchemyClient) -> None:
    """
    Begins a database transaction on the current engine scoped
    to the lifecycle of a test function, that rollbacks at the end,
    and yields the session object for use by repositories.

    Args:
        client (AlchemyClient): the current SqlAlchemy client.

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: the created
            AsyncSession transaction object.
    """
    async with sessionmaker(bind=client.engine) as session:
        session.begin()
        try:
            with alchemy_exception_map():
                yield session
        except:
            await session.rollback()
            raise
