# Standard Library
from datetime import datetime

# External Libraries
from attrs import field
from src.geometry.domain import Coordinate, Geometry

# VerdanTech Source
from src.common.domain import (
    Entity,
    Ref,
    RootEntity,
    Value,
    entity_transform,
    root_entity_transform,
    value_transform,
)
from src.garden.domain import Garden


@value_transform
class Location(Value):
    workspace_ref: Ref["Workspace"]
    position: Coordinate | None
    time: datetime | None


@value_transform
class LocationHistory(Value):
    locations: list[Location] = field(factory=list)


@entity_transform
class PlantingArea(Entity):
    name: str  # type: ignore
    geometry: Geometry  # type: ignore
    location_history: LocationHistory = LocationHistory()
    description: str = ""
    depth: float | None = None
    movable: bool = False


@root_entity_transform
class Workspace(RootEntity):
    garden_ref: Ref[Garden]  # type: ignore
    name: str  # type: ignore
    slug: str  # type: ignore
    description: str = ""
    planting_areas: list[PlantingArea] = field(factory=list)
