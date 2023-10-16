from numbers import Real
from typing import List

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class BanSanitizationConfig(SanitizationConfig[List[Real] | List[str]]):
    pass


class BanSanitizationError(SanitizationError):
    pass


class BanSanitization(Sanitization):
    """Banned input sanitization functionality"""

    name = "Ban"
    error: Exception = BanSanitizationError

    def _base_sanitization(self, input: Real | str) -> bool:
        if not self.extra["case_sensitive"] and isinstance(input, str):
            input = input.lower()
            self.spec = [banned_input.lower() for banned_input in self.spec]
        if input in self.spec:
            return False
        else:
            return True
