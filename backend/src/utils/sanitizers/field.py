import asyncio
from enum import Enum
from typing import Any, Callable, Dict, Generic, List, Tuple, Type

from . import object
from .sanitization.generic import (
    GenericInputType,
    SanitizationError,
    SanitizationsT,
    SanitizationT,
)


class FieldSanitizer(Generic[*SanitizationsT]):
    def __init__(self, *sanitizations: List[SanitizationT]):
        for sanitization in sanitizations:
            sanitization.field = self
        self.sanitizations = sanitizations
        self.normalized_input = None

    async def sanitize(
        self,
        input_data: GenericInputType,
        sanitization_select: List[object.SelectEnum],
        apply_sanitization_default: bool = False,
        group_errors_by: object.GroupErrorsOptionsEnum = object.GroupErrorsOptionsEnum.FIELD,
    ) -> Tuple[GenericInputType, Dict[str, str]]:
        """
        Call the sanitization function, and raise error if any failure.

        Args:
            input (GenericInputType): the input to sanitize.
            sanitization_select (List[SelectEnum]):
                list of values of SelectEnum, which allows filtering
                the list of Sanitizations registered on each field.
            group_errors_by (GroupErrorsOptionsEnum): see GroupErrorsOptionsEnum
                for behavior description.
            apply_sanitization_default (bool) True applies all sanitizations
                registered on a FieldSanitizer by default. The selections in
                sanitization_select disable Sanitizations from being applied.
                False applied no sanitizations registered on a FieldSanitizer
                by default. The selections in sanitization_select enable
                Sanitizations from being applied. Defaults to False.

        Raises:
            SanitizationError: raised if sanitization fails and group_errors_by
                is FIELD or SANITIZATION.

        Returns:
            Tuple[GenericInputType, Dict[str, str]]: GenericInputType is the
                sanitized output data. Dict[str, str] is the error message, where
                the keys are names of Sanitizations, and the values are the error messages.
        """
        # Set default normalized value
        self.normalized = input

        # Group exceptions
        error = await self._sanitize(
            input_data=input_data,
            sanitization_select=sanitization_select,
            apply_sanitization_default=apply_sanitization_default,
        )

        # Raise errors if enabled.
        if error and (
            group_errors_by == object.GroupErrorsOptionsEnum.FIELD
            or group_errors_by == object.GroupErrorsOptionsEnum.SANITIZATION
        ):
            raise SanitizationError(error)

        return self.normalized, error

    async def _sanitize(
        self,
        input_data: GenericInputType,
        sanitization_select: List[object.SelectEnum],
        apply_sanitization_default: bool = False,
        group_errors_by: object.GroupErrorsOptionsEnum = object.GroupErrorsOptionsEnum.FIELD,
    ) -> Dict[str, str]:
        """
        Sanitizes the input against Sanitizations.

        Args:
            input_data (GenericInputType): see sanitize() method.
            sanitization_select (List[SelectEnum]): see sanitize() method.
            group_errors_by (GroupErrorsOptionsEnum): see sanitize() method.
            apply_sanitization_default (bool): see sanitize() method.

        Returns:
            Dict[str, str]: Dict containing errors.
        """

        # Group exceptions
        error = {}

        # For every enabled Sanitization, run the sanitization logic.
        for sanitization in self._select_sanitizations(
            sanitization_select=sanitization_select,
            apply_sanitization_default=apply_sanitization_default,
        ):
            if asyncio.iscoroutinefunction(sanitization.sanitize):
                sanitization_error = await sanitization.sanitize(
                    input_data=input_data, group_errors_by=group_errors_by
                )
            else:
                sanitization_error = sanitization.sanitize(
                    input_data=input_data, group_errors_by=group_errors_by
                )

            # Update the output error
            if sanitization_error:
                error[sanitization.name] = sanitization_error

        return error

    def _select_sanitizations(
        self,
        sanitization_select: List[object.SelectEnum],
        apply_sanitization_default: bool = False,
    ) -> List[Callable[[Dict[str, str]], Dict[str, str]]]:
        """
        Returns a Sanitization for every Sanitization class
        that is selected based on the arguments.

        Args:
            sanitization_select (List[SelectEnum]): see sanitize() method.
            apply_sanitization_default (bool): see sanitize() method.

        Returns:
            List[Sanitization]: a list of enabled Sanitizations.
        """
        # A DISABLE_ALL selection results in no sanitization.
        if object.SelectEnum.DISABLE_ALL in sanitization_select:
            return []

        # An ENABLE_ALL selection results in all sanitizations.
        if object.SelectEnum.ENABLE_ALL in sanitization_select:
            return self.sanitizations

        # A False apply_sanitization_default results in all sanitizations
        # with IDs that aren't selected within sanitization_select
        if apply_sanitization_default is True:
            return [
                sanitization
                for sanitization in self.sanitizaitons
                if sanitization.id not in sanitization_select
            ]

        # A False apply_sanitization_default results in all sanitizations
        # with IDs that are selected within sanitization_select
        if apply_sanitization_default is False:
            return [
                sanitization
                for sanitization in self.sanitizations
                if sanitization.id in sanitization_select
            ]

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
