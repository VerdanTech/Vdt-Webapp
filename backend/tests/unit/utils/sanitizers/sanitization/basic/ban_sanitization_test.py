from numbers import Real
from typing import List, Union

import pytest
from src.utils.sanitizers.sanitization.basic.ban import (
    BanSanitization,
    BanSanitizationConfig,
)

pytestmark = [pytest.mark.unit]


class TestBanSanitization:
    @pytest.mark.parametrize(
        [
            "input",
            "spec",
            "expected_output",
            "case_sensitive",
        ],
        [
            # Test case: float not in banned_inputs returns true
            (0.5, [0.1, 0.2, 0.3], True, None),
            # Test case: float in banned_inputs returns false
            (0.5, [0.1, 0.2, 0.5], False, None),
            # Test case: str not in banned_inputs returns true
            ("str", ["str1", "str2"], True, None),
            # Test case: str in banned_inputs returns false
            ("str", ["str1", "str"], False, None),
            # Test case: str in banned_inputs
            # with case_sensitive = True
            # returns True
            ("sTr", ["str"], True, True),
            # Test case: str in normalized(banned_inputs)
            # with case_sensitive = False
            # returns false
            ("sTr", ["str"], False, False),
        ],
    )
    def test_banned_input_base_validation(
        self,
        input: Real | str,
        spec: List[Real] | List[str],
        expected_output: bool,
        case_sensitive: Union[bool, None],
    ):
        """Ensure the base sanitization logic works as expected

        Args:
            input (Real): the input to test validation on
            spec (List[Real] | List[str]): the list of ints or
                strings to blacklist
            expected_output (bool): the expected result of the validation
            case_sensitve (bool): whether to be sensitive to cases
                in comparison between input and spec
        """
        sanitization = BanSanitization(
            BanSanitizationConfig(
                spec=spec,
                error_message="",
                extra={"case_sensitive": case_sensitive},
            )
        )
        assert sanitization._base_sanitization(input=input) == expected_output
