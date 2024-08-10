# Standard Library
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

# External Libraries
from litestar import Litestar
from litestar.datastructures import State as LitestarGlobalState
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

# VerdanTech Source
from src import settings
from src.common.interfaces.persistence import exceptions

from .client import AlchemyClient

sessionmaker = async_sessionmaker(expire_on_commit=False)


async def get_alchemy_client(state: LitestarGlobalState) -> AlchemyClient:
    """
    Provides the current AlchemyClient for dependency injection.

    Args:
        state (LitestarGlobalState): the Litestar application's global
            application state.

    Returns:
        AlchemyClient: the current SqlAlchemy client.
    """
    client = getattr(state, settings.ALCHEMY_CLIENT_NAME, None)
    if client is None:
        raise exceptions.RepositoryError(
            "SqlAlchemy client was expected to be initialized but no initialization has occured."
        )
    return client


@asynccontextmanager
async def litestar_alchemy_client_lifespan(app: Litestar) -> AsyncGenerator[None, None]:
    """
    Initializes the SqlAlchemy client, yields, and then deinitializes.
    For use with Litestar's application lifespan.

    Args:
        app (Litestar): the Litestar application object,
            upon creation.
    """
    uri = getattr(app.state, "alchemy_uri", None)
    if uri is None:
        raise exceptions.RepositoryError(
            "SqlAlchemy connection URI not set on Litestar application state."
        )

    engine = create_async_engine(uri)
    client = AlchemyClient(engine=engine)
    setattr(app.state, settings.ALCHEMY_CLIENT_NAME, client)

    await client.init()
    try:
        yield
    finally:
        await client.close()
