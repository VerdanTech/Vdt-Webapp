# Standard Library
from dataclasses import Field, dataclass, field
from datetime import datetime
from typing import dataclass_transform

"""
Domain modelling seeks to represent the problem domain in code with as much
resemblance as possible to the understanding of the users of the application.

For introduction to domain modelling, see this video: 
(https://www.youtube.com/watch?v=UEtmOW8uZZY&ab_channel=AmichaiMantinband)

For information on how domain modelling fits into software architecture see this book:
(https://github.com/cosmicpython/book)
"""


type EntityIdType = int
"""
EntityIdType is the only part of the domain dependent on persistence, because
the database is responsible for assigning primary keys. Currently, incrementing
integer primary keys are used.
"""


class Entity:
    """
    "Entity" style domain model settings.

    An Entity is a domain model which is defined by by an identifier
    field, and thus represents an instance of something. Two entities
    are equal if they share the same ID.
    """

    id: EntityIdType | None = None
    """Not included in __init__ as the ID is assigned at persistence."""
    created_at: datetime | None = None
    """Not included in __init__ as the timestamp is assigned at persistence."""

    def __eq__(self, other) -> bool:
        return self.id == other.id


class RootEntity(Entity):
    """
    "Root Entity / Aggregate Root" style domain model settings.

    A RootEntity is a domain model which is any Entity that
    defines a transactional boundary and thus the largest objects
    responsible for maintaining invariants. There is one Repository
    for each RootEntity.
    """

    pass


class Value:
    """
    "Value Object" style domain model settings.

    A Value is a domain model that is defined by its attributes
    and has no identifier field. They are also immutable.
    """

    pass


@dataclass_transform(field_specifiers=(Field, field))
def entity_dataclass(cls):
    """
    "Entity" style domain model dataclass settings. Used as a decorator.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies dataclass decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        eq=False: Explicit disabling of __eq__() generation as this
            is handled by Id equivalence.
    """
    dataclass_settings = {"kw_only": True, "eq": False}
    cls = dataclass(**dataclass_settings)(cls)
    return cls


@dataclass_transform(field_specifiers=(Field, field))
def root_entity_dataclass(cls):
    """
    "Root Entity / Aggregate Root" style domain model dataclass settings.
    Used as a decorator. Currently no different than the plain entity.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies @entity_dataclass decorator.
    """
    cls = entity_dataclass(cls)
    return cls


@dataclass_transform(field_specifiers=(Field, field))
def value_dataclass(cls):
    """
    "Value Object" style domain model dataclass settings. Used as a decorator.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies dataclass decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        frozen=True: Immutability. If the object is to be modified
            it must return a modified version of itself
            (for example, by using replace())
        eq=False: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.

    Args:
        cls (Type[Any]): the class before decoration.

    Returns:
        Type[ValueT]: the Value class after decoration.
    """

    dataclass_settings = {"kw_only": True, "frozen": True, "eq": True}
    cls = dataclass(**dataclass_settings)(cls)
    return cls


@value_dataclass
class Ref[RootEntity](Value):
    """
    Entities and Values can hold references to other aggregates, but
    only by referencing RootEntitys by ID.
    """

    id: EntityIdType

    def __init__(self, id: EntityIdType) -> None:
        self.id = id
