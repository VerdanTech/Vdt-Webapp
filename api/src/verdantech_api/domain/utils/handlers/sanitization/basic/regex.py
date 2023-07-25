import re
from typing import Pattern

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class RegexSanitizationError(SanitizationError):
    pass


class RegexSanitizationConfig(SanitizationConfig[Pattern]):
    pass


class RegexSanitization(Sanitization):
    """Regex pattern sanitization functionality"""

    name = "RegexPattern"
    error: Exception = RegexSanitizationError

    def _base_sanitization(self, input: str) -> bool:
        if not re.match(self.validate_against, input):
            return False
        else:
            return True
