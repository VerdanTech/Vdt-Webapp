# External Libraries
import pytest

# VerdanTech Source
from src.utils.sanitizers.basic.length import (
    LengthSpec,
    LengthSpecConfig,
    LengthSpecParams,
)

pytestmark = [pytest.mark.unit]


class TestLengthSpec:
    # ======================================
    # LengthSpec._sanitize() tests
    # ======================================

    @pytest.mark.parametrize(
        ["input_data", "params", "expected_output"],
        [
            # Test case: len(str) == min_length returns true
            ("str", LengthSpecParams(min=3, max=10), True),
            # Test case: len(str) < min_length returns false
            ("st", LengthSpecParams(min=3, max=10), False),
            # Test case: len(str) == max_length returns true
            ("str", LengthSpecParams(min=0, max=3), True),
            # Test case: len(str) > max_length returns false
            ("str", LengthSpecParams(min=0, max=2), False),
        ],
    )
    def test_length_spec(
        self, input_data: str, params: LengthSpecParams, expected_output: bool
    ):
        """
        Ensure the inner sanitization logic rejects inputs with lengths
        less than params.min or greater than params.max.

        Args:
            input_data (Real): the input to test validation on.
            params (LengthSpecParams): the min and max values
                to use for validation.
            expected_output (bool): the expected result of the validation.
        """
        config = LengthSpecConfig(params=params, error_message="")
        spec = LengthSpec(config=config)
        assert spec._sanitize(input_data=input_data) == expected_output
