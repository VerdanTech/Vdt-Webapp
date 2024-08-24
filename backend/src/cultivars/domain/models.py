# VerdanTech Source
from src.common.domain import (
    Entity,
    Ref,
    RootEntity,
    root_entity_transform, entity_transform
)
from src.garden.domain import Garden
from src.user.domain import User
from .attributes import CultivarAttributeProfileSet
type CultivarCollectionParentType = Garden | User
"""CultivarCollections can be linked to either a User or a Garden."""


@entity_transform
class Cultivar(Entity):
    name: str
    abbreviation: str
    parent_name: str
    attributes: CultivarAttributeProfileSet = CultivarAttributeProfileSet()
    enabled: bool = True


@root_entity_transform
class CultivarCollection[Parent: CultivarCollectionParentType](RootEntity):
    parent_ref: Ref[Parent] | None
    key: str
    name: str
    description: str | None
    cultivar: set[Cultivar]
