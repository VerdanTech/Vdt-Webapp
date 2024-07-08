# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy import AlchemyClient

from .uow import DatabaseClients, StandardUow


async def provide_standard_uow(
    svcs_container: Container,
) -> StandardUow:
    """
    Provides a Unit Of Work for regular use.

    Args:
        svcs_container (Container): svcs service provider.

    Returns:
        StandardUow: provided unit of work.
    """
    client = await svcs_container.aget(AlchemyClient)
    return StandardUow(clients=DatabaseClients(alchemy_client=client))
