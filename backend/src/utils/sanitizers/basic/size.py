# Standard Library
from numbers import Real

from ..options import SelectEnum
from ..spec import Spec, SpecConfig, SpecError, SpecParams


class SizeSpecParams(SpecParams):
    min: int
    max: int


class SizeSpecConfig(SpecConfig[SizeSpecParams]):
    pass


class SizeSpecError(SpecError):
    pass


class SizeSpec(Spec):
    """Size sanitization functionality"""

    id = SelectEnum.SIZE
    name = "SizeSpec"
    error = SizeSpecError

    def _sanitize(self, input_data: Real) -> bool:
        """
        Reject the input if its size is outside the bounds configured
        in self.config.params.

        Args:
            input_data (Real): the input real number to validate.

        Returns:
            bool: validation result.
        """
        if (
            input_data < self.config.params["min"]
            or input_data > self.config.params["max"]
        ):
            return False
        else:
            return True
