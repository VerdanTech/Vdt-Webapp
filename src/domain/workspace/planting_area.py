# VerdanTech Source
from src.domain.common import Entity, entity_dataclass

from .geometry import Geometry


class PlantingArea(Entity):
    geometry: Geometry


@entity_dataclass
class SoilContainer(PlantingArea):
    pass


@entity_dataclass
class SeedStartingContainer(PlantingArea):
    pass
