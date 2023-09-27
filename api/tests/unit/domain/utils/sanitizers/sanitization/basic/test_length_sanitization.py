from numbers import Real

import pytest
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.length import (
    LengthSanitization,
    LengthSanitizationConfig,
    LengthSanitizationSpec,
)


class TestLengthSanitization:
    @pytest.mark.parametrize(
        ["input", "spec", "expected_output"],
        [
            # Test case: len(str) == min_length returns true
            ("str", LengthSanitizationSpec(min=3, max=10), True),
            # Test case: len(str) < min_length returns false
            ("st", LengthSanitizationSpec(min=3, max=10), False),
        ],
    )
    def test_min_length_base_sanitization(
        self, input: Real, spec: LengthSanitizationSpec, expected_output: bool
    ):
        """Ensure the base sanitization logic works as expected

        Args:
            input (Real): the input
            spec (LengthSanitizationSpec): the min and max values
                to use for validation
            expected_output (bool): the expected result of the validation
        """
        sanitization = LengthSanitization(
            LengthSanitizationConfig(spec=spec, error_message="")
        )
        assert sanitization._base_sanitization(input=input) == expected_output

    @pytest.mark.parametrize(
        ["input", "spec", "expected_output"],
        [
            # Test case: len(str) == max_length returns true
            ("str", LengthSanitizationSpec(min=0, max=3), True),
            # Test case: len(str) > max_length returns false
            ("str", LengthSanitizationSpec(min=0, max=2), False),
        ],
    )
    def test_max_length_base_sanitization(
        self, input: Real, spec: LengthSanitizationSpec, expected_output: bool
    ):
        """Ensure the base sanitization logic works as expected

        Args:
            input (Real): the input
            spec (LengthSanitizationSpec): the min and max values
                to use for validation
            expected_output (bool): the expected result of the validation
        """
        sanitization = LengthSanitization(
            LengthSanitizationConfig(spec=spec, error_message="")
        )
        assert sanitization._base_sanitization(input=input) == expected_output
