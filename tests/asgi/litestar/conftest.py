# Standard Library
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
import pytest
from litestar import Litestar
from litestar.testing import AsyncTestClient
from pytest_mock import MockerFixture
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# VerdanTech Source
from src import settings
from src.asgi.litestar.app import create_app
from src.infra.persistence.sqlalchemy.repository import AlchemyClient
from src.infra.persistence.sqlalchemy.repository.exceptions import alchemy_exception_map
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import sessionmaker
from tests.infra.persistence.sqlalchemy.repository.lifespan import test_scoped_sql_transaction

test_alchemy_transaction_key = "test_scoped_alchemy_transaction"
import pdb

@asynccontextmanager
async def test_scoped_litestar_alchemy_client_lifespan(
    app: Litestar,
) -> AsyncGenerator[None, None]:
    """
    Initializes the SqlAlchemy client, yields, and then deinitializes.
    For use with Litestar's application lifespan.

    Args:
        app (Litestar): the Litestar application object,
            upon creation.
    """
    engine = create_async_engine(settings.ALCHEMY_URI)
    client = AlchemyClient(engine=engine)
    await client.init()

    try:
        async with test_scoped_sql_transaction(client=client) as transaction:
            setattr(client, test_alchemy_transaction_key, transaction)
            setattr(app.state, settings.ALCHEMY_CLIENT_NAME, client)
            yield
    finally:
        await client.close()


@asynccontextmanager
async def test_scoped_get_alchemy_transaction(
    client: AlchemyClient,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Begins a database transaction on the current engine
    and yields the session object for use by repositories.

    Args:
        client (AlchemyClient): the current SqlAlchemy client.

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: the created
            AsyncSession transaction object.
    """

    if not hasattr(client, test_alchemy_transaction_key):
        print(client, test_alchemy_transaction_key)
        raise ValueError(
            "Test scoped transaction non-existant on application client lifespan."
        )
    transaction = getattr(client, test_alchemy_transaction_key)
    yield transaction


@pytest.fixture
async def litestar_client(mocker: MockerFixture
) -> AsyncGenerator[AsyncTestClient, None]:
    mocker.patch(
        "src.asgi.litestar.app.litestar_alchemy_client_lifespan",
        new=test_scoped_litestar_alchemy_client_lifespan,
    )
    mocker.patch(
        "src.dependencies.factories.infra.persistence.sqlalchemy.get_alchemy_transaction",
        new=test_scoped_get_alchemy_transaction,
    )

    app = create_app()

    async with AsyncTestClient(
        app=app, raise_server_exceptions=True
    ) as litestar_client:
        yield litestar_client
