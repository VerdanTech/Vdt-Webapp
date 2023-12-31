
from datetime import date
from src.domain.common import value_dataclass, Value

class EnvironmentAttributeProfile(Value):
    pass

@value_dataclass
class FrostDateProfile(EnvironmentAttributeProfile):
    first_frost_date: date
    last_frost_date: date