# Standard Library
from datetime import datetime

# External Libraries
from attrs import field

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
from src.environment.domain import Environment
from src.garden.domain import Garden
from src.geometry.interface import Coordinate, Geometry


@root_entity_transform
class Workspace(RootEntity):
    garden_ref: Ref[Garden]  # type: ignore
    name: str  # type: ignore
    planting_areas: set["PlantingArea"] = field(factory=set)
    environment_ref: Ref[Environment] | None = None


@value_transform
class Location(Value):
    workspace_ref: Ref[Workspace]
    position: Coordinate | None
    time: datetime | None


@value_transform
class LocationHistory(Value):
    locations: set[Location] = field(factory=set)

    @property
    def undefined(self) -> bool:
        """
        Returns:
            bool: True if the Location has no defined locations. 
        """
        return (
            self.location_history.locations is None
            and self.geometric_history.geometries is None
            and self.seed_date is None
            and self.germ_date is None
            and self.first_harvest_date is None
            and self.last_harvest_date is None
            and self.expiry_date is None

@entity_transform
class PlantingArea(Entity):
    geometry: Geometry  # type: ignore
    location_history: LocationHistory = LocationHistory()
    movable: bool = False
    environment_ref: Ref[Environment] | None = None
