# VerdanTech Source
from src.common.domain import Ref, RootEntity, root_entity_transform
from src.common.domain.geometry import Geometry
from src.environment.domain import Environment

from .location import LocationHistory


@root_entity_transform
class PlantingArea(RootEntity):
    geometry: Geometry
    location_history: LocationHistory = LocationHistory()
    movable: bool = False
    environment_ref: Ref[Environment] | None = None
