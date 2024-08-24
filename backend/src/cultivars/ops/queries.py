# Standard Library
import uuid
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src.user.domain import User
from src import exceptions, settings
from src.common.domain import Ref
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.queries import Query, QueryResult, query_result_transform
from src.cultivars.domain import Cultivar, CultivarCollection
from src.garden.domain.commands import GardenKey

# ======================================
# QueryResults
# ======================================


@query_result_transform
class CultivarGetByGardenResult(QueryResult[None]):
    collections: set[Ref[CultivarCollection]]
    active_collection: Ref[CultivarCollection]

@query_result_transform
class CultivarGetByClientResult(QueryResult[None]):
    collections: set[Ref[CultivarCollection]]

# ======================================
# Queries
# ======================================

class CultivarGetByGardenQuery(Query):
    garden_key: GardenKey


# ======================================
# Query handlers
# ======================================

async def get_by_garden(query: CultivarGetByGardenQuery, svcs_container: Container, client: User | None) -> CultivarGetByGardenResult:
    """
    Retrieves the cultivar collections that 
    are associated with a garden.

    Args:
        query (CultivarGetByGardenQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        CultivarGetByGardenResult: references to the
            cultivar collections associated with the garden.
    """
    ...

async def get_by_client(svcs_container: Container, client: User |None) -> CultivarGetByClientResult:
    """
    Retrieves the cultivar collections that
    are associated with the client.

    Returns:
        CultivarGetByClientResult: references to the
            cultivar collections associated with the gardens.
    """
    ...