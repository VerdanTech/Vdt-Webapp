# Standard Library
import pdb
from collections.abc import AsyncGenerator

# External Libraries
from litestar.datastructures import State as LitestarGlobalState
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Container

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.client import AlchemyClient
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import (
    get_alchemy_client,
    get_alchemy_transaction,
)
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository


async def provide_alchemy_client(svcs_container: Container) -> AlchemyClient:
    litestar_global_state = await svcs_container.aget(LitestarGlobalState)
    return await get_alchemy_client(state=litestar_global_state)


async def provide_alchemy_transaction(
    svcs_container: Container,
) -> AsyncGenerator[AsyncSession, None]:
    client = await svcs_container.aget(AlchemyClient)
    async with get_alchemy_transaction(client=client) as transaction:
        yield transaction


async def provide_user_alchemy_repository(
    svcs_container: Container,
) -> UserAlchemyRepository:
    """Configure and provide a user sqlalchemy repository for dependency injection"""
    sql_transaction = await svcs_container.aget(AsyncSession)
    return UserAlchemyRepository(
        transaction=sql_transaction,
    )
