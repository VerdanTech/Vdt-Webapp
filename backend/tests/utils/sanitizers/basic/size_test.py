# Standard Library
from numbers import Real

# External Libraries
import pytest

# VerdanTech Source
from src.utils.sanitizers.basic.size import SizeSpec, SizeSpecConfig, SizeSpecParams

pytestmark = [pytest.mark.unit]


class TestSizeSpec:
    # ======================================
    # SizeSpec._sanitize() tests
    # ======================================

    @pytest.mark.parametrize(
        ["input_data", "params", "expected_output"],
        [
            # Test case: int size == min_size returns true
            (1, SizeSpecParams(min=1, max=10), True),
            # Test case: int size < min_size returns false
            (0, SizeSpecParams(min=1, max=10), False),
            # Test case: float size == min_size returns true
            (0.01, SizeSpecParams(min=0.01, max=10), True),
            # Test case: float size < min_size returns false
            (0.005, SizeSpecParams(min=0.01, max=10), False),
            # Test case: int size == max_size returns true
            (1, SizeSpecParams(min=0, max=1), True),
            # Test case: int size > max_size returns false
            (2, SizeSpecParams(min=0, max=1), False),
            # Test case: float size == max_size returns true
            (0.01, SizeSpecParams(min=0, max=0.01), True),
            # Test case: float size > max_size returns false
            (0.05, SizeSpecParams(min=0, max=0.01), False),
        ],
    )
    def test_size_spec(
        self, input_data: Real, params: SizeSpecParams, expected_output: bool
    ):
        """
        Ensure the inner sanitization logic rejects inputs with sizes
        less than params.min or greater than params.max.

        Args:
            input_data (Real): the input to test validation on.
            params (LengthSpecParams): the min and max values
                to use for validation.
            expected_output (bool): the expected result of the validation.
        """
        config = SizeSpecConfig(params=params, error_message="")
        spec = SizeSpec(config=config)
        assert spec._sanitize(input_data=input_data) == expected_output
