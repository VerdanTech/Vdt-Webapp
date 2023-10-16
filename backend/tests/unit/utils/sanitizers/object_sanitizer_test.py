from typing import Any, ContextManager, Dict, List

import pytest
from pytest_mock import MockerFixture
from src.utils.sanitizers.field import FieldSanitizer
from src.utils.sanitizers.object import ObjectSanitizer
from src.utils.sanitizers.sanitization.generic import (
    SanitizationError,
)


class TestObjectSanitizer:
    @pytest.mark.parametrize(
        ("field_name", "expected_error_context"),
        [
            ("int_field", None),
            ("nonexistent_field", ValueError),
        ],
        indirect=["expected_error_context"],
    )
    def test__get_field_sanitizer(
        self,
        field_name: str,
        expected_error_context: ContextManager,
        mock_entity_sanitizer: ObjectSanitizer,
    ):
        """Ensure that the function returns the sanitizer
        and raises an error if not found

        Args:
            field_name (str): the field name to try and get
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            mock_entity_sanitizer (ObjectSanitizer): an object sanitizer
                configured for the mock entity
        """
        with expected_error_context:
            field_sanitizer = mock_entity_sanitizer._get_field_sanitizer(
                field_name=field_name
            )
            assert field_sanitizer == mock_entity_sanitizer.config.get(field_name)

    @pytest.mark.parametrize(
        ("input", "normalized", "field_name", "expected_output"),
        [
            # Test case: normalized value is set on
            # correct field
            (
                {"str_field": "str", "int_field": 0},
                "STR",
                "str_field",
                {"str_field": "STR", "int_field": 0},
            ),
            # Test case: normalized value is not set
            (
                {"str_field": "str"},
                None,
                "str_field",
                {"str_field": "str"},
            ),
        ],
    )
    async def test__use_field_sanitizer(
        self,
        input: Dict[str, Any],
        normalized: Any,
        field_name: str,
        expected_output: Dict[str, Any],
        mock_entity_sanitizer: ObjectSanitizer,
        field_sanitizer: FieldSanitizer,
        mocker: MockerFixture,
    ):
        """Ensure that the function calls the field sanitization
            and sets the normalized input if it was set during the
            sanitization

        Args:
            input (Dict[str, Any]): input to test sanitization on
            normalized (Any): normalized value for sanitization to
                set on the field sanitizer
            field_name (str): name of the field to test sanitization on
            expected_output (Dict[str, Any]): the expected sanitized data
            mock_entity_sanitizer (ObjectSanitizer): an object sanitizer
                configured for the mock entity
            field_sanitizer (FieldSanitizer): fixture providing
                a FieldSanitizer filled with mock Sanitizations
            mocker (MockerFixture): pytest-mock
        """
        sanitized = input

        sanitize_mock = mocker.patch.object(
            field_sanitizer, "sanitize", return_value=True
        )
        normalized_mock = mocker.patch.object(
            field_sanitizer, "normalized", return_value=normalized
        )

        sanitized = await mock_entity_sanitizer._use_field_sanitizer(
            input=input,
            sanitized=sanitized,
            field_sanitizer=field_sanitizer,
            field_name=field_name,
        )

        sanitize_mock.assert_called_once_with(input=input, disabled_sanitizations=None)
        normalized_mock.assert_called_once()
        assert sanitized == expected_output

    @pytest.mark.parametrize(
        ("input", "sanitization_results", "expected_output", "expected_error"),
        [
            # Test case: all sanitization happens okay, no error raised
            (
                {"str_field": "str", "int_field": 0},
                [
                    {"str_field": "STR", "int_field": 0},
                    {"str_field": "STR", "int_field": 1},
                ],
                {"str_field": "STR", "int_field": 1},
                {},
            ),
            # Test case: errors occur and are added
            (
                {"str_field": "str", "int_field": 0},
                [
                    SanitizationError("error1"),
                    SanitizationError("error2"),
                ],
                {"str_field": "str", "int_field": 0},
                {"str_field": "error1", "int_field": "error2"},
            ),
        ],
    )
    async def test__sanitize(
        self,
        input: Dict[str, Any],
        sanitization_results: List[Dict[str, Any] | Exception],
        expected_output: Dict[str, Any],
        expected_error: Dict[str, str],
        mock_entity_sanitizer: ObjectSanitizer,
        mocker: MockerFixture,
    ):
        """Ensure that the function constructs the output error correctly

        Args:
            input (Dict[str, Any]): the input to test
            sanitization_results (List[Dict[str, Any] | Exception]):
                a list of output data or exceptions raised
                by the _use_field_sanitizer function
            expected_output (Dict[str, Any]): the expected output
                sanitized data of the function
            expected_error (Dict[str, str]): the expected output
                error message
            mock_entity_sanitizer (ObjectSanitizer): an object sanitizer
                configured for the mock entity
            mocker (MockerFixture): pytest-mock
        """
        _get_field_sanitizer_mock = mocker.patch.object(
            mock_entity_sanitizer, "_get_field_sanitizer"
        )
        _use_field_sanitizer_mock = mocker.patch.object(
            mock_entity_sanitizer,
            "_use_field_sanitizer",
            side_effect=sanitization_results,
        )

        sanitized, error = await mock_entity_sanitizer._sanitize(input=input)

        assert sanitized == expected_output
        assert error == expected_error

    @pytest.mark.parametrize(
        ("sanitized_result", "error_result", "expected_error_context"),
        [
            # Test case: no errer returned, and none raised
            ({"str_field": "str"}, {}, None),
            # Test case: error is returned and is raised as a SanitizationError
            ({"str_field": str}, {"str_field": "error"}, SanitizationError),
        ],
        indirect=["expected_error_context"],
    )
    async def test_sanitize(
        self,
        sanitized_result: Dict[str, Any],
        error_result: Dict[str, str],
        expected_error_context: ContextManager,
        mock_entity_sanitizer: ObjectSanitizer,
        mocker: MockerFixture,
    ):
        """Ensure that the function raises SanitizationError
            with the resultant grouped exception from _sanitize

        Args:
            sanitized_result (Dict[str, Any]): the mocked result
                of the sanitization
            error_result (Dict[str, str]): the mocked error result
                of the sanitizatoin
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            mock_entity_sanitizer (ObjectSanitizer): an object sanitizer
                configured for the mock entity
            mocker (MockerFixture): pytest-mock
        """
        _sanitite_mock = mocker.patch.object(
            mock_entity_sanitizer,
            "_sanitize",
            return_value=(sanitized_result, error_result),
        )

        with expected_error_context as error:
            sanitized = await mock_entity_sanitizer.sanitize(input={})
            _sanitite_mock.assert_called_once_with(input={}, disabled_fields=None)
            assert sanitized == sanitized_result
            if error is not None:
                assert error == error_result
