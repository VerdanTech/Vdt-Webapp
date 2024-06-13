# Standard Library
from enum import Enum


class OriginEnum(Enum):
    """Describes the process by which a plant is brought into being."""

    DIRECT_SEED = "direct seed"
    """A seed is sown directly into the area it will reach maturity in."""
    SEED_TRANSPLANT = "seed transplant"
    """A seed is sown in one area and then transplanted into the area it will reach maturity in."""
    SEEDLING_TO_TRANSPLANT = "seelding transplant"
    """A seedling is transplanted directly into the area it will reach maturity in."""
