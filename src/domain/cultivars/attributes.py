# Standard Library
from datetime import date, timedelta

# VerdanTech Source
from src.domain.attributes import AttributeCluster
from src.domain.common import DomainModel, Value, value_dataclass
from src.domain.cultivars.entities import Cultivar
from src.domain.garden.garden import Garden


class CultivarAttributeCluster(AttributeCluster[Cultivar]):
    """Base class for attribute clusters which pertain to Cultivars"""

    pass


@value_dataclass
class LifecycleProfile(CultivarAttributeCluster):
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

    sow_to_germ: float
    germ_to_sprout: float
    sprout_to_first_harvest: float
    first_to_last_harvest: float
    last_harvest_to_expiry: float
    years_of_life: int


@value_dataclass
class FrostDatePlantingWindows(CultivarAttributeCluster):
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

    last_frost_window_open: float
    last_frost_window_close: float
    first_frost_window_open: float
    first_frost_window_close: float
