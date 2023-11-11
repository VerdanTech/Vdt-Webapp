from numbers import Real

import pytest
from src.utils.sanitizers.sanitization.basic.size import (
    SizeSanitization,
    SizeSanitizationConfig,
    SizeSanitizationSpec,
)

pytestmark = [pytest.mark.unit]


class TestSizeSanitization:
    @pytest.mark.parametrize(
        ["input", "spec", "expected_output"],
        [
            # Test case: int size == min_size returns true
            (1, SizeSanitizationSpec(min=1, max=10), True),
            # Test case: int size < min_size returns false
            (0, SizeSanitizationSpec(min=1, max=10), False),
            # Test case: float size == min_size returns true
            (0.01, SizeSanitizationSpec(min=0.01, max=10), True),
            # Test case: float size < min_size returns false
            (0.005, SizeSanitizationSpec(min=0.01, max=10), False),
        ],
    )
    def test_min_size_base_sanitization(
        self, input: Real, spec: SizeSanitizationConfig, expected_output: bool
    ):
        """Ensure the base sanitization logic works as expected

        Args:
            input (Real): the input
            spec (SizeSanitizationSpec): the min and max values
                to use for validation
            expected_output (bool): the expected result of the sanitization
        """
        sanitization = SizeSanitization(
            SizeSanitizationConfig(spec=spec, error_message="")
        )
        assert sanitization._base_sanitization(input=input) == expected_output

    @pytest.mark.parametrize(
        ["input", "spec", "expected_output"],
        [
            # Test case: int size == max_size returns true
            (1, SizeSanitizationSpec(min=0, max=1), True),
            # Test case: int size > max_size returns false
            (2, SizeSanitizationSpec(min=0, max=1), False),
            # Test case: float size == max_size returns true
            (0.01, SizeSanitizationSpec(min=0, max=0.01), True),
            # Test case: float size > max_size returns false
            (0.05, SizeSanitizationSpec(min=0, max=0.01), False),
        ],
    )
    def test_max_size_base_sanitization(
        self, input: Real, spec: SizeSanitizationSpec, expected_output: bool
    ):
        """Ensure the base sanitization logic works as expected

        Args:
            input (Real): the input to test validation on
            spec (SizeSanitizationSpec): the min and max values
                to use for validation
            expected_output (bool): the expected result of the validation
        """
        sanitization = SizeSanitization(
            SizeSanitizationConfig(spec=spec, error_message="")
        )
        assert sanitization._base_sanitization(input=input) == expected_output
