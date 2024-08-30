# VerdanTech Source
from src.common.adapters.utils.spec_manager import merge_spec_collections
from src.common.domain import Command, Value, value_transform

from .annual_lifecycle import AnnualLifecycleProfile
from .frost_date_planting_windows import (
    FrostDatePlantingWindowProfile,
    FrostDatePlantingWindowProfileUpdateCommand,
    frost_date_planting_window_specs,
)
from .origin import OriginProfile, OriginProfileUpdateCommand, origin_specs

specs = merge_spec_collections(
    "cultivar", [frost_date_planting_window_specs, origin_specs]
)


@value_transform
class CultivarAttributeSet(Value):
    """
    Acts as a container for sets of CultivarAttributeProfiles.
    """

    frost_date_planting_window_profile: FrostDatePlantingWindowProfile | None = None
    origin_profile: OriginProfile | None = None


class CultivarAttributeUpdateCommand(Command):
    """
    Allows updating any possible cultivar attribute.
    """
    frost_date_planting_window_profile: FrostDatePlantingWindowProfileUpdateCommand | None = (
        None
    )
    origin_profile: OriginProfileUpdateCommand | None = None
