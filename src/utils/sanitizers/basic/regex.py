# Standard Library
import re
from typing import Pattern

from ..options import SelectEnum
from ..spec import Spec, SpecConfig, SpecError, SpecParams


class RegexSpecParams(SpecParams):
    pattern: Pattern


class RegexSpecConfig(SpecConfig[RegexSpecParams]):
    pass


class RegexSpecError(SpecError):
    pass


class RegexSpec(Spec):
    """Regex pattern sanitization functionality"""

    id = SelectEnum.REGEX
    name = "RegexSpec"
    error = RegexSpecError

    def _sanitize(self, input_data: str) -> bool:
        """
        Reject the input if does not match the regex pattern
        configured in self.config.params

        Args:
            input_data (str): the input string to validate.

        Returns:
            bool: validation result.
        """
        if not re.match(self.config.params["pattern"], input_data):
            return False
        else:
            return True
