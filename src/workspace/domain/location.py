# Standard Library
from datetime import datetime

# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import Ref, Value, value_transform
from src.domain.geometry import Coordinate, Geometry

from .workspace import Workspace


@value_transform
class Location(Value):
    workspace_ref: Ref[Workspace]
    position: Coordinate | None
    time: datetime | None


@value_transform
class LocationHistory(Value):
    locations: set[Location] = field(factory=set)


@value_transform
class GeometryHistoryPoint(Value):
    geometry: Geometry
    time: datetime | None


@value_transform
class GeometricHistory(Value):
    geometry_points: set[GeometryHistoryPoint] = field(factory=set)
