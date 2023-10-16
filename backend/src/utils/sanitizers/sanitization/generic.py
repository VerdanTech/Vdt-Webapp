from dataclasses import dataclass
from typing import Any, Dict, Generic, Optional, TypeVar, TypeVarTuple

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

    name = "GenericSanitization"
    error: Exception = SanitizationError

    def __init__(self, config: SanitizationConfig):
        self.spec = config.spec
        self.error_message = config.error_message
        self.extra = config.extra

    def base_sanitization(self, input: GenericInputType) -> None:
        """Validate input against self.validate_against

        Args:
            input (Any): Input to validate

        Raises:
            self.error(): If sanitization fails
        """
        if not self._base_sanitization(input=input):
            raise self.error(self.error_message.format(spec=self.spec))

    def _base_sanitization(self, input: Any) -> bool:
        """Validate input against self.validate_against

        Args:
            input (input_type): the input to validate

        Returns:
            bool: the status of the sanitization
        """
        raise NotImplementedError
