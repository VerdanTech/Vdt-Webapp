# Standard Library
from datetime import datetime
from typing import Annotated

# External Libraries
from pydantic import Field

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


class RectangleAttributesCreateUpdateCommand(Command):
    width: float
    height: float | None


class PolygonAttributesCreateUpdateCommand(Command):
    coordinates: list[CoordinateCreateUpdateCommand]


class EllipseAttributesCreateUpdateCommand(Command):
    width: float
    height: float | None


class LinesAttributesCreateUpdateCommand(Command):
    coordinates: list[CoordinateCreateUpdateCommand]


class GeometryCreateUpdateCommand(Command):
    type: GeometryTypeEnum
    rectangle_attributes: RectangleAttributesCreateUpdateCommand | None = None
    polygon_attributes: PolygonAttributesCreateUpdateCommand | None = None
    lines_attributes: EllipseAttributesCreateUpdateCommand | None = None
    ellipse_attributes: LinesAttributesCreateUpdateCommand | None = None
    scale_factor: float | None = None


class GeometricHistoryPointCreateUpdateCommand(Command):
    geometry: GeometryCreateUpdateCommand
    time: datetime | None = None


class GeometricHistoryCreateUpdateCommand(Command):
    geometries: list[GeometricHistoryPointCreateUpdateCommand]
