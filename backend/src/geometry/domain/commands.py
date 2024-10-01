from datetime import datetime
# VerdanTech Source
from src.common.domain import Command
from .enums import GeometryTypeEnum

# ======================================
# Fields
# ======================================


# ======================================
# Commands
# ======================================

class CoordinateCreateUpdateCommand(Command):
    x: float
    y: float
    z: float | None = None

class PolygonAttributesCreateUpdateCommand(Command):
    shell_coordinates: list[CoordinateCreateUpdateCommand]
    hole_polygons: list[list[CoordinateCreateUpdateCommand]]


class EllipseAttributesCreateUpdateCommand(Command):
    width: float
    height: float | None

class LinesAttributesCreateUpdateCommand(Command):
    coordinates: list[CoordinateCreateUpdateCommand]

class GeometryCreateUpdateCommand(Command):
    type: GeometryTypeEnum
    polygon_attributes: PolygonAttributesCreateUpdateCommand | None = None
    lines_attributes: EllipseAttributesCreateUpdateCommand | None = None
    ellipse_attributes: LinesAttributesCreateUpdateCommand | None = None
    scale_factor: float | None = None

class GeometryHistoryPointCreateUpdateCommand(Command):
    geometry: GeometryCreateUpdateCommand
    time: datetime | None = None

class GeometricHistoryCreateUpdateCommand(Command):
    geometries: list[GeometryHistoryPointCreateUpdateCommand]