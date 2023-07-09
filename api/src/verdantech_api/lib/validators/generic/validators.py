import inspect
from numbers import Real
from typing import Callable, Dict, List, Pattern, TypeVar, Union

from .errors import ValidationError
from .validations import (
    BannedInputValidation,
    MaxLengthValidation,
    MaxSizeValidation,
    MinLengthValidation,
    MinSizeValidation,
    RegexValidation,
)

GenericInputType = TypeVar("GenericInputType")


class FieldValidator:
    """Generic class for implementing validations. Can be combined
    with ValidationMixins for base behavior."""

    field_name: str = "generic_field"

    def __init__(self):
        """Must set all variables required by ValidationMixins"""

    def _get_base_validations(self) -> List[Callable[[Dict[str, str]], Dict[str, str]]]:
        """Returns a callable validation function for every
            Validation class

        Returns:
            List[Callable]: a list of validation methods
        """
        validation_classes = inspect.getmembers(
            self.__class__, predicate=(inspect.isclass)
        )
        return [
            validation_class[1].base_validation
            for validation_class in validation_classes
            if validation_class[0].endswith("Validation")
        ]

    def _validate(self, input: GenericInputType) -> Dict[str, str]:
        """Validates the input against base validation logis

        Args:
            input (GenericInputType): The input to validate

        Returns:
            Dict[str, str]: Dict containing errors
        """

        # Group exceptions
        error = {}

        # Base validation logic here
        for validation_method in self._get_base_validations():
            error = validation_method(error)

        return error

    def validate(self, input: GenericInputType) -> bool:
        # Group exceptions
        error = self._validate(input=input)

        # Custom validation logic

        # Raise errors
        if error:
            raise ValidationError(error)
        return True

    def normalize(self, input: GenericInputType) -> GenericInputType:
        """Convert input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """
        return input


class NumberFieldValidator(
    FieldValidator,
):
    field_name = "generic_number_field"

    min_size_validation: Union[MinSizeValidation, None] = None
    max_size_validation: Union[MinSizeValidation, None] = None
    banned_input_validation: Union[MinSizeValidation, None] = None

    def __init__(
        self,
        min_size: int = None,
        min_size_message: str = "Requires minimum {validate_against}",
        max_size: int = None,
        max_size_message: str = "Allows maximum {validate_against}",
        banned_inputs: List[Real] = [],
        banned_input_message: str = "Input not allowed",
    ):
        if min_size:
            self.min_size_validation = MinSizeValidation(
                validate_against=min_size, error_message=min_size_message
            )
        if max_size:
            self.max_size_validation = MaxSizeValidation(
                validate_against=max_size, error_message=max_size_message
            )
        if banned_inputs:
            self.banned_input_validation = BannedInputValidation(
                validate_against=banned_inputs, error_message=banned_input_message
            )


class StringFieldValidator(
    FieldValidator,
):
    field_name = "generic_string_field"

    min_length_validation: Union[MinLengthValidation, None] = None
    max_length_validation: Union[MaxLengthValidation, None] = None
    regex_validation: Union[RegexValidation, None] = None
    banned_input_validation: Union[BannedInputValidation, None] = None

    def __init__(
        self,
        min_length: int = None,
        min_length_message: str = "Requires minimum {validate_against} characters",
        max_length: int = None,
        max_length_message: str = "Allows minimum {validate_against} characters",
        regex: Pattern = None,
        regex_message: str = "Must fit pattern: {validate_against}",
        banned_inputs: List[str] = None,
        banned_input_message: str = "Input not allowed",
        normalize_banned_input_validation: bool = False,
    ):
        if min_length:
            self.min_length_validation = MinLengthValidation(
                validate_against=min_length, error_message=min_length_message
            )
        if max_length:
            self.max_length_validation = MaxLengthValidation(
                validate_against=max_length, error_message=max_length_message
            )
        if regex:
            self.regex_validation = RegexValidation(
                validate_against=regex, error_message=regex_message
            )
        if banned_inputs:
            self.banned_input_validation = BannedInputValidation(
                validate_against=banned_inputs,
                error_message=banned_input_message,
                normalize_banned_input_validation=normalize_banned_input_validation,
            )
