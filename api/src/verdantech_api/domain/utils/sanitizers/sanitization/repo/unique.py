from dataclasses import dataclass
from typing import Any, List, TypedDict

from litestar.contrib.repository.abc import AbstractAsyncRepository

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class UniqueSanitizationSpec(TypedDict):
    uniqueness_method_argument_name: str


@dataclass(kw_only=True)
class UniqueSanitizationConfig(SanitizationConfig[UniqueSanitizationSpec]):
    repo: AbstractAsyncRepository
    uniqueness_method_name: str


class UniqueSanitizationError(SanitizationError):
    pass


class UniqueSanitization(Sanitization):
    """Uniqueness sanitization functionality"""

    name = "Uniqueness"
    error: Exception = UniqueSanitizationError

    def __init__(self, config: UniqueSanitizationConfig):
        self.repo = config.repo
        self.uniqueness_method_name = config.uniqueness_method_name
        super().__init__(config=config)

    async def _base_sanitization(self, input: Any) -> bool:
        kwargs = {self.spec["uniqueness_method_argument_name"]: input}
        return not await self.repo.async_dynamic_call(
            method_name=self.uniqueness_method_name, **kwargs
        )
