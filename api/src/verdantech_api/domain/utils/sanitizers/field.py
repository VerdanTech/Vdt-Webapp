import asyncio
from typing import Callable, Dict, Generic, List, Type

from .sanitization.generic import GenericInputType, SanitizationError, SanitizationT


class FieldSanitizer(Generic[SanitizationT]):
    def __init__(self, *sanitizations: List[SanitizationT]):
        for sanitization in sanitizations:
            sanitization.field = self
        self.sanitizations = sanitizations
        self.normalized_input = None

    def _get_base_sanitization_methods(
        self, disabled_sanitizations: List[Type[SanitizationT]] = None
    ) -> List[Callable[[Dict[str, str]], Dict[str, str]]]:
        """Returns a callable sanitization function for every
            Sanitization class that is not disabled

        Returns:
            List[Callable]: a list of sanitization methods
        """
        if disabled_sanitizations is None:
            return [
                sanitizer.base_sanitization
                for sanitizer in self.sanitizations
            ]
        else:
            return [
                sanitizer.base_sanitization
                for sanitizer in self.sanitizations
                if type(sanitizer) not in disabled_sanitizations
            ]

    async def _sanitize(
        self, input: GenericInputType, disabled_sanitizations: List[Type[SanitizationT]] = None
    ) -> Dict[str, str]:
        """Sanitizes the input against base sanitization logis

        Args:
            input (GenericInputType): the input to sanitize
            disabled_sanitizations (List[Type[SanitizationT]]): list of 
                sanitization types to skip when performing sanitization

        Returns:
            Dict[str, str]: Dict containing errors
        """

        # Group exceptions
        error = {}

        # Base sanitization logic here
        for sanitization_method in self._get_base_sanitization_methods(
            disabled_sanitizations=disabled_sanitizations
        ):
            try:
                if asyncio.iscoroutinefunction(sanitization_method):
                    await sanitization_method(input=input)
                else:
                    sanitization_method(input=input)
            except SanitizationError as error_raised:
                error[type(error_raised).__name__] = str(error_raised)

        return error

    async def sanitize(
        self, input: GenericInputType, disabled_sanitizations: List[Type[SanitizationT]] = None
    ) -> bool:
        """Call the sanitization function, and raise error if any failure

        Args:
            input (GenericInputType): the input to sanitize
            disabled_sanitizations (List[Type[SanitizationT]]): list of 
                sanitization types to skip when performing sanitization

        Raises:
            SanitizationError: raised if sanitization fails

        Returns:
            bool: true if successful 
        """
        # Set default normalized value
        self.normalized = input

        # Group exceptions
        error = await self._sanitize(
            input=input, disabled_sanitizations=disabled_sanitizations
        )

        # Raise errors
        if error:
            raise SanitizationError(error)
        return True

    def normalized(self) -> GenericInputType:
        """Supply last input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """
        return self.normalized_input or None


class MockFieldSanitizer(FieldSanitizer):
    """Mock sanitizer class for testing"""

    field_name: str = "generic_field"

    def sanitize(self, input: GenericInputType) -> bool:
        return True

    def normalized(self) -> GenericInputType:
        return input
