# VerdanTech Source
from src.domain.common import DomainModel, Ref, RootEntity, root_entity_transform
from src.domain.garden import Garden
from src.domain.user import User

from .cultivar import Cultivar

type CultivarCollectionFriendType = Garden | User
"""CultivarCollections can be linked to either a User or a Garden."""


@root_entity_transform
class CultivarCollection[Friend: DomainModel](RootEntity):
    friend_ref: Ref[CultivarCollectionFriendType] | None
    name: str
    description: str | None
    cultivar_refs: set[Ref[Cultivar]]
