# Standard Library
import uuid
from dataclasses import Field, dataclass, field
from datetime import datetime
from typing import Union, dataclass_transform

from .exceptions import EntityIntegrityException

"""
Domain modelling seeks to represent the problem domain in code with as much
resemblance as possible to the understanding of the users of the application.

For introduction to domain modelling, see this video: 
(https://www.youtube.com/watch?v=UEtmOW8uZZY&ab_channel=AmichaiMantinband)

For information on how domain modelling fits into software architecture see this book:
(https://github.com/cosmicpython/book)
"""


type EntityIdType = uuid.UUID
type DomainModel = Union[RootEntity, Entity, Value]


class Entity:
    """
    "Entity" style domain model settings.

    An Entity is a domain model which is defined by by an identifier
    field, and thus represents an instance of something. Two entities
    are equal if they share the same ID.
    """

    id: EntityIdType = field(default_factory=uuid.uuid4, init=False)
    """Not included in __init__ as the ID is assigned with a factory."""
    created_at: datetime = field(default_factory=datetime.now, init=False)
    """Not included in __init__ as the timestamp is assigned with a factory."""
    persisted: bool = False

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def assert_persisted(self) -> None:
        if not self.persisted:
            raise EntityIntegrityException(
                "Unpersisted entity used in unexpected location."
            )


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
        slots=True: slotted classes are user for simple
            and easy performance gains.
    """
    dataclass_settings = {"kw_only": True, "eq": False, "slots": True}
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
        eq=True: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.
        slots=True: slotted classes are user for simple
            and easy performance gains.

    Args:
        cls (Type[Any]): the class before decoration.

    Returns:
        Type[ValueT]: the Value class after decoration.
    """

    dataclass_settings = {"kw_only": True, "frozen": True, "eq": True, "slots": True}
    cls = dataclass(**dataclass_settings)(cls)
    return cls


@value_dataclass
class Ref[E: RootEntity](Value):
    """
    Entities and Values can hold references to other aggregates, but
    only by referencing RootEntitys by ID.
    """

    id: uuid.UUID
    """
    UUID class is used directly as the Ref class is often used
    as a data transfer schema directly, and the ASGI framework in use
    (Litestar) currently cannot type it correctly when using the EntityIdType alias.
    """

    def to_schema(self):
        """
        When a domain model is to be used directly as a
        data transfer object, it must be ensured that the
        conversion is valid. This is is done by calling
        this function to use a domain model as a schema.
        """
        return self
