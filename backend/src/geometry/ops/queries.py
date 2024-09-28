# VerdanTech Source
from src.common.ops.queries import QueryResult, query_result_transform
from src.geometry.domain import (
    Coordinate,
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
    position: Coordinate
    attributes: PolygonAttributes | LinesAttributes | EllipseAttributes
