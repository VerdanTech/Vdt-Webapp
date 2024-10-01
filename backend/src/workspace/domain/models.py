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
from src.garden.domain import Garden
from src.geometry.domain import Coordinate, Geometry


@value_transform
class Location(Value):
    """
    Value object which locates an object in
    space and time.

    Attributes:
        workspace_ref (Ref[Workspace]): a reference
            to the workspace that the coordinate
            is located in.
        position (Coordinate | None): the position of the
            object in the workspace. If None, the
            position is undetermined.
        time (datetime): the time that the object
            is located at the position.
    """

    workspace_ref: Ref["Workspace"]
    position: Coordinate | None
    time: datetime


@value_transform
class LocationHistory(Value):
    """
    Used to construct a history of locations for an object.

    Deltas between locations are assumed to be instantaneous.
    For example, if an object is located at position A at time 1,
    and moves to position B at time 2, the object is assumed to be
    located at position A all the way up until time 2.

    Attributes:
        locations (list[Location]): A chronological list of
            locations for the object.
    """

    locations: list[Location] = field(factory=list)


@entity_transform
class PlantingArea(Entity):
    """
    Describes an area in a workspace where
    plants are able to be placed.

    Attributes:
        name (str): A descriptive name for the planting area.
        geometry (Geometry): The shape of the planting area.
        location_history (LocationHistory): The location history
            of the planting area. For non-movable areas, this will
            be a single location.
        depth (float | None): The physical depth of the planting area.
            May be used to determine volume.
        movable (bool): Whether or not the planting area can be moved.
        description (str): A description of the planting area.
    """

    name: str  # type: ignore
    geometry: Geometry  # type: ignore
    location_history: LocationHistory = LocationHistory()
    depth: float | None = None
    movable: bool = False
    description: str = ""


@root_entity_transform
class Workspace(RootEntity):
    """
    Acts as a spatial reference point for all objects.

    Having multiple Workspaces in a Garden allows for
    segregation of physical contexts within a single model context.

    While objects may be moved between Workspaces, it is intended
    that Workspaces be defined such that routine changes in location
    take place within a single workspace.

    Attributes:
        garden_ref (Ref[Garden]): A reference to the Garden that the
            workspace is located in.
        name (str): A descriptive name for the workspace.
        slug (str): A unique identifier for the workspace, used for URLs.
            Must be unique within each Garden.
        description (str): A description of the workspace.
        planting_areas (list[PlantingArea]): A list of planting areas
            within the workspace. Note that because a PlantingArea
            contains a LocationHistory, it may be moved between Workspaces.
            The Workspace which contains the PlantingArea is the latest
            one which it has been moved to.
    """

    garden_ref: Ref[Garden]  # type: ignore
    name: str  # type: ignore
    slug: str  # type: ignore
    description: str = ""
    planting_areas: list[PlantingArea] = field(factory=list)
