# Standard Library
from typing import Union

# VerdanTech Source
from src.common.interfaces.events.message import schema
from src.environment.domain.attributes import FrostDateProfile, GeoCoordinateProfile


@schema
class EnvironmentAttributeClusterInput:
    profiles: list[Union[FrostDateProfile, GeoCoordinateProfile]]
