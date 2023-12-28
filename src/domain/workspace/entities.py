# VerdanTech Source
from src.domain.common import (
    Entity,
    RootEntity,
    entity_dataclass,
    root_entity_dataclass,
)


@root_entity_dataclass
class Workspace(RootEntity):
    pass


@entity_dataclass
class PlantingArea(Entity):
    pass
