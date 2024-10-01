# Standard Library
from datetime import datetime

# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import Value, value_transform

from .enums import GeometryTypeEnum


@value_transform
class Coordinate(Value):
    x: float
    y: float
    z: float | None = None


@value_transform
class PolygonAttributes(Value):
    shell_coordinates: list[Coordinate]
    hole_polygons: list[list[Coordinate]]


@value_transform
class EllipseAttributes(Value):
    width: float
    height: float | None = None


@value_transform
class LinesAttributes(Value):
    coordinates: list[Coordinate]


@value_transform
class Geometry(Value):
    type: GeometryTypeEnum
    polygon_attributes: PolygonAttributes | None = None
    lines_attributes: LinesAttributes | None = None
    ellipse_attributes: EllipseAttributes | None = None
    scale_factor: float = 1
    nulled: bool = False

    @property
    def attributes(self) -> PolygonAttributes | LinesAttributes | EllipseAttributes:
        ...


@value_transform
class GeometryHistoryPoint(Value):
    geometry: Geometry
    time: datetime | None = None


@value_transform
class GeometricHistory(Value):
    geometries: list[GeometryHistoryPoint] = field(factory=list)
