# Standard Library
import uuid

# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import (
    Entity,
    Ref,
    RootEntity,
    entity_transform,
    root_entity_transform,
)
from src.garden.domain import Garden
from src.user.domain import User

from .attributes import CultivarAttributeSet


@entity_transform
class Cultivar(Entity):
    name: str  # type: ignore
    key: str  # type: ignore
    attributes: CultivarAttributeSet = CultivarAttributeSet()
    description: str = ""
    parent_id: uuid.UUID | None = None


@root_entity_transform
class CultivarCollection(RootEntity):
    name: str  # type: ignore
    slug: str  # type: ignore
    _cultivars: set[Cultivar] = field(factory=set)
    description: str = ""
    tags: set[str] = field(factory=set)
    parent_ref: Ref["CultivarCollection"] | None = None

    """if there is a user ref, they is treated as the creator. 
    When a user adds a cultivar collection to a garden, both the
    garden and user are are added. The user is treated as creator
     of the collection, but only admins in the garden can modify or delete it.
       """
    user_ref: Ref[User] | None = None
    garden_ref: Ref[Garden] | None = None

    @property
    def cultivars(self) -> set[Cultivar]:
        return self._cultivars
