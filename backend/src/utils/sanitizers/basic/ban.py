# Standard Library
from dataclasses import dataclass
from numbers import Real
from typing import List

from ..options import SelectEnum
from ..spec import Spec, SpecConfig, SpecError, SpecParams


class BanSpecParams(SpecParams):
    banned_inputs: List[Real] | List[str]


@dataclass(kw_only=True)
class BanSpecConfig(SpecConfig[BanSpecParams]):
    case_sensitive: bool


class BanSpecError(SpecError):
    pass


class BanSpec(Spec):
    """Banned input sanitization functionality"""

    id = SelectEnum.BAN
    name = "BanSpec"
    error = BanSpecError

    def _sanitize(self, input_data: Real | str) -> bool:
        """
        Reject the input if is contained within the banned list.
        Adjust the banned list depending on the configured value of
        case_sensitive and whether the input is a string.

        Args:
            input_data (Real | str): the input real number or string to validate.

        Returns:
            bool: validation result.
        """
        if not self.config.case_sensitive and isinstance(input_data, str):
            input_data = input_data.lower()
            self.config.params["banned_inputs"] = [
                banned_input.lower()
                for banned_input in self.config.params["banned_inputs"]
            ]
        if input_data in self.config.params["banned_inputs"]:
            return False
        else:
            return True
