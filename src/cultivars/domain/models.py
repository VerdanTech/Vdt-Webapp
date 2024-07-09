# VerdanTech Source
from src.common.domain import DomainModel, Ref, RootEntity, root_entity_transform
from src.garden.domain import Garden
from src.user.domain import User

from .attributes import CultivarAttributeCluster

type CultivarCollectionFriendType = Garden | User

"""CultivarCollections can be linked to either a User or a Garden."""


@root_entity_transform
class Cultivar(RootEntity):
    name: str
    abbreviation: str | None
    parent_name: str
    attributes: CultivarAttributeCluster = CultivarAttributeCluster()
    enabled: bool = True


@root_entity_transform
class CultivarCollection[Friend: DomainModel](RootEntity):
    friend_ref: Ref[CultivarCollectionFriendType] | None
    name: str
    description: str | None
    cultivar_refs: set[Ref[Cultivar]]
