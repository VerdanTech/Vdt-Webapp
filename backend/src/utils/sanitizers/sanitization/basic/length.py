from typing import TypedDict

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class LengthSanitizationSpec(TypedDict):
    min: int
    max: int


class LengthSanitizationConfig(SanitizationConfig[LengthSanitizationSpec]):
    pass


class LengthSanitizationError(SanitizationError):
    pass


class LengthSanitization(Sanitization):
    """Length sanitization functionality"""

    name = "Length"
    error: Exception = LengthSanitizationError

    def _base_sanitization(self, input: str) -> bool:
        length = len(input)
        if length < self.spec["min"] or length > self.spec["max"]:
            return False
        else:
            return True
