class ValidationError(Exception):
    """Base class for handling validation errors"""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class MinSizeValidationError(ValidationError):
    pass


class MaxSizeValidationError(ValidationError):
    pass


class MinLengthValidationError(ValidationError):
    pass


class MaxLengthValidationError(ValidationError):
    pass


class RegexValidationError(ValidationError):
    pass


class BannedInputValidationError(ValidationError):
    pass


from dataclasses import dataclass
from typing import Any, Dict, Optional, Protocol

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
class BasicValidationConfig:
    validate_against: Any
    error_message: str
    extra: Optional[Dict[str, Any]] = None


class BasicValidationProtocol(Protocol):
    """Base validation functionality. base_validation()
    and error must be replaced in concrete classes"""

    name = "GenericValidation"
    error: Exception = ValidationError
    validate_against: Any
    error_message: str
    extra: Dict[str, Any]

    def __init__(self, config: BasicValidationConfig):
        self.validate_against: Any = config.validate_against
        self.error_message: str = config.error_message
        self.extra: Dict[str, Any] = config.extra

    def base_validation(self, input: Any) -> None:
        """Validate input against self.validate_against

        Args:
            input (Any): Input to validate

        Raises:
            self.error(): If validation fails
        """
        ...

    def _base_validation(self, input: Any) -> bool:
        """Validate input against self.validate_against

        Args:
            input (input_type): the input to validate

        Returns:
            bool: the status of the validation
        """
        ...


class MinSizeValidationProtocol(BasicValidationProtocol):
    """Minimum size validation functionality"""

    name = "MinSize"
    error: Exception = MinSizeValidationError


class MaxSizeValidationProtocol(BasicValidationProtocol):
    """Maximum size validation functionality"""

    name = "MaxSize"
    error: Exception = MaxSizeValidationError


class MinLengthValidationProtocol(BasicValidationProtocol):
    """Minimum length validation functionality"""

    name = "MinLength"
    error: Exception = MinLengthValidationError


class MaxLengthValidationProtocol(BasicValidationProtocol):
    """Maximum length validation functionality"""

    name = "MaxLength"
    error: Exception = MaxLengthValidationError


class RegexValidationProtocol(BasicValidationProtocol):
    """Regex pattern validation functionality"""

    name = "RegexPattern"
    error: Exception = RegexValidationError


class BannedInputValidationProtocol(BasicValidationProtocol):
    """Banned input validation functionality"""

    name = "BannedInput"
    error: Exception = BannedInputValidationError
