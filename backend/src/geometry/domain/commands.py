from datetime import datetime
from typing import Annotated
from pydantic import Field
# VerdanTech Source
from src.common.domain import Command
from .enums import GeometryTypeEnum

# ======================================
# Fields
# ======================================

CoordinateX = Annotated[
    str,
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["workspace_name"]["field"],
        json_schema_extra={
            "min_length": specs.values["workspace_name"][Specs.MIN_LENGTH],
            "max_length": specs.values["workspace_name"][Specs.MAX_LENGTH],
            "pattern": specs.values["workspace_name"][Specs.PATTERN],
        },
    ),
]

# ======================================
# Commands
# ======================================

class CoordinateCreateUpdateCommand(Command):
    x: float
    y: float
    z: float | None = None

class PolygonAttributesCreateUpdateCommand(Command):
    coordinates: list[CoordinateCreateUpdateCommand]

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