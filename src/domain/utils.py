# Standard Library
from datetime import datetime

# VerdanTech Source
from src.domain.common import Value, value_transform


@value_transform
class TimeWindow(Value):
    """
    Represents a single window of time through two dates.

    If either date is None, it indicates that the end and/or
    beginning of the window failed to resolve.
    """

    start_date: datetime | None
    end_date: datetime | None
