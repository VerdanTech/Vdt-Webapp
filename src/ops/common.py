# Standard Library
from dataclasses import Field, dataclass, field
from typing import dataclass_transform


@dataclass_transform(field_specifiers=(Field, field))
def schema_dataclass(cls):
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
