"""
Domain modelling seeks to represent the problem domain in code with as much
resemblance as possible to the understanding of the users of the application.

For introduction to domain modelling, see this video: 
(https://www.youtube.com/watch?v=UEtmOW8uZZY&ab_channel=AmichaiMantinband)

For information on how domain modelling fits into software architecture see this book:
(https://github.com/cosmicpython/book)
"""

# Standard Library
import uuid
from datetime import datetime
from typing import Self, Union, dataclass_transform

# External Libraries
from attr import attrib
from attrs import define, evolve, field
from pydantic import BaseModel, ConfigDict

from .exceptions import EntityIntegrityException

type EntityIdType = uuid.UUID
type DomainModel = Union[RootEntity, Entity, Value]


class Command(BaseModel):
    """
    Represents a job the system may perform.

    Pydantic is used for a feature complete validation system
    for incoming inputs.
    """

    model_config = ConfigDict(frozen=True)


class Event:
    """
    Represents something that happened in the system.
    """

    pass


@dataclass_transform(field_specifiers=(attrib, field))
def event_transform(cls):
    """
    "Event" object settings. Used as a decorator.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies attrs @define decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        frozen=True: Immutability. If the object is to be modified
            it must return a modified version of itself
            (for example, by using evolve()).
        eq=True: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.
        slots=True: slotted classes are user for simple
            and easy performance gains.

    Args:
        cls (Type[Any]): the class before decoration.

    Returns:
        Type[ValueT]: the Value class after decoration.
    """
    cls = define(kw_only=True, frozen=True, eq=True, slots=True)(cls)
    return cls


class Entity:
    """
    "Entity" style domain model settings.

    An Entity is a domain model which is defined by by an identifier
    field, and thus represents an instance of something. Two entities
    are equal if they share the same ID.
    """

    id: EntityIdType | None = None
    """Not included in __init__ as the ID is assigned at persistence."""
    created_at: datetime = field(factory=datetime.now, init=False)
    """Not included in __init__ as the timestamp is assigned with a factory."""

    def __eq__(self, other) -> bool:
        """Two entities are equivalent if they share the same ID."""
        return self.id == other.id

    @property
    def persisted(self) -> bool:
        """If an ID has not been assigned, the entity has not been persisted."""
        return self.id is not None

    def id_or_error(self) -> EntityIdType:
        """
        Returns the id of the Entity.

        Raises:
            EntityIntegrityException: raised if the id
                attribute is None, which occurs
                before it is persisted for the first time.

        Returns:
            EntityIdType: the id of the Entity.
        """
        if self.id is None:
            raise EntityIntegrityException(
                "Unpersisted entity used in unexpected location."
            )
        else:
            return self.id

    def assert_persisted(self) -> None:
        """Raise an integrity exception if the entity is used in a location it should be persisted."""
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

    events: list[Event] = field(factory=list)

    @property
    def ref(self) -> "Ref[Self]":
        """
        Get a reference to self.

        Returns:
            Ref[RootEntity]: the reference to the RootEntity.
        """
        return Ref(id=self.id_or_error())


class Value:
    """
    "Value Object" style domain model settings.

    A Value is a domain model that is defined by its attributes
    and has no identifier field. They are also immutable.
    """

    def transform(self, **kwargs):
        """Wraps the attrs.evolve() function for transforming immutable value objects."""
        return evolve(self, **kwargs)


@dataclass_transform(field_specifiers=(attrib, field))
def entity_transform(cls):
    """
    "Entity" style domain model settings. Used as a decorator.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies attrs @define decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        eq=False: Explicit disabling of __eq__() generation as this
            is handled by Id equivalence.
        slots=False: Slotted classes are preferred for performance,
            but is currently not supported by SQLAlchemy. To make use
            of SQLAlchemy's imperative mapper and avoid clunky
            mapping between domain and ORM objects, they are currently disabled.
    """
    cls = define(kw_only=True, eq=False, slots=False)(cls)
    return cls


@dataclass_transform(field_specifiers=(attrib, field))
def root_entity_transform(cls):
    """
    "Root Entity / Aggregate Root" style domain model settings.
    Used as a decorator. Currently no different than the plain entity.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies @entity_transform decorator.
    """
    cls = entity_transform(cls)
    return cls


@dataclass_transform(field_specifiers=(attrib, field))
def value_transform(cls):
    """
    "Value Object" style domain model settings. Used as a decorator.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies attrs @define decorator with arguments:
        kw_only=True: Positional arguments are not supported
            for the sake of simplicity and readability.
        frozen=False: Value objects are supposed to be immutable,
            so use of frozen=True is preferred to enforce this.
            However, due to lack of support from SQLAlchemy,
            this is currently disabled.
        eq=True: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.
        slots=False: Slotted classes are preferred for performance,
            but is currently not supported by SQLAlchemy. To make use
            of SQLAlchemy's imperative mapper and avoid clunky
            mapping between domain and ORM objects, they are currently disabled.

    Args:
        cls (Type[Any]): the class before decoration.

    Returns:
        Type[ValueT]: the Value class after decoration.
    """

    cls = define(kw_only=True, frozen=False, eq=True, slots=False)(cls)
    return cls


@value_transform
class Ref[E: RootEntity](Value):
    """
    Entities and Values can hold references to other aggregates, but
    only by referencing RootEntitys by ID.
    """

    id: EntityIdType
