# External Libraries
from attr import define

from ..sqlalchemy.client import AlchemyClient


@define
class DatabaseClients:
    """Container for all required database clients."""

    alchemy_client: AlchemyClient
