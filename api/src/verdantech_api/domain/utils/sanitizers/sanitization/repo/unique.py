from dataclasses import dataclass
from typing import Any, List, TypedDict

from litestar.contrib.repository.abc import AbstractAsyncRepository

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class UniqueSanitizationSpec(TypedDict):
    field: str


@dataclass(kw_only=True)
class UniqueSanitizationConfig(SanitizationConfig[UniqueSanitizationSpec]):
    repo: AbstractAsyncRepository


class UniqueSanitizationError(SanitizationError):
    pass


class UniqueSanitization(Sanitization):
    """Uniqueness sanitization functionality"""

    name = "Uniqueness"
    error: Exception = UniqueSanitizationError

    def __init__(self, config: UniqueSanitizationConfig):
        self.repo = config.repo
        super().__init__(config=config)

    async def _base_sanitization(self, input: Any) -> bool:
        kwargs = {self.spec["field"]: input}
        return not await self.repo.exists(**kwargs)
