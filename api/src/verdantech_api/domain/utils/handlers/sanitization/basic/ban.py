from typing import List, Real

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class BanSanitizationConfig(SanitizationConfig[List[Real] | List[str]]):
    pass


class BanSanitizationError(SanitizationError):
    pass


class BannedInputSanitization(Sanitization):
    """Banned input sanitization functionality"""

    name = "Ban"
    error: Exception = BanSanitizationError

    def _base_sanitization(self, input: Real | str) -> bool:
        if self.extra["normalize_banned_input_sanitization"] and isinstance(input, str):
            input = input.lower()
            self.spec = [banned_input.lower() for banned_input in self.validate_against]
        if input in self.validate_against:
            return False
        else:
            return True
