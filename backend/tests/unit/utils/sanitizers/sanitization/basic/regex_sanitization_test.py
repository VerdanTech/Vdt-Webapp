import pytest
from pytest_mock import MockerFixture
from src.utils.sanitizers.sanitization.basic.regex import (
    RegexSanitization,
    RegexSanitizationConfig,
)

pytestmark = [pytest.mark.unit]


class TestRegexSanitization:
    @pytest.mark.parametrize(["sanitization_result"], [(True,), (False,)])
    def test_regex_base_sanitization(
        self, sanitization_result: bool, mocker: MockerFixture
    ):
        """Ensure the base sanitization logic correctly calls re.match

        Args:
            sanitization_result (bool): the result of re.match to test
            mocker (MockerFixture): pytest-mock
        """
        re_match_mock = mocker.patch(
            "src.utils.sanitizers.sanitization.basic.regex.re.match",
            return_value=sanitization_result,
        )
        regex = "regex"
        input = "input"
        sanitization = RegexSanitization(
            RegexSanitizationConfig(spec=regex, error_message="")
        )

        assert sanitization._base_sanitization(input=input) == sanitization_result
        re_match_mock.assert_called_once_with(regex, input)
