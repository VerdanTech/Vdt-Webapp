# Standard Library
import uuid
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.domain import Ref
from src.common.ops.queries import Query, QueryResult, RefSchema, query_result_transform
from src.cultivars.domain import (
    Cultivar,
    CultivarAttributeSet,
    CultivarCollection,
    CultivarCollectionVisibilityEnum,
)
from src.garden.domain.commands import GardenKey
from src.user.domain import User

# ======================================
# QueryResults
# ======================================


@query_result_transform
class CultivarSchema(QueryResult[Cultivar]):
    id: uuid.UUID
    names: list[str]
    key: str
    scientific_name: str
    description: str
    parent_id: uuid.UUID | None
    created_at: datetime
    attributes: CultivarAttributeSet


@query_result_transform
class CultivarCollectionPartialSchema(QueryResult[CultivarCollection]):
    id: uuid.UUID
    name: str
    slug: str
    visibility: CultivarCollectionVisibilityEnum
    description: str
    tags: set[str]
    parent_ref: RefSchema | None
    user_ref: RefSchema | None
    garden_ref: RefSchema | None
    created_at: datetime


@query_result_transform
class CultivarCollectionFullSchema(QueryResult[CultivarCollection]):
    id: uuid.UUID
    name: str
    slug: str
    visibility: CultivarCollectionVisibilityEnum
    description: str
    tags: set[str]
    parent_ref: RefSchema | None
    user_ref: RefSchema | None
    garden_ref: RefSchema | None
    created_at: datetime
    cultivars: set[CultivarSchema]


@query_result_transform
class CultivarCollectionGetByGardenResult(QueryResult[None]):
    collections: set[CultivarCollectionPartialSchema]
    active_collection: Ref[CultivarCollection]


@query_result_transform
class CultivarCollectionGetByClientResult(QueryResult[None]):
    collections: set[CultivarCollectionPartialSchema]


# ======================================
# Queries
# ======================================


class CultivarCollectionGetByGardenQuery(Query):
    garden_key: GardenKey


class CultivarCollectionGetByIdsQuery(Query):
    cultivar_ids: list[uuid.UUID]


# ======================================
# Query handlers
# ======================================


async def get_by_garden(
    query: CultivarCollectionGetByGardenQuery,
    svcs_container: Container,
    client: User | None,
) -> CultivarCollectionGetByGardenResult:
    """
    Retrieves the cultivar collections that
    are associated with a garden.

    Args:
        query (CultivarCollectionGetByGardenQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        CultivarCollectionGetByGardenResult: references to the
            cultivar collections associated with the garden.
    """
    ...


async def get_by_client(
    svcs_container: Container, client: User | None
) -> CultivarCollectionGetByClientResult:
    """
    Retrieves the cultivar collections that
    are associated with the client.

    Returns:
        CultivarCollectionGetByClientResult: references to the
            cultivar collections associated with the gardens.
    """
    ...


async def get_by_ids(
    query: CultivarCollectionGetByIdsQuery,
    svcs_container: Container,
    client: User | None,
) -> list[CultivarCollectionFullSchema]:
    """
    Retrieves the cultivars by their ids.

    Args:
        query (CultivarCollectionGetByIdsQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        set[Cultivar]: the cultivars.
    """
    ...
