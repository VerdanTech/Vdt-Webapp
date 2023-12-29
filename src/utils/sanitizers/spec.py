# Standard Library
import asyncio
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Coroutine, Optional, Type, TypedDict

if TYPE_CHECKING:
    from .field import FieldSanitizer

from .options import GroupErrorsByEnum, SelectEnum

type InputType = Any
type SpecErrorMessage = str | dict[str, str] | dict[str, dict[str, str]]
"""
The SpecError's message can take one of three forms:
    - str when raised on the Spec level with group_errors_by = SPEC.
        The message is the message attribute on the Spec class, formatted
        with the parameters and input data.
    - dict[str, str] when raised on the FieldSanitizer level 
        with group_errors_by = FIELD. The keys are the name attributes 
        of Specs and the values are the Spec-level error messages.
    - dict[str, dict[str, str]] when raised on the ObjectSanitizer
        level with group_errors_by = OBJECT. The keys are the names
        of field attributes set on the ObjectSanitizer and the values
        are the FieldSanitizer-level error messages. 
"""


class SpecError(Exception):
    """Base class for handling sanitization errors"""

    message: SpecErrorMessage

    def __init__(self, message: SpecErrorMessage) -> None:
        super().__init__(message)
        self.message = message


class SpecParams(TypedDict):
    """
    Keys are names of validation rules and values are parameters for validation rules,
    such as {"min_length": 7} or {"banned_inputs": ["banned_input1", "banned_input2"]}.
    """

    pass


@dataclass(kw_only=True)
class SpecConfig[T: SpecParams]:
    params: T
    error_message: str

    def __post_init__(self) -> None:
        self._validate_error_message_params()

    def _validate_error_message_params(self) -> None:
        """
        If the error message supplied contains parameters
        enclosed in "{}" that aren't contained in the self.params
        or "input_data", a ValueError is raised.

        Raises:
            ValueError: raised if the error message set on self
                contains parameters not supplied by self.params
                or "input_data."
        """
        # Extract all .format() parameters enclosed in "{}"
        pattern = r"\{([^\{\}]+)\}"
        placeholders = re.findall(pattern, self.error_message)
        if placeholders is None:
            return

        # If params is None, reform into an unpackable type
        self.params = self.params or {}

        # The parameters formatted into an error message are unpacked self.params plus input_data
        error_message_format_parameters = {**self.params, "input_data": None}

        missing_params = [
            p for p in placeholders if p not in error_message_format_parameters
        ]
        if missing_params:
            raise ValueError(
                f"Missing parameters in error message for {self.__class__.__name__}: {', '.join(missing_params)}."
            )


class Spec[C: SpecConfig]:
    """
    Base class for encapsulating validation and normalization
    logic along with a dynamically formatted error message.

    Implements sanitization interface.

    Sanitization logic, including one of _sanitize or _asanitize is implemented by subclasses.
    """

    # The id of the Spec is used to select it on a FieldSanitizer
    # or ObjectSanitizer with the spec_select argument.
    id: SelectEnum

    # The name of the spec is used as a key when FieldSanitizers
    # and ObjectSanitizers construct error messages.
    name = "GenericSpec"

    # The error of the spec is raised when validation fails.
    error: Type[SpecError] = SpecError

    # A reference to the containing FieldSanitizer is held
    # for setting normalized data on the parent.
    field_sanitizer: Optional["FieldSanitizer"]

    def __init__(self, config: C):
        self.config = config
        self.field_sanitizer = None

    async def sanitize(
        self,
        input_data: InputType,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.SPEC,
    ) -> Optional[str]:
        """
        Validate input against self.config.params.

        Args:
            input_data (InputType): input to validate.

        Raises:
            self.error(): if sanitization fails and group_errors_by
            is equal to GroupErrorsByEnum.SPEC.
        """
        # Some Specs require access to async interfaces, such as the
        # Specs that rely on Repositories. Select the correct calling
        # API based on whether the inner sanitization function is async.
        if asyncio.iscoroutinefunction(self._sanitize):
            sanitization_clear = await self._sanitize(input_data=input_data)
        else:
            sanitization_clear = self._sanitize(input_data=input_data)

        if not sanitization_clear:
            # The error message is formatted with the SpecParams and input data
            self.config.params = self.config.params or {}
            error_message_format_parameters = {
                **self.config.params,
                "input_data": input_data,
            }
            error = self.config.error_message.format(**error_message_format_parameters)

            # Raise error if group_by_error calls for errors to be raised at the Spec level.
            # Otherwire return error.
            if group_errors_by == GroupErrorsByEnum.SPEC:
                raise self.error(message=error)
            else:
                return error
        else:
            return None

    def _sanitize(self, input_data: InputType) -> bool | Coroutine[Any, Any, bool]:
        """
        Sanitize input against self.params. Optionally, set the normalized
        attribute on the associated FieldSanitizer.

        Args:
            input_data (InputType): input to validate.

        Returns:
            bool | Coroutine[Any, Any, bool]: the status of the sanitization.
        """
        raise NotImplementedError
