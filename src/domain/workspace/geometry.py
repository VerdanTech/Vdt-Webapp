# External Libraries
from shapely import LineString, Point, Polygon

# VerdanTech Source
from src.domain.common import Value, value_dataclass


@value_dataclass
class Coordinate(Value):
    point: Point


class Geometry(Value):
    pass


@value_dataclass
class Polygon(Geometry):
    polygon: Polygon


@value_dataclass
class Lines(Geometry):
    lines: LineString


@value_dataclass
class Circle(Geometry):
    point: Point
