from __future__ import annotations

# Standard Library
from datetime import datetime, timedelta

# External Libraries
from attrs import field

from ..common import Value, value_transform


@value_transform
class BaseConfirmation(Value):
    """Base value object for verification through email"""

    key: str
    created_at: datetime = field(factory=datetime.now)

    def is_valid(self, expiry_time_hours: int) -> bool:
        """
        Computes whether the confirmation has expired.

        Args:
            expiry_time_hours (int): amount of hours before an email
                confirmation should expire, application setting.

        Returns:
            bool: false if not expired.
        """
        return not (datetime.now() - self.created_at) > timedelta(
            hours=expiry_time_hours
        )
