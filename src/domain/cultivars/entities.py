# Standard Library
from typing import List

# VerdanTech Source
from src.domain.attributes.common import AttributeCluster
from src.domain.common import (
    DomainModel,
    Entity,
    EntityIdType,
    Ref,
    RootEntity,
    entity_dataclass,
    root_entity_dataclass,
)


@entity_dataclass
class Cultivar(Entity):
    name: str
    abbreviation: str
    parent_ref: Ref["Cultivar"]
    attributes: set[AttributeCluster]
    enabled: bool = True


@root_entity_dataclass
class Varset[Friend: DomainModel](RootEntity):
    friend: Ref[Friend]
    name: str
    cultivars: list[Cultivar]


class GlobalVarsetStore(RootEntity):
    pass
