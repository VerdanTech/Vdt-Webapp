from typing import Any, Dict, Generic, Tuple, TypedDict, TypeVar, List, Type

from .field import FieldSanitizer
from .sanitization.generic import SanitizationError, SanitizationT


class ObjectSanitizerConfig(TypedDict):
    """TypedDict keys are field names and
    values are instances of FieldSanitizer
    """

    pass


ObjectSanitizerConfigT = TypeVar("ObjectSanitizerConfigT", bound=ObjectSanitizerConfig)

object_mapping = {
    "username": "username",
    "email_address": "emails.address",
    "password": None,
}


class ObjectSanitizer(Generic[ObjectSanitizerConfigT]):
    """This class allows assigning multiple FieldSanitizers to
    multiple object fields, and to validate all fields while grouping errors"""

    object_mapping: Dict[str, str]

    def __init__(self, config: ObjectSanitizerConfig):
        self.config = config

    def _get_field_sanitizer(self, field_name: str) -> FieldSanitizer:
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

    async def _use_field_sanitizer(
        self,
        input: Dict[str, Any],
        sanitized: Dict[str, Any],
        field_sanitizer: FieldSanitizer,
        field_name: str,
        disabled_sanitizations: List[Type[SanitizationT]] = None
    ) -> Dict[str, Any]:
        """Use the field sanitizer to sanitize,
        and if the sanitizer returns a normalized value,
            update the output sanitized data

        Args:
            input (Dict[str, Any]): the input to the object
                sanitizer sanitization function
            sanitized (Dict[str, Any]): the output sanitized data
            field_sanitizer (FieldSanitizer): the field sanitizer
                to use for the sanitization
            field_name (str): the name of the field to sanitize
            disabled_fields (Dict[str, List[Type[SanitizationT]] | None] | None):
                keys are field names to skip sanitization on, and values are a 
                list of sanitization types to skip sanitization on that field,
                or None if all sanitizations are to be skipped

        Returns:
            Dict[str, Any]: the output sanitized data
        """
        await field_sanitizer.sanitize(input=input, disabled_sanitizations=disabled_sanitizations)
        normalized = field_sanitizer.normalized()
        if normalized:
            sanitized[field_name] = normalized
        return sanitized

    async def _sanitize(
        self,
        input: Dict[str, Any],
        disabled_fields: Dict[str, List[Type[SanitizationT]] | None] | None = None,
    ) -> Tuple[Dict[str, Any], Dict[str, str]]:
        """Call the field sanitizer for every field in
        the input, and group sanitization errors together

        Args:
            input (Dict[str, Any]): the input data to sanitize
            disabled_fields (Dict[str, List[Type[SanitizationT]] | None] | None):
                keys are field names to skip sanitization on, and values are a 
                list of sanitization types to skip sanitization on that field,
                or None if all sanitizations are to be skipped

        Returns:
            Tuple[Dict[str, Any], Dict[str, str]]: the output sanitized
                data and the error dictionary
        """
        sanitized = input # Default normalized value is no chang
        error = {}  # Group exceptions

        for field_name, input in input.items():

            # Grab list of disabled sanitization types if any
            disabled_sanitizations = None
            if disabled_fields is not None and field_name in disabled_fields:
                if disabled_fields[field_name] is None:
                    continue
                else:
                    disabled_sanitizations = disabled_fields[field_name]

            field_sanitizer = self._get_field_sanitizer(field_name=field_name)

            try:
                sanitized = await self._use_field_sanitizer(
                    input=input,
                    sanitized=sanitized,
                    field_sanitizer=field_sanitizer,
                    field_name=field_name,
                    disabled_sanitizations=disabled_sanitizations
                )
            except SanitizationError as error_raised:
                error[field_name] = str(error_raised)

        return sanitized, error

    async def sanitize(
        self,
        input: Dict[str, Any],
        disabled_fields: Dict[str, List[Type[SanitizationT]] | None] | None = None,
    ) -> Dict[str, Any]:
        """Call the sanitization function, and raise error if any failure

        Args:
            input (Dict[str, Any]): the input fields to sanitize
            disabled_fields (Dict[str, List[Type[SanitizationT]] | None] | None):
                keys are field names to skip sanitization on, and values are a 
                list of sanitization types to skip sanitization on that field,
                or None if all sanitizations are to be skipped

        Raises:
            SanitizationError: raised if any field failed to validate

        Returns:
            Dict[str, Any]: the sanitized data
        """
        sanitized, error = await self._sanitize(
            input=input, disabled_fields=disabled_fields
        )
        if error:
            raise SanitizationError(error)

        return sanitized
