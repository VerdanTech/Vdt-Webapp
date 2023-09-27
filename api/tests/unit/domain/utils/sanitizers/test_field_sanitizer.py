from typing import Any, ContextManager, Dict, List

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.domain.utils.sanitizers.field import FieldSanitizer
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.size import (
    SizeSanitizationError,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.generic import (
    SanitizationError,
)


class TestFieldSanitizer:
    def test__get_base_sanitization_methods(self, field_sanitizer: FieldSanitizer):
        """Ensure that the function returns all the
            base sanitization methods from the sanitizer

        Args:
            field_sanitizer (FieldSanitizer): fixture providing
                a FieldSanitizer filled with mock Sanitizations
        """
        base_sanitization_methods = field_sanitizer._get_base_sanitization_methods()
        assert len(base_sanitization_methods) == len(field_sanitizer.sanitizations)

    @pytest.mark.parametrize(
        ["errors_raised", "expected_error_message"],
        [
            # Test case: no errors raised, and no output error dict
            ([None], {}),
            # Test case: one error raised, and error dict reflects
            ([SanitizationError("error")], {"SanitizationError": "error"}),
            # Test case: multiple errors raised, and error dict reflects
            (
                [SizeSanitizationError("error1"), SanitizationError("error2"), None],
                {
                    "SizeSanitizationError": "error1",
                    "SanitizationError": "error2",
                },
            ),
        ],
    )
    async def test__sanitize(
        self,
        errors_raised: List[Exception | None],
        expected_error_message: Dict[str, str],
        field_sanitizer: FieldSanitizer,
        mocker: MockerFixture,
    ):
        """Ensure that the _sanitize function correctly constructs
            the output error dict given the exceptions

        Args:
            errors_raised (List[Exception | None]): List of
                exceptions to mock raising
            expected_error_message (Dict[str, str]): expected output
                error dict
            field_sanitizer (FieldSanitizer): fixture providing
                a FieldSanitizer filled with mock Sanitizations
            mocker (MockerFixture): pytest-mock
        """
        mocked_base_sanitization_methods = [
            mocker.MagicMock(side_effect=error) for error in errors_raised
        ]
        mocker.patch.object(
            field_sanitizer,
            "_get_base_sanitization_methods",
            return_value=mocked_base_sanitization_methods,
        )

        error_message = await field_sanitizer._sanitize(input=0)

        assert error_message == expected_error_message

    @pytest.mark.parametrize(
        [
            "base_sanitization_errors",
            "expected_error_context",
            "expected_error_message",
        ],
        [
            # Test case: no base validation error,
            # so no exception is called
            ({}, None, {}),
            # Test case: base validation error,
            # exception is called
            (
                {"SanitizationError": "message"},
                SanitizationError,
                {"SanitizationError": "message"},
            ),
        ],
        indirect=["expected_error_context"],
    )
    async def test_sanitize(
        self,
        base_sanitization_errors: Dict[str, str],
        expected_error_context: ContextManager,
        expected_error_message: Dict[str, str],
        field_sanitizer: FieldSanitizer,
        mocker: MockerFixture,
    ):
        """Ensure that the function calls base
            sanitization, and raises a sanitization error with
            the gathered errors

        Args:
            base_sanitization_errors (Dict[str, str]): the mock result of
                _sanitize
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            expected_error_message (Dict[str, str]): the expected message passed
                into raised ValidationError
            field_sanitizer (FieldSanitizer): fixture providing
                a FieldSanitizer filled with mock Sanitizations
            mocker (MockerFixture): pytest-mock
        """
        _sanitize_mock = mocker.patch.object(
            field_sanitizer, "_sanitize", return_value=base_sanitization_errors
        )

        with expected_error_context as error:
            await field_sanitizer.sanitize(input=0)
            _sanitize_mock.assert_called_once_with(input=0, disabled_sanitizations=None)
            if error is not None:
                assert error.str() == expected_error_message

    @pytest.mark.parametrize(
        ("normalized_input", "expected_output"),
        [("normalized_input", "normalized_input"), (None, None)],
    )
    def test_normalized(
        self,
        normalized_input: Any,
        expected_output: Any | None,
        field_sanitizer: FieldSanitizer,
    ):
        """Ensure the function returns None if the
        normalized input has not been supplied

        Args:
            normalized_input (Any): the normalized input set on the
                FieldSanitizer
            expected_output (Any | None): expected return of function
            field_sanitizer (FieldSanitizer): fixture providing
                a FieldSanitizer filled with mock Sanitizations
        """
        field_sanitizer.normalized_input = normalized_input
        assert field_sanitizer.normalized() == normalized_input
