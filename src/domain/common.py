# Standard Library
from dataclasses import dataclass, field, fields
from datetime import datetime
from typing import Annotated, Any, Generic, Optional, Type, TypeVar

"""
For introduction to domain modelling, see this video: 
(https://www.youtube.com/watch?v=UEtmOW8uZZY&ab_channel=AmichaiMantinband)
"""

EntityT = TypeVar("EntityT")
RootEntityT = TypeVar("RootEntityT")
ValueT = TypeVar("ValueT")

EntityIDType = TypeVar("EntityIDType")


def entity(cls: Type[Any]) -> Type[EntityT]:
    """
    "Entity" style domain model settings. Used as a decorator.

    An Entity is a domain model which is defined by by an identifier
    field, and thus represents an instance of something. Two entities
    are equal if they share the same ID.

    This decorator:
    - Creates an id attribute if one does not already exist.
    - Creates an __eq__() method to compare Entity's by their id attribute.
    - Creates a created_at attribute to record the initial time of
        domain model instantiation.
    - Applies dataclass decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        eq=False: Explicit disabling of __eq__() generation.

    Args:
        cls (Type[Any]): the class before decoration.

    Returns:
        Type[EntityT]: the Entity class after decoration.
    """
    # Create an id attribute if it doesn't exist.
    if not hasattr(cls, "id"):
        # ID is optional, because IDs are only set once persisted.
        # Not included in __init__ as that takes place before first persistence.
        cls.id = field(default=None, init=False)
        # Set the type annotation so dataclasses can recognize type.
        # TODO: As manually modifying the __annotations__ dict
        # is bad practice, investigate if this can be done a better way
        # without requiring a base class.
        cls.__annotations__["id"] = Optional[EntityIDType]

    # Create a created_at attribute if it doesn't exist.
    if not hasattr(cls, "created_at"):
        # Set at object instantiation. Not included in __init__.
        cls.created_at: datetime = field(default_factory=datetime.now, init=False)
        # Set the type annotation so dataclasses can recognize type.
        # TODO: As manually modifying the __annotations__ dict
        # is bad practice, investigate if this can be done a better way
        # without requiring a base class.
        cls.__annotations__["created_at"] = datetime

    # Set the comparison function to compare by ID.
    if not hasattr(cls, "__eq__"):

        def __eq__(self: EntityT, other: EntityT) -> bool:
            return self.id == other.id

        setattr(cls, "__eq__", __eq__)

    dataclass_settings = {"kw_only": True}
    cls = dataclass(**dataclass_settings)(cls)
    return cls


def root_entity(cls: Type[EntityT]) -> Type[RootEntityT]:
    """
    "Root Entity / Aggregate Root" style domain model settings.
    Used as a decorator.

    A RootEntity is a domain model which is any Entity that
    defines a transactional boundary and thus the largest objects
    responsible for maintaining invariants. There is one Repository
    for each RootEntity.

    This decorator:
    - Applies @entity decorator.

    Args:
        cls (Type[EntityT]): the Entity class before decoration.

    Returns:
        Type[RootEntityT]: the RootEntity class after decoration.
    """
    cls = entity(cls)
    return cls


def value(cls: Type[Any]) -> Type[ValueT]:
    """
    "Value Object" style domain model settings. Used as a decorator.

    A Value is a domain model that is defined by its attributes
    and has no identifier field. They are also immutable.

    This decorator:
    - Applies dataclass decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        frozen=True: Immutability. If the object is to be modified
            it must return a modified version of itself
            (for example, by using replace())

    Args:
        cls (Type[Any]): the class before decoration.

    Returns:
        Type[ValueT]: the Value class after decoration.
    """

    dataclass_settings = {"kw_only": True, "frozen": True}
    cls = dataclass(**dataclass_settings)(cls)
    return cls


@value
class Ref(Generic[RootEntityT]):
    """
    Entities and Values can only hold references to RootEntitys by ID.
    """

    id: EntityIDType = field(init=True)
