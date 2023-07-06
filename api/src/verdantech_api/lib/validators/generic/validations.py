import re
from abc import ABC, abstractmethod
from numbers import Real
from typing import Any, Dict, Pattern, Union


class ValidationMixin(ABC):
    """Base validation functionality. Corresponding validate_against and
    error_message must be set in Validator class __init__"""

    name = "GenericValidation"
    # validate_against: Any
    # error_message: str

    @abstractmethod
    def validation_base_validation(
        self, input: Any, error: Dict[str, str]
    ) -> Dict[str, str]:
        """Validate input against self.validate_against

        Args:
            input (Any): Input to validate
            error (dict[str, str]): An error dict containing
                ValidationMixin class name and error_message for
                each error that has been raised so far in the flow

        Raises:
            ValueError: if an improper type is passed in

        Returns:
            Dict[str, str]: the input error dict, with any new errors
        """
        # if input == self.validate_against:
        # error[self.name] = self.error_message.format(
        # message=self.validate_against_message
        # )
        return error


class MinSizeValidationMixin(ValidationMixin):
    """Minimum size validation functionality"""

    name = "MinSize"
    min_size: int
    min_size_message: str

    def min_size_base_validation(
        self, input: Real, error: Dict[str, str]
    ) -> Dict[str, str]:
        if self.min_size and input < self.min_size:
            error[self.name] = self.error_message.format(message=self.min_size_message)
        return error


class MaxSizeValidationMixin(ValidationMixin):
    """Maximum size validation functionality"""

    name = "MaxSize"
    max_size: int
    max_size_message: str

    def max_size_base_validation(
        self, input: Real, error: Dict[str, str]
    ) -> Dict[str, str]:
        if self.max_size and input > self.max_size:
            error[self.name] = self.error_message.format(message=self.max_size_message)
        return error


class MinLengthValidationMixin(ValidationMixin):
    """Minimum length validation functionality"""

    name = "MinLength"
    min_length: int
    min_length_message: str

    def min_length_base_validation(
        self, input: str, error: Dict[str, str]
    ) -> Dict[str, str]:
        if self.min_length and len(input) < self.min_length:
            error[self.name] = self.error_message.format(
                message=self.min_length_message
            )
        return error


class MaxLengthValidationMixin(ValidationMixin):
    """Maximum length validation functionality"""

    name = "MaxLength"
    max_length: int
    max_length_message: str

    def max_length_base_validation(
        self, input: str, error: Dict[str, str]
    ) -> Dict[str, str]:
        if self.max_length and len(input) > self.max_length:
            error[self.name] = self.error_message.format(
                message=self.max_length_message
            )
        return error


class RegexValidationMixin(ValidationMixin):
    """Regex pattern validation functionality"""

    name = "RegexPattern"
    regex: Pattern
    regex_message: str

    def regex_base_validation(
        self, input: str, error: Dict[str, str]
    ) -> Dict[str, str]:
        if self.regex and not re.match(self.regex, input):
            error[self.name] = self.error_message.format(message=self.regex_message)
        return error


class BannedInputValidationMixin(ValidationMixin):
    """Banned input validation functionality"""

    name = "BannedInput"
    blacklist: list[Union[Real, str]]
    whitelist: list[Union[Real, str]]
    banned_input_message: str
    normalize_banned_input_validation: bool

    def banned_input_base_validation(
        self, input: Union[Real, str], error: Dict[str, str]
    ) -> Dict[str, str]:
        if not self.blacklist:
            return error
        banned_inputs = set(self.blacklist) - set(self.whitelist)
        if isinstance(input, str):
            if self.normalize_banned_input_validation:
                input = input.lower()
                banned_inputs = [banned_input.lower() for banned_input in banned_inputs]
        if input in banned_inputs:
            error[self.name] = self.error_message.format(
                message=self.banned_input_message
            )
        return error
