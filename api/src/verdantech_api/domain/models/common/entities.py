from dataclasses import dataclass
from typing import Optional, TypeVar

EntityT = TypeVar("EntityT", bound="Entity")


@dataclass
class Entity:
    """Base entity class for all domain entity models"""

    _id: Optional[str] = None


class RootEntity(Entity):
    """Base class for entities which are aggregate roots"""

    pass
