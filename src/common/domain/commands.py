# Standard Library
from typing import Any, Callable

# External Libraries
from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    WrapValidator,
)
from pydantic_core import PydanticCustomError


class Command(BaseModel):
    """
    Represents a job the system may perform.

    Pydantic is used for a feature complete validation system
    for incoming inputs.
    """

    model_config = ConfigDict(frozen=True)

    @classmethod
    def to_operation_id(cls) -> str:
        """Converts the Command's type to an operation ID for use with OpenAPI."""
        return str(cls.__name__) + "Op"


class ValidatorWrapper[T]:
    """
    A WrapValidator that catches ValueError and AssertionError exceptions and
    raises a PydanticCustomError with the message from the original exception,
    while removing the error type prefix, which is not user-friendly.

    Credit to (https://github.com/pydantic/pydantic/discussions/8468#discussioncomment-10128759)
    """

    def __new__(cls, validator: Callable[[T], T]) -> WrapValidator:
        """
        Wrap a validator function with a WrapValidator that catches ValueError and
        AssertionError exceptions and raises a PydanticCustomError with the message
        from the original exception, while removing the error type prefix, which is
        not user-friendly.

        Args:
            validator: The validator function to wrap.

        Returns: A WrapValidator instance that prettifies error messages.
        """

        def _validator(v: T, handler: ValidatorFunctionWrapHandler, _: ValidationInfo):
            try:
                validator(v)
            except (ValueError, AssertionError) as exc:
                raise PydanticCustomError(
                    "",
                    str(exc),
                )

            return handler(v)

        return WrapValidator(_validator)
