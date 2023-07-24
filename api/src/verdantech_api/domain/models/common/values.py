from dataclasses import dataclass


@dataclass(frozen=True)
class Value:
    """Base value object for all domain value objects"""

    pass


class Ref(Value):
    """Base class for inter-object reference, aka a
    container around an object ID"""

    _id: str
