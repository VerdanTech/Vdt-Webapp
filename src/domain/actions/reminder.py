# Standard Library
from datetime import datetime

# VerdanTech Source
from src.domain.common import Value, value_transform


@value_transform
class Reminder(Value):
    time: datetime
    title: str
    description: str | None = None
