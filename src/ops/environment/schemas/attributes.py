# Standard Library
from typing import Union

# VerdanTech Source
from src.domain.environment.attributes import FrostDateProfile, GeoCoordinateProfile
from src.ops.common import schema_dataclass


@schema_dataclass
class EnvironmentAttributeClusterInput:
    profiles: list[Union[FrostDateProfile, GeoCoordinateProfile]]
