# Standard Library
from typing import Union

# VerdanTech Source
from src.domain.environment.attributes import FrostDateProfile, GeoCoordinateProfile
from src.common.ops.common import schema


@schema
class EnvironmentAttributeClusterInput:
    profiles: list[Union[FrostDateProfile, GeoCoordinateProfile]]
