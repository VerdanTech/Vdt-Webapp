from typing import ContextManager, Dict, List, Union

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.lib.validators.generic.errors import (
    MaxSizeValidationError,
    MinSizeValidationError,
    ValidationError,
)
from src.verdantech_api.lib.validators.generic.validations import Validation
from src.verdantech_api.lib.validators.generic.validators import FieldValidator


class TestGenericFieldValidator:
    def test__init__(
        self,
        mock_validations: List[Validation],
        mocker: MockerFixture,
    ):
        """Ensure that the constructor of FieldValidator adds
            all validations that are passed to it

        Args:
            mock_validations [List[Validation]: fixture providing mock
                instances of all Validation classes to test on
        """

        field_validator = FieldValidator(*mock_validations)

        assert len(field_validator.validations) == len(mock_validations)

    def test_get__base_validations(
        self, field_validator: FieldValidator, mocker: MockerFixture
    ):
        """Ensure that the _base_validation function returns the
            base validation methods from the validations

        Args:
            field_validator (FieldValidator): fixture providing
                a FieldValidator filled with mock Validations
        """

        base_validation_methods = field_validator._get_base_validation_methods()

        assert len(base_validation_methods) == len(field_validator.validations)

    @pytest.mark.parametrize(
        ["errors_raised", "expected_error_message"],
        [
            # Test case: no errors raised, and no output error dict
            ([None], {}),
            # Test case: one error raised, and error dict reflects
            ([ValidationError(message="error")], {"ValidationError": "error"}),
            # Test case: multiple errors raised, and error dict reflects
            (
                [
                    MinSizeValidationError(message="error1"),
                    MaxSizeValidationError(message="error2"),
                ],
                {
                    "MinSizeValidationError": "error1",
                    "MaxSizeValidationError": "error2",
                },
            ),
        ],
    )
    def test__validate(
        self,
        errors_raised: Union[List[Exception], None],
        expected_error_message: Dict[str, str],
        field_validator: FieldValidator,
        mocker: MockerFixture,
    ):
        """Ensure that the _validate function constructs the output
            error dict given the exceptions correctly

        Args:
            errors_raised (List[Union[Exception, None]]): List of exceptions
                to mock raising, or None
            expected_error_message (Dict[str, str]): expected output
                error dict
            field_validator (FieldValidator): fixture providing
                a FieldValidator filled with mock Validations
            mocker (MockerFixture): pytest-mock
        """
        mocked_base_validation_methods = [
            mocker.MagicMock(side_effect=error) for error in errors_raised
        ]
        mocker.patch.object(
            field_validator,
            "_get_base_validation_methods",
            return_value=mocked_base_validation_methods,
        )

        error_message = field_validator._validate(input=0)

        assert error_message == expected_error_message

    @pytest.mark.parametrize(
        ["base_validation_error", "error_context", "expected_error_message"],
        [
            # Test case: no base validation error,
            # so no exception is called
            ({}, None, {}),
            # Test case: base validation error,
            # exception is called
            (
                {"ValidationError": "message"},
                ValidationError,
                {"ValidationError": "message"},
            ),
        ],
        indirect=["error_context"],
    )
    def test_validate(
        self,
        base_validation_error: Dict[str, str],
        error_context: ContextManager,
        expected_error_message: Dict[str, str],
        field_validator: FieldValidator,
        mocker: MockerFixture,
    ):
        """Ensure that the validate function calls base
            validation, and raises a validation error with
            the gathered errors

        Args:
            base_validation_error (Dict[str, str]): the mock result of
                _validate_
            error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
            expected_error_message (Dict[str, str]): the expected message passed
                into raised ValidationError
            field_validator (FieldValidator): fixture providing
                a FieldValidator filled with mock Validations
            mocker (MockerFixture): pytest-mock
        """
        _validate_mock = mocker.patch.object(
            field_validator, "_validate", return_value=base_validation_error
        )

        with error_context as error:
            field_validator.validate(input=0)
            _validate_mock.assert_called_once_with(input=0)
            if error is not None:
                assert error.message == expected_error_message
