# VerdanTech Source
from src.attributes.domain import Attribute, AttributeProfile, AttributeProfileSet
from src.common.domain import (
    Entity,
    Ref,
    RootEntity,
    root_entity_transform,
    value_transform,
)
from src.garden.domain import Garden
from src.user.domain import User

type CultivarCollectionParentType = Garden | User
"""CultivarCollections can be linked to either a User or a Garden."""


@root_entity_transform
class Cultivar(Entity):
    name: str
    abbreviation: str
    parent_name: str
    attributes: CultivarAttributeCluster = CultivarAttributeCluster()
    enabled: bool = True


@root_entity_transform
class CultivarCollection[Parent: CultivarCollectionParentType](RootEntity):
    parent_ref: Ref[Parent] | None
    key: str
    name: str
    description: str | None
    cultivar: set[Cultivar]
