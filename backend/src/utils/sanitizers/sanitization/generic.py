from dataclasses import dataclass
from typing import Any, Dict, Generic, Optional, TypeVar, TypeVarTuple

from .. import object

SpecT = TypeVar("SpecT")
SanitizationT = TypeVar("SanitizationT", bound="Sanitization")
SanitizationsT = TypeVarTuple("SanitizationsT")
GenericInputType = TypeVar("GenericInputType")


@dataclass(kw_only=True)
class SanitizationConfig(Generic[SpecT]):
    spec: SpecT
    error_message: str
    extra: Optional[Dict[str, Any]] = None


class SanitizationError(Exception):
    """Base class for handling sanitization errors"""

    pass


class Sanitization:
    """Base sanitization functionality"""

    id = "generic"
    name = "Generic"
    error: Exception = SanitizationError

    def __init__(self, config: SanitizationConfig):
        self.spec = config.spec
        self.error_message = config.error_message
        self.extra = config.extra

    def sanitize(
        self,
        input_data: GenericInputType,
        group_errors_by: object.GroupErrorsOptionsEnum = object.GroupErrorsOptionsEnum.SANITIZATION,
    ) -> str:
        """
        Validate input against self.spec.

        Args:
            input_data (GenericInputType): input to validate.

        Raises:
            self.error(): if sanitization fails and group_errors_by
            allows it.
        """
        if not self._sanitize(input_data=input_data):
            error = self.error_message.format(spec=self.spec, input_data=input_data)

            if group_errors_by == object.GroupErrorsOptionsEnum.SANITIZATION:
                raise self.error(error)
            else:
                return error

    def _sanitize(self, input_data: Any) -> bool:
        """
        Validate input against self.validate_against

        Args:
            input_data (GenericInputType): input to sanitize.

        Returns:
            bool: the status of the sanitization.
        """
        raise NotImplementedError
