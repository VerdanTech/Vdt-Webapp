from datetime import datetime
# VerdanTech Source
from src.geometry.domain.models import GeometricHistory, GeometricHistoryPoint
from src.common.ops.queries import QueryResult, query_result_transform
from src.geometry.domain import (
    Coordinate, RectangleAttributes,
    EllipseAttributes,
    Geometry,
    GeometryTypeEnum,
    LinesAttributes,
    PolygonAttributes,
)
# ======================================
# QueryResults
# ======================================


@query_result_transform
class GeometrySchema(QueryResult[Geometry]):
    type: GeometryTypeEnum
    attributes: RectangleAttributes | PolygonAttributes | LinesAttributes | EllipseAttributes
    scale_factor: float
    rotation: float
    nulled: bool

@query_result_transform
class GeometricHistoryPointSchema(QueryResult[GeometricHistoryPoint]):
    geometry: GeometrySchema
    time: datetime | None

@query_result_transform
class GeometricHistorySchema(QueryResult[GeometricHistory]):
    geometries: list[GeometricHistoryPointSchema]