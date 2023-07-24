from typing import Any, Callable, Dict, List, Pattern, Type, TypeVar, Union

from .errors import ValidationError
from .validations import Validation

GenericInputType = TypeVar("GenericInputType")


class FieldValidator:
    """Generic class for implementing validations. Can be combined
    with ValidationMixins for base behavior."""

    field_name: str = "generic_field"
    field_type: Type = Type

    def __init__(self, validations: List[Validation]):
        self.validations = validations

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
                error[self.field_name][
                    type(error_raised).__name__
                ] = error_raised.message

        return error

    def validate(self, input: GenericInputType) -> bool:
        # Group exceptions
        error = self._validate(input=input)

        # Custom validation logic

        # Raise errors
        if error:
            raise ValidationError(message=error)
        return True


class NormalizationMixin:
    def normalize(self, input: GenericInputType) -> GenericInputType:
        """Convert input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """
        return input


class MockFieldValidator:
    """Mock validator class for testing"""

    field_name: str = "generic_field"

    def validate(self, input: GenericInputType) -> bool:
        return True

    def normalize(self, input: GenericInputType) -> GenericInputType:
        return input
