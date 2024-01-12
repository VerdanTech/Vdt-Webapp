# Standard Library
from dataclasses import dataclass
from typing import Any

# VerdanTech Source
from src.interfaces.persistence.generic import AbstractRepository

from ..options import SelectEnum
from ..spec import Spec, SpecConfig, SpecError


@dataclass(kw_only=True)
class ExistsSpecConfig(SpecConfig):
    params = None
    # The repository to use for validation.
    repo: AbstractRepository
    # The name of the method on the repository that return True when
    # the input exists in the database and False when it doesn't.
    existence_method_name: str
    # The name of the argument on existence_method_name that represents
    # the input data that the repository is checking uniqueness on.
    existence_method_argument_name: str

    def __init__(
        self,
        error_message: str,
        repo: AbstractRepository,
        existence_method_name: str,
        existence_method_argument_name: str,
    ) -> None:
        self.error_message = error_message
        self.repo = repo
        self.existence_method_name = existence_method_name
        self.existence_method_argument_name = existence_method_argument_name

        self.repo.validate_async_dynamic_call_signature(
            method_name=self.existence_method_name,
            **{existence_method_argument_name: None},
        )


class ExistsSpecError(SpecError):
    pass


class ExistsSpec[ExistsSpecConfig](Spec):
    """Existance sanitization functionality"""

    id = SelectEnum.EXISTS
    name = "ExistenceSpec"
    error = ExistsSpecError

    async def _sanitize(self, input_data: Any) -> bool:
        """
        Reject the input if the repository's existence check method
        returns False.

        Args:
            input_data (Real): the input to validate.

        Returns:
            bool: validation result.
        """
        existence_check_result = await self.config.repo.async_dynamic_call(
            method_name=self.config.existence_method_name,
            bypass_validation=True,
            **{self.config.existence_method_argument_name: input_data},
        )

        return existence_check_result
