from abc import ABC, abstractmethod
from numbers import Real
from typing import Dict, List, Pattern, TypeVar

from .errors import ValidationError
from .validations import (
    BannedInputValidationMixin,
    MaxLengthValidationMixin,
    MaxSizeValidationMixin,
    MinLengthValidationMixin,
    MinSizeValidationMixin,
    RegexValidationMixin,
)

GenericInputType = TypeVar("GenericInputType")


class FieldValidator(ABC):
    """Generic class for implementing validations. Can be combined
    with ValidationMixins for base behavior."""

    field_name: str = "generic_field"

    @abstractmethod
    def __init__(self):
        """Must set all variables required by ValidationMixins"""

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
        for base in FieldValidator.__bases__:
            if hasattr(base, "base_validation"):
                base_validation_method = getattr(base, "base_validation")
                error = base_validation_method(self, input, error)

        return error

    def validate(self, input: GenericInputType) -> bool:
        # Group exceptions
        error = self._validate(input=input)

        # Custom validation logic

        # Raise errors
        if error:
            raise ValidationError(error)
        return True

    @abstractmethod
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
    MinSizeValidationMixin,
    MaxSizeValidationMixin,
    BannedInputValidationMixin,
):
    field_name = "generic_number_field"

    def __init__(
        self,
        min_size: int = None,
        max_size: int = None,
        blacklist: List[Real] = [],
        whitelist: List[Real] = [],
        min_size_message: str = "Requires minimum {message}",
        max_size_message: str = "Allows maximum {message}",
        banned_input_message: str = "Input not allowed",
    ):
        self.min_size = min_size
        self.max_size = max_size
        self.blacklist = blacklist
        self.whitelist = whitelist
        self.min_size_message = min_size_message
        self.max_size_message = max_size_message
        self.banned_input_message = banned_input_message


class StringFieldValidator(
    FieldValidator,
    MinLengthValidationMixin,
    MaxLengthValidationMixin,
    RegexValidationMixin,
    BannedInputValidationMixin,
):
    field_name = "generic_string_field"

    def __init__(
        self,
        min_length: int = None,
        max_length: int = None,
        regex: Pattern = None,
        blacklist: List[str] = [],
        whitelist: List[str] = [],
        min_length_message: str = "Requires minimum {message} characters",
        max_length_message: str = "Allows minimum {message} characters",
        regex_message: str = "Must fit pattern: {message}",
        banned_input_message: str = "Input not allowed",
    ):
        self.min_length = min_length
        self.max_length = max_length
        self.regex = regex
        self.blacklist = blacklist
        self.whitelist = whitelist
        self.min_length_message = min_length_message
        self.max_length_message = max_length_message
        self.regex_message = regex_message
        self.banned_input_message = banned_input_message
