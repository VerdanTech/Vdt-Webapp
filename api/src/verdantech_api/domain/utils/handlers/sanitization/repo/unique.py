from typing import TypedDict

from litestar.contrib.repository.abc import AbstractAsyncRepository
from litestar.contrib.repository.filters import CollectionFilter

from ..generic import Sanitization, SanitizationConfig, SanitizationError


class UniqueSanitizationSpec(TypedDict):
    field_name: str
    repo: AbstractAsyncRepository


class UniqueSanitizationConfig(SanitizationConfig[UniqueSanitizationSpec]):
    pass


class UniqueSanitizationError(SanitizationError):
    pass


class UniqueSanitization(Sanitization):
    """Length sanitization functionality"""

    name = "Uniqueness"
    error: Exception = UniqueSanitizationError

    async def _base_sanitization(self, input: str) -> bool:
        return not await self.spec.repo.exists(
            CollectionFilter(field_name=self.spec.field_name, values=input)
        )
