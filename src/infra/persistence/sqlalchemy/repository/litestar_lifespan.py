# Standard Library
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

# External Libraries
from litestar import Litestar
from litestar.datastructures import State as LitestarGlobalState
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# VerdanTech Source
from src import settings
from src.infra.persistence.generic.repository.exceptions import ClientLifecycleError

from .client import AlchemyClient
from .exceptions import alchemy_exception_map

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
        raise ClientLifecycleError(
            "SqlAlchemy client was expected to be initialized but no initialization has occured."
        )
    return client


@asynccontextmanager
async def get_alchemy_transaction(
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
    async with sessionmaker(bind=client.engine) as session:
        session.begin()
        try:
            with alchemy_exception_map():
                yield session
        except:
            await session.rollback()
            raise
        finally:
            if settings.ALCHEMY_TRANSACTION_COMMIT:
                await session.commit()


@asynccontextmanager
async def litestar_alchemy_client_lifespan(app: Litestar) -> AsyncGenerator[None, None]:
    """
    Initializes the SqlAlchemy client, yields, and then deinitializes.
    For use with Litestar's application lifespan.

    Args:
        app (Litestar): the Litestar application object,
            upon creation.
    """
    engine = create_async_engine(settings.ALCHEMY_URI)
    client = AlchemyClient(engine=engine)
    setattr(app.state, settings.ALCHEMY_CLIENT_NAME, client)

    await client.init()
    try:
        yield
    finally:
        await client.close()
