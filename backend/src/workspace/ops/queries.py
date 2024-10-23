# Standard Library
from datetime import datetime
from uuid import UUID

# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.ops.queries import Query, QueryResult, RefSchema, query_result_transform
from src.garden.domain.commands import GardenKey
from src.geometry.domain import Coordinate
from src.geometry.ops.queries import GeometricHistorySchema
from src.user.domain import User
from src.workspace.domain import Location, LocationHistory, PlantingArea, Workspace

# ======================================
# QueryResults
# ======================================


@query_result_transform
class LocationSchema(QueryResult[Location]):
    workspace_ref: RefSchema
    position: Coordinate | None
    time: datetime | None


@query_result_transform
class LocationHistorySchema(QueryResult[LocationHistory]):
    locations: list[LocationSchema]


@query_result_transform
class PlantingAreaSchema(QueryResult[PlantingArea]):
    id: UUID
    name: str
    geometries: GeometricHistorySchema
    location_history: LocationHistorySchema
    description: str
    depth: float | None
    movable: bool


@query_result_transform
class WorkspacePartialSchema(QueryResult[Workspace]):
    id: UUID
    garden_ref: RefSchema
    name: str
    slug: str


@query_result_transform
class WorkspaceFullSchema(QueryResult[Workspace]):
    id: UUID
    garden_ref: RefSchema
    name: str
    slug: str
    description: str
    planting_areas: list[PlantingAreaSchema]


# ======================================
# Queries
# ======================================


class WorkspaceGetPartialsQuery(Query):
    garden_key: GardenKey


class WorkspaceGetFullQuery(Query):
    garden_key: GardenKey
    workspace_slug: str  # TODO: Change to Pydantic object


# ======================================
# Query handlers
# ======================================


async def get_partials(
    query: WorkspaceGetPartialsQuery,
    svcs_container: Container,
    client: User | None,
) -> list[WorkspacePartialSchema]:
    """
    Retrieves the workspaces that
    are associated with a garden.

    Args:
        query (WorkspaceGetPartialsQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        list[WorkspacePartialSchema]: the workspaces associated with the garden.
    """
    ...


async def get_full(
    query: WorkspaceGetFullQuery,
    svcs_container: Container,
    client: User | None,
) -> WorkspaceFullSchema:
    """
    Retrieves a workspace full schema.

    Args:
        query (WorkspaceGetFullQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        WorkspaceFullSchema: a full representation of the workspace.
    """
    ...
