# Standard Library
from typing import dataclass_transform

# External Libraries
from attr import attrib
from attrs import define, field


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
