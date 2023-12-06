# Standard Library
import asyncio
import re
from dataclasses import dataclass
from typing import Generic, Optional, TypedDict, TypeVar, TypeVarTuple

from .options import GroupErrorsByEnum

SpecParamsT = TypeVar("SpecParamsT", bound="SpecParams")
SpecT = TypeVar("SpecT", bound="Spec")
SpecsT = TypeVarTuple("SpecsT")
GenericInputType = TypeVar("GenericInputType")


class SpecParams(TypedDict):
    """
    Keys are names of validation rules and values are parameters for validation rules,
    such as {"min_length": 7} or {"banned_inputs": ["banned_input1", "banned_input2"]}.
    """

    pass


@dataclass(kw_only=True)
class SpecConfig(Generic[SpecParamsT]):
    params: SpecParamsT
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


class SpecError(Exception):
    """Base class for handling sanitization errors"""

    pass


class Spec:
    """
    Base class for encapsulating validation and normalization
    logic along with a dynamically formatted error message.
    """

    # The id of the Spec is used to select it on a FieldSanitizer
    # or ObjectSanitizer with the sanitize_select argument.
    id = "generic"

    # The name of the spec is used as a key when FieldSanitizers
    # and ObjectSanitizers construct error messages.
    name = "GenericSpec"

    # The error of the spec is raised when validation fails.
    error: Exception = SpecError

    def __init__(self, config: SpecConfig):
        self.config = config

    async def sanitize(
        self,
        input_data: GenericInputType,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.SPEC,
    ) -> Optional[str]:
        """
        Validate input against self.config.params.

        Args:
            input_data (GenericInputType): input to validate.

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
                raise self.error(error)
            else:
                return error
        else:
            return None

    def _sanitize(self, input_data: GenericInputType) -> bool:
        """
        Sanitize input against self.params. Optionally, set the normalized
        attribute on the associated FieldSanitizer.

        Args:
            input_data (GenericInputType): input to validate.

        Returns:
            bool: the status of the sanitization.
        """
        raise NotImplementedError
