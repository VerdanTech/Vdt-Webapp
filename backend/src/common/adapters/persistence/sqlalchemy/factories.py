# External Libraries
from litestar.datastructures import State as LitestarGlobalState
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Container

from .client import AlchemyClient
from .litestar_lifespan import get_alchemy_client


async def provide_alchemy_client(svcs_container: Container) -> AlchemyClient:
    """
    Provides a Sqlalchemy client for dependency injection.

    Args:
        svcs_container (Container): svcs service provider.

    Returns:
        AlchemyClient: the Sqlalchemy client stored in global state.
    """
    litestar_global_state = await svcs_container.aget(LitestarGlobalState)
    return await get_alchemy_client(state=litestar_global_state)
