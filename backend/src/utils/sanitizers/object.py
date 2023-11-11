from enum import Enum
from typing import Any, Dict, Generic, List, Tuple, Type, TypedDict, TypeVar

from . import field
from .sanitization.generic import SanitizationError, SanitizationT


class ObjectSanitizerConfig(TypedDict):
    """
    TypedDict keys are field names and
    values are instances of FieldSanitizer.
    """

    pass


ObjectSanitizerConfigT = TypeVar("ObjectSanitizerConfigT", bound=ObjectSanitizerConfig)


class GroupErrorsOptionsEnum(Enum):
    """
    Enumerated options for grouping errors.

    OBJECT: An ObjectSanitizer will group together the errors
        returned by the FieldSanitizers, and raise them together
        after all FieldSanitizers have been run. FieldSanitizers and
        Sanitizations will return rather than raise errors.
    FIELD: A FieldSanitizer will group together the errors returned
        by the Sanitizions, and raise them together after all Sanitizations
        have been run. Sanitizations will return rather than raise errors.
    SANITIZATION: A Sanitization will raise an exception and return no error.
        No errors will be grouped together, and Sanitizations will be run until one
        fails to sanitize.
    """

    OBJECT = 0
    FIELD = 1
    SANITIZATION = 2


class SelectEnum(Enum):
    """
    Enumerated aliases for selecting Sanitizations.

    Options that are specific to a Sanitization type correspond
    to the id attribute defined on that type.
    """

    # Options that aren't specific to a Sanitization type.
    ENABLE_ALL = "enable_all"
    DISABLE_ALL = "disable_all"

    # Basic sanitizations.
    LENGTH = "length"
    SIZE = "size"
    REGEX = "regex"
    BAN = "ban"

    # Repo sanitizations.
    UNIQUE = "unique"

    # Custom sanitizations.
    EMAIL = "email"


class ObjectSanitizer(Generic[ObjectSanitizerConfigT]):
    """This class allows assigning multiple FieldSanitizers to
    multiple object fields, and to validate all fields while grouping errors"""

    def __init__(self, config: ObjectSanitizerConfig):
        self.config = config

    async def sanitize(
        self,
        input_data: Dict[str, field.GenericInputType],
        sanitization_select: Dict[str, List[field.SelectEnum]],
        apply_sanitization_default: bool = False,
        group_errors_by: GroupErrorsOptionsEnum = GroupErrorsOptionsEnum.OBJECT,
    ) -> Dict[str, Any]:
        """
        Call the sanitization function on a dict input,
        and raise error if any failure.

        Args:
            input_data (Dict[str, GenericInputType]): keys are field names
                and values are field values to sanitize.
            sanitization_select (Dict[str, List[str]]):
                keys are field names and values are lists
                of values of SelectEnum, which allows filtering
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
            SanitizationError: raised if any field failed to validate, with
                errors grouped according to group_errors_by

        Returns:
            Dict[str, GenericInputType]: the sanitized data
        """
        sanitized_data, error = await self._sanitize(
            input_data=input_data,
            sanitization_select=sanitization_select,
            group_errors_by=group_errors_by,
            apply_sanitization_default=apply_sanitization_default,
        )
        if error:
            raise SanitizationError(error)

        return sanitized_data

    async def sanitize_object(self, object: Any) -> None:
        """
        Implement object-specific logic for validating object
            instances as opposed to dicts.

        Args:
            object (Any): the object to sanitize.
        """
        raise NotImplementedError

    async def _sanitize(
        self,
        input_data: Dict[str, field.GenericInputType],
        sanitization_select: Dict[str, List[field.SelectEnum]],
        apply_sanitization_default: bool = False,
        group_errors_by: GroupErrorsOptionsEnum = GroupErrorsOptionsEnum.OBJECT,
    ) -> Tuple[Dict[str, Any], Dict[str, str]]:
        """
        Call the field sanitizer for every field in
        the input, and group sanitization errors together.

        Args:
            input_data (Dict[str, GenericInputType]): see sanitize() method
            sanitization_select (Dict[str, List[SelectEnum]]): see sanitize() method
            group_errors_by (GroupErrorsOptionsEnum): see sanitize() method
            apply_sanitization_default (bool): see sanitize() method

        Returns:
            Tuple[Dict[str, GenericInputType], Dict[str, str]]: the output sanitized
                data and the error dictionary.
        """
        # Default normalized value is no change
        object_sanitized_data = input_data
        # Group exceptions
        object_error = {}

        # For every input field
        for field_name, field_input_data in input.items():
            # Get the FieldSanitizer associated with that field.
            # Raise exception if FieldSanitizer not found.
            field_sanitizer = self._get_field_sanitizer(field_name=field_name)

            # Call the FieldSanitizer's sanitize() method.
            field_sanitization_select = sanitization_select[field_name]
            field_sanitized_data, field_error = await field_sanitizer.sanitize(
                input_data=field_input_data,
                sanitization_select=field_sanitization_select,
                group_errors_by=group_errors_by,
                apply_sanitization_default=apply_sanitization_default,
            )

            if field_error is not None:
                # Update the output error
                object_error[field_name] = field_error

            # Update the output sanitized data if it was safely returned from the FieldSanitizer.
            if field_sanitized_data is not None:
                object_sanitized_data[field_name] = field_sanitized_data

        return object_sanitized_data, object_error

    def _get_field_sanitizer(self, field_name: str) -> field.FieldSanitizer:
        """Get the sanitizer for the field from the
            config, or raise an error if it doesn't exist

        Args:
            field_name (str): the field to get the
                sanitizer for

        Raises:
            ValueError: raised if field not found

        Returns:
            FieldSanitizer: the found sanitizer
        """
        field_sanitizer = self.config.get(field_name)
        if not field_sanitizer:
            raise ValueError(f"No field sanitizer found for field: {field_name}")
        return field_sanitizer


class MockObjectSanitizer(ObjectSanitizer):
    """Mock object sanitizer for testing"""

    def __init__(self) -> None:
        pass

    async def sanitize(
        self,
        input: Dict[str, Any],
        sanitization_select: Dict[str, List[field.SelectEnum]],
        group_errors_by: field.GroupErrorsOptionsEnum = field.GroupErrorsOptionsEnum.OBJECT,
        apply_sanitization_default: bool = False,
    ) -> Dict[str, Any]:
        return input

    async def sanitize_object(self, object: Any) -> None:
        return
