from dataclasses import dataclass
from typing import Optional, TypeVar

EntityT = TypeVar("EntityT", bound="Entity")
RootEntityT = TypeVar("RootEntityT", bound="RootEntity")

EntityIDType = str


class Entity:
    """Base entity class for all domain entity models"""

    _id: Optional[EntityIDType] = None

    @classmethod
    def __init_subclass__(cls):
        dataclass(kw_only=True)(cls)


class RootEntity(Entity):
    """Base class for entities which are aggregate roots"""

    pass


class MockEntity(Entity):
    """Simple entity class for tests"""

    int_field: int
    str_field: str
