# Standard Library
from typing import Any

# VerdanTech Source
from src.common.domain import Value


class Attribute[ValueT: Any](Value):
    label: str
    description: str
    value: ValueT


class AttributeProfile(Value):
    """
    Represents a generic group of attributes.

    Attributes:
        label (str): the user-facing string label.
        description (str): the user facing description.
    """

    label: str
    description: str


class AttributeProfileSet[ProfileT: AttributeProfile](Value):
    """
    Acts as a container for a set of attribute profiles.
    """

    pass
