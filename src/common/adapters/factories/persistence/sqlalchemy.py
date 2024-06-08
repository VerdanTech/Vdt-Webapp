# External Libraries
from litestar.datastructures import State as LitestarGlobalState
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Container

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy import AlchemyClient
from src.common.adapters.persistence.sqlalchemy import (
    get_alchemy_client,
)
from src.common.adapters.persistence.sqlalchemy.uow import AlchemyUow


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


async def provide_alchemy_uow(
    svcs_container: Container,
) -> AlchemyUow:
    """
    Provides a Unit Of Work with sqlalchemy for depedency injection.

    Args:
        svcs_container (Container): svcs service provider.

    Returns:
        AlchemyUow: provided unit of work.
    """
    client = await svcs_container.aget(AlchemyClient)
    return AlchemyUow(
        client=client
    )
