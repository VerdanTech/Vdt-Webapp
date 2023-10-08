from dataclasses import dataclass


class Value:
    """Base value object for all domain value objects"""

    @classmethod
    def __init_subclass__(cls) -> None:
        dataclass(kw_only=True, frozen=True)(cls)


class Ref(Value):
    """Base class for inter-object reference, aka a
    container around an object ID"""

    id: str
