import re
from dataclasses import dataclass
from numbers import Real
from typing import Any, Dict, List, Optional, Pattern, Type, Union

from .errors import (
    BannedInputValidationError,
    MaxLengthValidationError,
    MaxSizeValidationError,
    MinLengthValidationError,
    MinSizeValidationError,
    RegexValidationError,
    ValidationError,
)


@dataclass
class ValidationConfig:
    validate_against: Any
    error_message: str
    extra: Optional[Dict[str, Any]] = None


class Validation:
    """Base validation functionality. base_validation()
    and error must be replaced in concrete classes"""

    name = "GenericValidation"
    error: Exception = ValidationError

    def __init__(self, config: ValidationConfig):
        self.validate_against: Any = config.validate_against
        self.error_message: str = config.error_message
        self.extra: Dict[str, Any] = config.extra

    def base_validation(self, input: Any) -> None:
        """Validate input against self.validate_against

        Args:
            input (Any): Input to validate

        Raises:
            self.error(): If validation fails. Raised
            with self.error_message formatted
                with self.validate_against
        """
        if not self._base_validation(input=input):
            raise self.error(
                message=self.error_message.format(
                    validate_against=self.validate_against
                )
            )

    def _base_validation(self, input: Any) -> bool:
        """Validate input against self.validate_against

        Args:
            input (input_type): the input to validate

        Returns:
            bool: the status of the validation
        """
        return False


class MinSizeValidation(Validation):
    """Minimum size validation functionality"""

    name = "MinSize"
    error: Exception = MinSizeValidationError

    def _base_validation(self, input: Real) -> bool:
        if input < self.validate_against:
            return False
        else:
            return True


class MaxSizeValidation(Validation):
    """Maximum size validation functionality"""

    name = "MaxSize"
    error: Exception = MaxSizeValidationError

    def _base_validation(self, input: Real) -> bool:
        if input > self.validate_against:
            return False
        else:
            return True


class MinLengthValidation(Validation):
    """Minimum length validation functionality"""

    name = "MinLength"
    error: Exception = MinLengthValidationError

    def _base_validation(self, input: str) -> bool:
        if len(input) < self.validate_against:
            return False
        else:
            return True


class MaxLengthValidation(Validation):
    """Maximum length validation functionality"""

    name = "MaxLength"
    error: Exception = MaxLengthValidationError

    def _base_validation(self, input: str) -> bool:
        if len(input) > self.validate_against:
            return False
        else:
            return True


class RegexValidation(Validation):
    """Regex pattern validation functionality"""

    name = "RegexPattern"
    error: Exception = RegexValidationError

    def _base_validation(self, input: str) -> bool:
        if not re.match(self.validate_against, input):
            return False
        else:
            return True


class BannedInputValidation(Validation):
    """Banned input validation functionality"""

    name = "BannedInput"
    error: Exception = BannedInputValidationError

    def _base_validation(self, input: Union[Real, str]) -> bool:
        if self.extra["normalize_banned_input_validation"] and isinstance(input, str):
            input = input.lower()
            self.validate_against = [
                banned_input.lower() for banned_input in self.validate_against
            ]
        if input in self.validate_against:
            return False
        else:
            return True
