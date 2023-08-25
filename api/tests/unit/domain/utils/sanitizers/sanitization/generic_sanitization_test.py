from typing import Any, ContextManager

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.domain.utils.sanitizers.sanitization.generic import (
    Sanitization,
    SanitizationError,
)


class TestGenericSanitization:
    @pytest.mark.parametrize(
        [
            "sanitization_result",
            "spec",
            "error_message",
            "expected_error_message",
            "expected_error_context",
        ],
        [
            # Test case: The sanitization is true,
            # and nothing is raised
            (
                True,
                0,
                "",
                None,
                None,
            ),
            # Test case: The validation is false,
            # and error is raised with error message
            (
                False,
                0,
                "minimum",
                "minimum",
                SanitizationError,
            ),
            # Test case: The validation is false,
            # and error is raised with error message, f
            # formatted with validate_against
            (
                False,
                0,
                "minimum {spec}",
                {"GenericSanitization": "minimum 0"},
                SanitizationError,
            ),
        ],
        indirect=["expected_error_context"],
    )
    def test_generic_sanitization(
        self,
        sanitization_result: bool,
        spec: Any,
        error_message: str,
        expected_error_message: str,
        expected_error_context: ContextManager,
        sanitization: Sanitization,
        mocker: MockerFixture,
    ):
        """Ensure the base_sanitization function validates,
            and raises error with error message

        Args:
            sanitization_result (bool): the mock result of self._base_sanitization
            sanitization_against (Any): parameter to use for sanitization
            error_message (str): the message to be appended onto the error dict
            expected_error_message (str): expected error message raised
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            sanitization (Sanitization): provider of a Validation class to test on
            mocker (MockerFixture): pytest-mock
        """
        sanitization_mock = mocker.patch(
            "src.verdantech_api.domain.utils.sanitizers.sanitization.generic.Sanitization._base_sanitization",
            return_value=sanitization_result,
        )
        sanitization.spec = spec
        sanitization.error_message = error_message

        with expected_error_context as error:
            sanitization.base_sanitization(input=0)
            sanitization_mock.assert_called_once()
            if error is not None:
                assert error.message == expected_error_message
