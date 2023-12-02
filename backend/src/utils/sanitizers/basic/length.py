from ..options import SelectEnum
from ..spec import Spec, SpecConfig, SpecError, SpecParams


class LengthSpecParams(SpecParams):
    min: int
    max: int


class LengthSpecConfig(SpecConfig[LengthSpecParams]):
    pass


class LengthSpecError(SpecError):
    pass


class LengthSpec(Spec):
    """Length sanitization functionality"""

    id = SelectEnum.LENGTH
    name = "LengthSpec"
    error = LengthSpecError

    def _sanitize(self, input_data: str) -> bool:
        """
        Reject the input if its length is outside the bounds configured
        in self.config.params.

        Args:
            input_data (Real): the input string to validate.

        Returns:
            bool: validation result.
        """
        length = len(input_data)
        if length < self.config.params["min"] or length > self.config.params["max"]:
            return False
        else:
            return True
