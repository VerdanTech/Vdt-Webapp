# Standard Library
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.ops.queries import Query, QueryResult, RefSchema, query_result_transform
from src.garden.domain.commands import GardenKey
from src.geometry.domain import (
    Coordinate,
    EllipseAttributes,
    Geometry,
    GeometryTypeEnum,
    LinesAttributes,
    PolygonAttributes,
)
from src.geometry.ops.queries import GeometrySchema
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
    name: str
    geometry: GeometrySchema
    location_history: LocationHistorySchema
    description: str
    depth: float | None
    movable: bool


@query_result_transform
class WorkspaceSchema(QueryResult[Workspace]):
    garden_ref: RefSchema
    name: str
    slug: str
    description: str
    planting_areas: list[PlantingAreaSchema]


# ======================================
# Queries
# ======================================


class WorkspaceGetByBardenQuery(Query):
    garden_key: GardenKey


# ======================================
# Query handlers
# ======================================


async def get_by_garden(
    query: WorkspaceGetByBardenQuery,
    svcs_container: Container,
    client: User | None,
) -> list[WorkspaceSchema]:
    """
    Retrieves the workspaces that
    are associated with a garden.

    Args:
        query (WorkspaceGetByBardenQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.

    Returns:
        list[WorkspaceSchema]: the workspaces associated with the garden.
    """
    ...
