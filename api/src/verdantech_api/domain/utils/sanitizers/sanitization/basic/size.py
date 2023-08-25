from numbers import Real
from typing import TypedDict

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class SizeSanitizationSpec(TypedDict):
    min: int
    max: int


class SizeSanitizationConfig(SanitizationConfig[SizeSanitizationSpec]):
    pass


class SizeSanitizationError(SanitizationError):
    pass


class SizeSanitization(Sanitization):
    """Size sanitization functionality"""

    name = "Size"
    error: Exception = SizeSanitizationError

    def _base_sanitization(self, input: Real) -> bool:
        if input < self.spec["min"] or input > self.spec["max"]:
            return False
        else:
            return True
