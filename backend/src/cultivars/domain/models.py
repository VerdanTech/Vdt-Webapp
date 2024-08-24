# VerdanTech Source
import uuid
from src.common.domain import (
    Entity,
    Ref,
    RootEntity,
    root_entity_transform, entity_transform
)
from src.garden.domain import Garden
from src.user.domain import User
from .attributes import CultivarAttributeProfileSet
from attrs import field


@entity_transform
class Cultivar(Entity):
    name: str # type: ignore
    abbreviation: str # type: ignore
    attributes: CultivarAttributeProfileSet = CultivarAttributeProfileSet()
    parent_id: uuid.UUID | None = None


@root_entity_transform
class CultivarCollection(RootEntity):
    key: str # type: ignore
    name: str # type: ignore
    cultivars: set[Cultivar] = field(factory=set)
    description: str | None = None
    tags: set[str] = field(factory=set)
    parent_ref: Ref["CultivarCollection"] | None = None
    user_ref: Ref[User] | None = None
    garden_ref: Ref[Garden] | None = None
