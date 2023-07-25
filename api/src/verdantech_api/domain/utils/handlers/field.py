from typing import Callable, Dict, Generic, List

from .sanitization.generic import GenericInputType, SanitizationError, SanitizationT


class NormalizedValueNotSet(Exception):
    pass


class FieldSanitizer(Generic[SanitizationT]):
    def __init__(self, *sanitizers: List[SanitizationT]):
        for sanitizer in sanitizers:
            sanitizer.field = self
        self.sanitizers = sanitizers
        self.normalized = None

    def _get_base_sanitization_methods(
        self,
    ) -> List[Callable[[Dict[str, str]], Dict[str, str]]]:
        """Returns a callable sanitization function for every
            Sanitization class

        Returns:
            List[Callable]: a list of sanitization methods
        """
        return [sanitizer.base_sanitization for sanitizer in self.sanitizations]

    def _sanitize(self, input: GenericInputType) -> Dict[str, str]:
        """Sanitizes the input against base sanitization logis

        Args:
            input (GenericInputType): The input to sanitize

        Returns:
            Dict[str, str]: Dict containing errors
        """

        # Group exceptions
        error = {}

        # Base sanitization logic here
        for sanitization_method in self._get_base_sanitization_methods():
            try:
                sanitization_method(input=input)
            except SanitizationError as error_raised:
                error[type(error_raised).__name__] = str(error_raised)

        return error

    def sanitize(self, input: GenericInputType) -> bool:
        # Set default normalized value
        self.normalized = input

        # Group exceptions
        error = self._sanitize(input=input)

        # Raise errors
        if error:
            raise SanitizationError(message=error)
        return True

    def normalized(self) -> GenericInputType:
        """Supply last input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """
        if not self.normalized:
            raise NormalizedValueNotSet(
                """
                Normalization requested from FieldSanitizer 
                with normalized value not set
                """
            )
        return self.normalized


class MockFieldSanitizer:
    """Mock sanitizer class for testing"""

    field_name: str = "generic_field"

    def sanitize(self, input: GenericInputType) -> bool:
        return True

    def normalize(self, input: GenericInputType) -> GenericInputType:
        return input
