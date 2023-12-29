# VerdanTech Source
from src.domain.common import RootEntity, root_entity_dataclass


@root_entity_dataclass
class PlantSchema(RootEntity):
    pass


@root_entity_dataclass
class PlantInstance(RootEntity):
    pass
