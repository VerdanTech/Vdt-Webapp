# VerdanTech Source
from src.attributes.domain import AttributeProfile, AttributeProfileSet
from src.common.domain import Command, value_transform

from .frost_date_planting_windows import (
    FrostDatePlantingWindowProfile,
    FrostDatePlantingWindowProfileUpdateCommand,
)
from .lifecycle import LifecycleProfile
from .origin import OriginProfile

type CultivarAttributeProfile = AttributeProfile


@value_transform
class CultivarAttributeProfileSet(AttributeProfileSet[CultivarAttributeProfile]):
    """Acts as a container for a set of CultivarProfile."""

    lifecycle: LifecycleProfile | None
    origin: OriginProfile | None
    frost_date_planting_windows: FrostDatePlantingWindowProfile | None


class CultivarAttributeProfileSetUpdateCommand(Command):
    frost_date_planting_windows: FrostDatePlantingWindowProfileUpdateCommand | None
