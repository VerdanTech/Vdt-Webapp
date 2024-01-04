# Standard Library
import pdb
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from litestar import Litestar
from sqlalchemy.ext.asyncio import AsyncSession
from svcs import Container

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    
)
from sqlalchemy.pool import NullPool

# VerdanTech Source
from src import settings
from src.infra.persistence.sqlalchemy.repository import AlchemyClient
from tests.infra.persistence.sqlalchemy.repository.lifespan import (
    function_scoped_sql_transaction,
    session_scoped_sql_connection,
)

function_scoped_alchemy_transaction_key = "function_scoped_alchemy_transaction"
session_scoped_alchemy_connection_key = "session_scoped_alchemy_connection"

engine = create_async_engine(settings.ALCHEMY_URI, echo=True, poolclass=NullPool)

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

alchemy_client = AlchemyClient(engine=engine)

@asynccontextmanager
async def litestar_alchemy_client_lifespan(
    app: Litestar,
) -> AsyncGenerator[None, None]:
    """
    Initializes the SqlAlchemy client, begins a
    nested transaction, yields, and then deinitializes and rolls back.

    Used to override default Litestar SqlAlchemy client lifespan to
    use a single transaction over the life of the test function scope,
    as opposed to the request.

    Args:
        app (Litestar): the Litestar application object,
            upon creation.
    """
    async with session_scoped_sql_connection(client=alchemy_client) as connection:
        client = AlchemyClient(engine=connection.engine)
        setattr(client, session_scoped_alchemy_connection_key, connection)
        setattr(app.state, settings.ALCHEMY_CLIENT_NAME, client)
        yield


async def provide_alchemy_transaction(
    svcs_container: Container,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Provides a Sqlalchemy AsyncSession generator
    for transactional units of work.

    Used to override default Litestar SqlAlchemy client transaction to
    use a single transaction over the life of the test function scope,
    as opposed to the request.

    Args:
        svcs_container (Container): svcs service provider.

    Yields:
        Iterator[AsyncSession, None]: transaction generator.
    """
    client = await svcs_container.aget(AlchemyClient)
    if not hasattr(client, session_scoped_alchemy_connection_key):
        raise ValueError(
            "Session scoped transaction non-existant on application state."
        )
    connection = getattr(client, session_scoped_alchemy_connection_key)
    async with function_scoped_sql_transaction(connection=connection, close_transaction=False) as transaction:
        yield transaction
        await client.close()