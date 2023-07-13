from numbers import Real
from typing import Any, ContextManager, Dict, Type, Union

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.lib.validators.generic.errors import ValidationError
from src.verdantech_api.lib.validators.generic.validations import (
    BannedInputValidation,
    MaxLengthValidation,
    MaxSizeValidation,
    MinLengthValidation,
    MinSizeValidation,
    RegexValidation,
    Validation,
    ValidationConfig,
)


class TestBaseValidation:
    @pytest.mark.parametrize(
        [
            "validation_result",
            "validation_against",
            "error_message",
            "expected_error_message",
            "error_context",
        ],
        [
            # Test case: The validation is true,
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
                {"GenericValidation": "minimum"},
                ValidationError,
            ),
            # Test case: The validation is false,
            # and error is raised with error message, f
            # formatted with validate_against
            (
                False,
                0,
                "minimum {validate_against}",
                {"GenericValidation": "minimum 0"},
                ValidationError,
            ),
        ],
        indirect=["error_context"],
    )
    def test_base_validation(
        self,
        validation_result: bool,
        validation_against: Any,
        error_message: str,
        expected_error_message: str,
        error_context: ContextManager,
        base_validation: Validation,
        mocker: MockerFixture,
    ):
        """Ensure the base_validation function validates,
            and raises error with error message

        Args:
            validation_result (bool): the mock result of self._base_validation
            validation_against (Any): parameter to use for validation
            error_message (str): the message to be appended onto the error dict
            expected_error_message (str): expected error message raised
            error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
            base_validation (Validation): provider of a Validation class to test on
            mocker (MockerFixture): pytest-mock
        """
        validation_mock = mocker.patch(
            "src.verdantech_api.lib.validators.generic.validations.Validation._base_validation",
            return_value=validation_result,
        )
        base_validation.validate_against = validation_against
        base_validation.error_message = error_message

        with error_context as error:
            base_validation.base_validation(input=0)
            validation_mock.assert_called_once()
            if error is not None:
                assert error.message == expected_error_message


class TestGenericValidations:
    @pytest.mark.parametrize(
        ["input", "validate_against", "expected_output"],
        [
            # Test case: int size == min_size returns true
            (1, 1, True),
            # Test case: int size < min_size returns false
            (0, 1, False),
            # Test case: float size == min_size returns true
            (0.01, 0.01, True),
            # Test case: float size < min_size returns false
            (0.005, 0.01, False),
        ],
    )
    def test_min_size_base_validation(
        self, input: Real, validate_against: Real, expected_output: bool
    ):
        """Ensure the base validation logic works as expected

        Args:
            input (Real): the input
            validate_against (Real): the value of the parameter to
                use for validation
            expected_output (bool): the expected result of the validation
        """
        validation = MinSizeValidation(
            ValidationConfig(validate_against=validate_against, error_message="")
        )
        assert validation._base_validation(input=input) == expected_output

    @pytest.mark.parametrize(
        ["input", "validate_against", "expected_output"],
        [
            # Test case: int size == max_size returns true
            (1, 1, True),
            # Test case: int size > max_size returns false
            (1, 0, False),
            # Test case: float size == max_size returns true
            (0.01, 0.01, True),
            # Test case: float size > max_size returns false
            (0.01, 0.005, False),
        ],
    )
    def test_max_size_base_validation(
        self, input: Real, validate_against: Real, expected_output: bool
    ):
        """Ensure the base validation logic works as expected

        Args:
            input (Real): the input
            validate_against (Real): the value of the parameter to
                use for validation
            expected_output (bool): the expected result of the validation
        """
        validation = MaxSizeValidation(
            ValidationConfig(validate_against=validate_against, error_message="")
        )
        assert validation._base_validation(input=input) == expected_output

    @pytest.mark.parametrize(
        ["input", "validate_against", "expected_output"],
        [
            # Test case: len(str) == min_length returns true
            ("str", 3, True),
            # Test case: len(str) < min_length returns false
            ("st", 3, False),
        ],
    )
    def test_min_length_base_validation(
        self, input: Real, validate_against: Real, expected_output: bool
    ):
        """Ensure the base validation logic works as expected

        Args:
            input (Real): the input
            validate_against (Real): the value of the parameter to
                use for validation
            expected_output (bool): the expected result of the validation
        """
        validation = MinLengthValidation(
            ValidationConfig(validate_against=validate_against, error_message="")
        )
        assert validation._base_validation(input=input) == expected_output

    @pytest.mark.parametrize(
        ["input", "validate_against", "expected_output"],
        [
            # Test case: len(str) == max_length returns true
            ("str", 3, True),
            # Test case: len(str) > max_length returns false
            ("str", 2, False),
        ],
    )
    def test_max_length_base_validation(
        self, input: Real, validate_against: Real, expected_output: bool
    ):
        """Ensure the base validation logic works as expected

        Args:
            input (Real): the input
            validate_against (Real): the value of the parameter to
                use for validation
            expected_output (bool): the expected result of the validation
        """
        validation = MaxLengthValidation(
            ValidationConfig(validate_against=validate_against, error_message="")
        )
        assert validation._base_validation(input=input) == expected_output

    @pytest.mark.parametrize(["validation_result"], [(True,), (False,)])
    def test_regex_base_validation(
        self, validation_result: bool, mocker: MockerFixture
    ):
        """Ensure the base validation logic correctly calls re.match

        Args:
            validation_result (bool): the result of re.match to test
            mocker (MockerFixture): pytest-mock
        """
        re_match_mock = mocker.patch(
            "src.verdantech_api.lib.validators.generic.validations.re.match",
            return_value=validation_result,
        )
        validation = RegexValidation(
            ValidationConfig(validate_against="regex", error_message="error_message")
        )

        assert validation._base_validation(input="input") == validation_result
        re_match_mock.assert_called_once_with("regex", "input")

    @pytest.mark.parametrize(
        [
            "input",
            "validate_against",
            "expected_output",
            "normalize_banned_input_validation",
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
            # with normalize_banned_input_validation = False
            # returns True
            ("sTr", ["str"], True, False),
            # Test case: str in normalized(banned_inputs)
            # with normalize_banned_input_validation = True
            # returns false
            ("sTr", ["str"], False, True),
        ],
    )
    def test_banned_input_base_validation(
        self,
        input: Real,
        validate_against: Real,
        expected_output: bool,
        normalize_banned_input_validation: Union[bool, None],
    ):
        """Ensure the base validation logic works as expected

        Args:
            input (Real): the input
            validate_against (Real): the value of the parameter to
                use for validation
            expected_output (bool): the expected result of the validation
            normalize_banned_input_validation (bool): whether to normalize
                strings before comparison with banned_inputs
        """
        validation = BannedInputValidation(
            ValidationConfig(
                validate_against=validate_against,
                error_message="",
                extra={
                    "normalize_banned_input_validation": normalize_banned_input_validation
                },
            )
        )
        assert validation._base_validation(input=input) == expected_output
