# Standard Library
from enum import Enum


class OriginEnum(Enum):
    """Describes the process by which a plant is brought into being."""

    DIRECT_SEED = "direct seed"
    """A seed is sown directly into the area it will reach maturity in."""
    SEED_TRANSPLANT = "seed transplant"
    """A seed is sown in one area and then transplanted into the area it will reach maturity in."""
    SEEDLING_TO_TRANSPLANT = "seedling transplant"
    """A seedling is transplanted directly into the area it will reach maturity in."""


class CultivarCollectionVisibilityEnum(Enum):
    """
    Visibility controls the ability of a CultivarCollection
    to be read-accessed.

    Attributes:
        PRIVATE:
        UNLISTED:
        PUBLIC:
    """

    PRIVATE = "private"
    UNLISTED = "unlisted"
    PUBLIC = "public"
