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
    parent_id: uuid.UUID | None = None


@root_entity_transform
class CultivarCollection(RootEntity):
    name: str  # type: ignore
    slug: str  # type: ignore
    _cultivars: set[Cultivar] = field(factory=set)
    description: str | None = None
    tags: set[str] = field(factory=set)
    parent_ref: Ref["CultivarCollection"] | None = None
    user_ref: Ref[User] | None = None
    garden_ref: Ref[Garden] | None = None

    @property
    def cultivars(self) -> set[Cultivar]:
        return self._cultivars
