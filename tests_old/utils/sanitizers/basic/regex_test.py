# Standard Library
import re

# External Libraries
import pytest

# VerdanTech Source
from src.utils.sanitizers.basic.regex import RegexSpec, RegexSpecConfig, RegexSpecParams

pytestmark = [pytest.mark.unit]


class TestRegexSpec:
    # ======================================
    # RegexSpec._sanitize() tests
    # ======================================

    @pytest.mark.parametrize(
        ["input_data", "pattern", "expected_output"],
        [
            # Test case: String matches the pattern
            ("abc123", r"^[a-z]+\d+$", True),
            # Test case: String does not match the pattern (no digits)
            ("abcdef", r"^[a-z]+\d+$", False),
            # Test case: String matches the pattern (empty string)
            ("", r"^$", True),
            # Test case: String does not match the pattern (non-empty string)
            ("nonempty", r"^$", False),
            # Test case: String matches a more complex pattern
            ("hello@world.com", r"^\w+@\w+\.\w+$", True),
            # Test case: String does not match the complex pattern (missing domain)
            ("hello@", r"^\w+@\w+\.\w+$", False),
        ],
    )
    def test_regex_spec(self, input_data: str, pattern: str, expected_output: bool):
        """
        Ensure that the regex sanitization logic works as expected.

        Args:
            input_string (str): the string to test against the regex pattern.
            pattern (str): the regex pattern to use for validation.
            expected_output (bool): the expected result of the validation.
        """
        compiled_pattern = re.compile(pattern)
        params = RegexSpecParams(pattern=compiled_pattern)
        config = RegexSpecConfig(params=params, error_message="")
        regex_spec = RegexSpec(config=config)
        assert regex_spec._sanitize(input_data=input_data) == expected_output
