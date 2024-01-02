# Standard Library
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from litestar import Litestar
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# VerdanTech Source
from src import settings
from src.infra.persistence.sqlalchemy.repository import AlchemyClient
from tests.infra.persistence.sqlalchemy.repository.lifespan import (
    function_scoped_sql_transaction,
)

test_alchemy_transaction_key = "test_scoped_alchemy_transaction"


@asynccontextmanager
async def function_scoped_litestar_alchemy_client_lifespan(
    app: Litestar,
) -> AsyncGenerator[None, None]:
    """
    Initializes the SqlAlchemy client, begins a
    nested transaction, yields, and then deinitializes and rolls back.
    
    Used to override default Litestar SqlAlchemy client lifespan to
    use a single transaction over the life of the application,
    as opposed to the request.

    Args:
        app (Litestar): the Litestar application object,
            upon creation.
    """
    engine = create_async_engine(settings.ALCHEMY_URI)
    client = AlchemyClient(engine=engine)
    await client.init()

    try:
        async with function_scoped_sql_transaction(client=client) as transaction:
            setattr(client, test_alchemy_transaction_key, transaction)
            setattr(app.state, settings.ALCHEMY_CLIENT_NAME, client)
            yield
    finally:
        await client.close()


@asynccontextmanager
async def function_scoped_get_alchemy_transaction(
    client: AlchemyClient,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Retrieves the transaction attached to the client.

    Used to override default Litestar SqlAlchemy client transaction to
    use a single transaction over the life of the application,
    as opposed to the request.

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
