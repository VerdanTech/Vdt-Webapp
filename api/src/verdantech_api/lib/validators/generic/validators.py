import inspect
from numbers import Real
from typing import Any, Callable, Dict, List, Pattern, Type, TypeVar, Union

from .errors import ValidationError
from .validations import (
    BannedInputValidation,
    MaxLengthValidation,
    MaxSizeValidation,
    MinLengthValidation,
    MinSizeValidation,
    RegexValidation,
    Validation,
    ValidationConfig,
)

GenericInputType = TypeVar("GenericInputType")


class FieldValidator:
    """Generic class for implementing validations. Can be combined
    with ValidationMixins for base behavior."""

    field_name: str = "generic_field"
    field_type: Type = Type

    def __init__(
        self,
        min_size_validation: MinSizeValidation = None,
        max_size_validation: MaxSizeValidation = None,
        min_length_validation: MinLengthValidation = None,
        max_length_validation: MaxLengthValidation = None,
        regex_validation: RegexValidation = None,
        banned_input_validation: BannedInputValidation = None,
    ):
        """Sets all Validations requested"""
        self.validations: List[Validation] = []
        if min_size_validation:
            self.validations.append(min_size_validation)
        if max_size_validation:
            self.validations.append(max_size_validation)
        if min_length_validation:
            self.validations.append(min_length_validation)
        if max_length_validation:
            self.validations.append(max_length_validation)
        if regex_validation:
            self.validations.append(regex_validation)
        if banned_input_validation:
            self.validations.append(banned_input_validation)

    def _get_base_validation_methods(
        self,
    ) -> List[Callable[[Dict[str, str]], Dict[str, str]]]:
        """Returns a callable validation function for every
            Validation class

        Returns:
            List[Callable]: a list of validation methods
        """
        return [validator.base_validation for validator in self.validations]

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
        for validation_method in self._get_base_validation_methods():
            try:
                validation_method(input=input)
            except ValidationError as error_raised:
                error[type(error_raised).__name__] = error_raised.message

        return error

    def validate(self, input: GenericInputType) -> bool:
        # Group exceptions
        error = self._validate(input=input)

        # Custom validation logic

        # Raise errors
        if error:
            raise ValidationError(message=error)
        return True

    def normalize(self, input: GenericInputType) -> GenericInputType:
        """Convert input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """
        return input
