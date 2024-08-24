# Standard Library
from typing import Literal

# VerdanTech Source
from src.common.domain import value_transform

from .profile import CultivarAttributeProfile


@value_transform
class LifecycleProfile(CultivarAttributeProfile):
    """
    Defines the expected length of time between sections of a plant's life.

    Attributes:
        sow_to_germ (float): the expected amount of days between the sowing
            and germination of a seed.
        germ_to_sprout (float): the expected amount of days between the germination
            of a seed and sprouting of a plant.
        sprout_to_first_harvest (float): the expected amount of days between the
            sprouting of a plant and its first harvest.
        first_to_last_harvest (float): the expected amount of days between the
            first and last harvest of a plant. None for plants which only
            have one harvest.
        last_harvest_to_expiry (float): the expected amount of days between the
            last harvest of a plant and the end of its life. None for plants which
            expire at the time of their first or last harvest. For plants
            which typically last until the end of their season, use Literal["Season"].
        years_of_life (int): the amount of years a plant is expected to live.
            Equal to 1 for annuals.
    """

    id = "lifecycle"
    label = "Lifecycle Profile"

    sow_to_germ: float | None = None
    germ_to_sprout: float | None = None
    germ_to_transplant: float | None = None
    sprout_to_first_harvest: float | None = None
    first_to_last_harvest: float | None = None
    last_harvest_to_expiry: float | Literal["Season"] | None = None
    years_of_life: int | None = None
