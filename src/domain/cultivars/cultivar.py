# VerdanTech Source
from src.domain.common import RootEntity, root_entity_transform

from .attributes import CultivarAttributeCluster


@root_entity_transform
class Cultivar(RootEntity):
    name: str
    abbreviation: str | None
    parent_name: str
    attributes: CultivarAttributeCluster = CultivarAttributeCluster()
    enabled: bool = True
