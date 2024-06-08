# VerdanTech Source
from src.common.domain import Ref, RootEntity, root_entity_transform
from src.domain.environment import Environment
from src.domain.geometry import Geometry

from .location import LocationHistory


@root_entity_transform
class PlantingArea(RootEntity):
    geometry: Geometry
    location_history: LocationHistory = LocationHistory()
    movable: bool = False
    environment_ref: Ref[Environment] | None = None
