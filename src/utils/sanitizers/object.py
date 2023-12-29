# Standard Library
from typing import Any, TypedDict

from . import field, spec
from .options import GroupErrorsByEnum, SelectEnum

type FieldName = str
"""Type alias for the names of fields put under sanitization."""
type ObjectInputType = dict[FieldName, spec.InputType]
"""Type alias for the mapping input to the ObjetSanitizer."""
type SpecSelectType = dict[FieldName, list[SelectEnum]]
"""Type alias for the spec selection input to the ObjectSanitizer"""


class ObjectSanitizerConfig(TypedDict):
    """
    TypedDict keys are field names and
    values are instances of FieldSanitizer.
    """

    pass


class ObjectSanitizer[C: ObjectSanitizerConfig]:
    """
    This class allows assigning multiple FieldSanitizers to
    multiple object fields and to validate all fields while grouping errors.
    """

    def __init__(self, config: C):
        self.config = config

    async def sanitize(
        self,
        input_data: ObjectInputType,
        spec_select: SpecSelectType,
        apply_default: bool = False,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.OBJECT,
    ) -> dict[str, Any]:
        """
        Call the sanitization function on a dict input,
        and raise error if any failure.

        Args:
            input_data (dict[str, GenericInputType]): keys are field names
                and values are field values to sanitize.
            spec_select (dict[str, list[str]]):
                keys are field names and values are lists
                of values of SelectEnum, which allows filtering
                the list of Sanitizations registered on each field.
            group_errors_by (GroupErrorsOptionsEnum): see GroupErrorsOptionsEnum
                for behavior description.
            apply_default (bool) True applies all sanitizations
                registered on a FieldSanitizer by default. The selections in
                sanitization_select disable Sanitizations from being applied.
                False applied no sanitizations registered on a FieldSanitizer
                by default. The selections in sanitization_select enable
                Sanitizations from being applied. Defaults to False.

        Raises:
            SanitizationError: raised if any field failed to validate, with
                errors grouped according to group_errors_by

        Returns:
            dict[str, GenericInputType]: the sanitized data
        """
        sanitized_data, error = await self._sanitize(
            input_data=input_data,
            spec_select=spec_select,
            group_errors_by=group_errors_by,
            apply_default=apply_default,
        )
        if error:
            raise spec.SpecError(error)

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
        input_data: ObjectInputType,
        spec_select: SpecSelectType,
        apply_default: bool = False,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.OBJECT,
    ) -> tuple[dict[str, spec.InputType], dict[str, str]]:
        """
        Call the field sanitizer for every field in
        the input, and group sanitization errors together.

        Args:
            input_data (ObjectInputType): see sanitize() method
            spec_select (SpecSelectType): see sanitize() method
            group_errors_by (GroupErrorsOptionsEnum): see sanitize() method
            apply_default (bool): see sanitize() method

        Returns:
            tuple[dict[str, InputType], Dict[str, str]]: the output sanitized
                data and the error dictionary.
        """
        # Default normalized value is no change
        object_sanitized_data = input_data
        # Group exceptions
        object_error = {}

        # For every input field
        for field_name, field_input_data in input_data.items():
            # Get the FieldSanitizer associated with that field.
            # Raise exception if FieldSanitizer not found.
            field_sanitizer = self._get_field_sanitizer(field_name=field_name)

            # Call the FieldSanitizer's sanitize() method.
            field_spec_select = spec_select[field_name]
            field_sanitized_data, field_error = await field_sanitizer.sanitize(
                input_data=field_input_data,
                spec_select=field_spec_select,
                group_errors_by=group_errors_by,
                apply_default=apply_default,
            )

            if field_error:
                # Update the output error
                object_error[field_name] = field_error

            # Update the output sanitized data if it was safely returned from the FieldSanitizer.
            if field_sanitized_data:
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
        input_data: dict[str, spec.InputType],
        spec_select: dict[str, list[SelectEnum]],
        apply_default: bool = False,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.OBJECT,
    ) -> dict[str, Any]:
        return input_data

    async def sanitize_object(self, object: Any) -> None:
        return
