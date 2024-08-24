# VerdanTech Source
from src.common.domain import Command, value_transform, Value
from src.common.adapters.utils.spec_manager import merge_spec_collections

from .frost_date_planting_windows import (
    FrostDatePlantingWindowProfile,
    FrostDatePlantingWindowProfileUpdateCommand, frost_date_planting_window_specs
)
from .lifecycle import LifecycleProfile
from .origin import OriginProfile

specs = merge_spec_collections("cultivar", [frost_date_planting_window_specs])

@value_transform
class CultivarAttributeProfileSet(Value):
    """
    Acts as a container for sets of CultivarAttributeProfiles.
    """

    lifecycle: LifecycleProfile | None= None
    origin: OriginProfile | None= None
    frost_date_planting_windows: FrostDatePlantingWindowProfile | None= None


class CultivarAttributeUpdateCommand(Command):
    frost_date_planting_windows: FrostDatePlantingWindowProfileUpdateCommand | None= None
