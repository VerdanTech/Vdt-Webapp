import re
from numbers import Real
from typing import Any, Dict, List, Pattern, Type, TypeVar, Union

input_type = TypeVar("input_type")


class Validation:
    """Base validation functionality. Only base_validation
    must be replaced in concrete classes"""

    name = "GenericValidation"
    input_type: Type = input_type
    validate_against_type: Type = Any
    validate_against: validate_against_type
    error_message: str

    def __init__(self, validate_against: Any, error_message: str):
        self.validate_against = validate_against
        self.error_message = error_message

    def check_type(self, input: Any, expected_type: Type = input_type):
        """Ensure the input type is correct

        Args:
            input (Any): the input to check

        Raises:
            ValueError: raised if input type not input_type
        """
        if not isinstance(input, expected_type):
            raise ValueError(
                f"""Validator {self.name}: 
                expected input type {self.input_type}, 
                got {type(input)}"""
            )

    def base_validation(
        self, input: input_type, error: Dict[str, str]
    ) -> Dict[str, str]:
        """Validate input against self.validate_against

        Args:
            input (Any): Input to validate
            error (dict[str, str]): An error dict containing
                Validation class name and error_message for
                each error that has been raised so far in the flow

        Returns:
            Dict[str, str]: the input error dict, with any new errors
        """
        self.check_type(input=input, expected_type=input_type)
        if not self._base_validation(input=input):
            error[self.name] = self.error_message.format(
                validate_against=self.validate_against
            )
        return error

    def _base_validation(self, input: input_type) -> bool:
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
    input_type = Real
    validate_against_type = Real

    def _base_validation(self, input: Real) -> bool:
        if input < self.validate_against:
            return False
        else:
            return True


class MaxSizeValidation(Validation):
    """Maximum size validation functionality"""

    name = "MaxSize"
    input_type = Real
    validate_against_type = Real

    def _base_validation(self, input: Real) -> bool:
        if input > self.validate_against:
            return False
        else:
            return True


class MinLengthValidation(Validation):
    """Minimum length validation functionality"""

    name = "MinLength"
    input_type = str
    validate_against_type = int

    def _base_validation(self, input: str) -> bool:
        if len(input) < self.validate_against:
            return False
        else:
            return True


class MaxLengthValidation(Validation):
    """Maximum length validation functionality"""

    name = "MaxLength"
    input_type = str
    validate_against_type = int

    def _base_validation(self, input: str) -> bool:
        if len(input) > self.validate_against:
            return False
        else:
            return True


class RegexValidation(Validation):
    """Regex pattern validation functionality"""

    name = "RegexPattern"
    input_type = str
    validate_against_type = Pattern

    def _base_validation(self, input: str) -> bool:
        if not re.match(self.validate_against, input):
            return False
        else:
            return True


class BannedInputValidation(Validation):
    """Banned input validation functionality"""

    name = "BannedInput"
    input_type = Union[Real, str]
    validate_against_type = [Union[List[Real], List[str]]]
    normalize_banned_input_validation: bool

    def __init__(
        self,
        validate_against: Any,
        error_message: str,
        normalize_banned_input_validation: bool = False,
    ):
        super().__init__(validate_against=validate_against, error_message=error_message)
        self.normalize_banned_input_validation = normalize_banned_input_validation

    def _base_validation(self, input: Union[Real, str]) -> bool:
        if isinstance(input, str):
            if self.normalize_banned_input_validation:
                input = input.lower()
                self.validate_against = [
                    banned_input.lower() for banned_input in self.validate_against
                ]
        if input in self.validate_against:
            return False
        else:
            return True
