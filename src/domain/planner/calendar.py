# Standard Library
from datetime import date, datetime
from enum import Enum

# VerdanTech Source
from src.domain.common import Ref, Value, value_transform
from src.domain.cultivars import Cultivar
from src.domain.environment import Environment
from src.domain.utils import TimeWindow


@value_transform
class PlantingWindow(Value):
    """
    Represents a set of TimeWindows that pertain to a specific
    Cultivar in a specific Environment, over a given time scope.
    """

    cultivar_ref: Ref[Cultivar]
    environment_ref: Ref[Environment]
    time_windows: set[TimeWindow]
    scope: TimeWindow


@value_transform
class PlantingCalendar(Value):
    planting_windows: set[PlantingWindow]
    scope: TimeWindow
