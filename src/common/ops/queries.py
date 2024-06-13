# Standard Library
from typing import dataclass_transform

# External Libraries
from attr import attrib, define, field

# VerdanTech Source
from src.common.domain.models import DomainModel


@dataclass_transform(field_specifiers=(attrib, field))
def query_transform(cls):
    """
    Attrs settings for API Data Transfer requests.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies attrs @define decorator with arguments:
        frozen=True: Immutability is enforced for read-only constructs.
        eq=True: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.
        slots=True: Slotted classes are preferred for performance.
    """

    cls = define(frozen=True, eq=True, slots=True)(cls)
    return cls


@dataclass_transform(field_specifiers=(attrib, field))
def query_result_transform(cls):
    """
    Attrs settings for API Data Transfer Objects.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies attrs @define decorator with arguments:
        frozen=True: Immutability is enforced for read-only constructs.
        eq=True: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.
        slots=True: Slotted classes are preferred for performance.
    """

    cls = define(frozen=True, eq=True, slots=True)(cls)
    return cls


class Query:
    pass


class QueryResult[T: DomainModel]:
    pass
