# Standard Library
import uuid
from dataclasses import Field, dataclass, field
from typing import dataclass_transform

# VerdanTech Source
from src.domain.common import Ref, RootEntity


@dataclass_transform(field_specifiers=(Field, field))
def schema(cls):
    """
    Data transfer schema dataclass settings. Used as a decorator.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies dataclass decorator with arguments:
        eq=True: Explicit enabling of __eq__() generation.
        slots=True: slotted classes are user for simple
            and easy performance gains.
    """
    dataclass_settings = {"eq": True, "slots": True}
    cls = dataclass(**dataclass_settings)(cls)
    return cls


@schema
class RefSchema[E: RootEntity]:
    id: uuid.UUID
    """
    UUID class is used directly as the the ASGI framework in use
    (Litestar) currently cannot type it correctly when using the EntityIdType alias.
    """

    @classmethod
    def from_model(cls, ref: Ref[E]) -> "RefSchema[E]":
        return cls(id=ref.id)
