# Standard Library
from datetime import date

# VerdanTech Source
from src.domain.common import Value, value_dataclass


class EnvironmentAttributeProfile(Value):
    pass


@value_dataclass
class FrostDateProfile(EnvironmentAttributeProfile):
    first_frost_date: date
    last_frost_date: date
