from datetime import datetime

from src.domain.common import value_transform, Value

@value_transform
class Reminder(Value):
    time: datetime
    title: str
    description: str | None = None