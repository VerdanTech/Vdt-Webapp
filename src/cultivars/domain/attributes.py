# Standard Library
from enum import Enum

# VerdanTech Source
from src.attributes.domain import AttributeCluster, AttributeProfile
from src.common.domain import value_transform
from src.plants.domain import OriginEnum

from .cultivar import Cultivar


class CultivarAttributeProfilesEnum(Enum):
    LIFE_CYCLE = "life_cycle_profile"
    FROST_DATE_PLANTING_WINDOWS = "frost_date_planting_windows"


class CultivarAttributeProfile(AttributeProfile[Cultivar]):
    """Base class for attribute profiles which pertain to plant type (cultivar) characteristics."""

    id: CultivarAttributeProfilesEnum


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
            first and last harvest of a plant. Zero for plants which only
            have one harvest.
        last_harvest_to_expiry (float): the expected amount of days between the
            last harvest of a plant and the end of its life. Zero for plants which
            expire at the time of their first or last harvest.
        years_of_life (int): the amount of years a plant is expected to live.
            Equal to 1 for annuals.
    """

    id = CultivarAttributeProfilesEnum.LIFE_CYCLE

    sow_to_germ: float
    germ_to_sprout: float
    germ_to_transplant: float
    sprout_to_first_harvest: float
    first_to_last_harvest: float
    # Or end of season!
    last_harvest_to_expiry: float
    years_of_life: int


@value_transform
class FrostDatePlantingWindowProfile(CultivarAttributeProfile):
    """
    Defines two static windows that a Cultivar is able to be planted outside,
    relative to the last and first frost dates.

    Attributes:
        last_frost_window_open (float): The amount of days between the last frost
            and the beginning of the planting window.
        last_frost_window_close (float): The amount of days between the last frost
            and the ending of the planting window.
        first_frost_window_open (float): The amount of days between the first frost
            and the beginning of the planting window.
        first_frost_window_close (float): The amount of days between the frist frost
            and the ending of the planting window.
    """

    id = CultivarAttributeProfilesEnum.FROST_DATE_PLANTING_WINDOWS

    last_frost_window_open: float
    last_frost_window_close: float
    first_frost_window_open: float
    first_frost_window_close: float


@value_transform
class AllowedOriginsProfile(CultivarAttributeProfile):
    """
    Defines the set of values of OriginEnum a plant of this cultivar is allowed to take.

    Attributes:
        allowed_origins: set[OriginEnum]: the values of OriginEnum that are allowed.
    """

    allowed_origins: set[OriginEnum]


@value_transform
class CultivarAttributeCluster(AttributeCluster[CultivarAttributeProfile]):
    """Acts as a container for a set of CultivarAttributeProfile."""

    life_cycle_profile: LifecycleProfile | None = None
    frost_date_planting_window_profile: FrostDatePlantingWindowProfile | None = None
    allowed_origins_profile: AllowedOriginsProfile | None = None
