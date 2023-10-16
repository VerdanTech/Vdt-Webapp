from contextlib import asynccontextmanager

from litestar.exceptions import ValidationException as LitestarValidationException
from src.utils.sanitizers.sanitization.generic import (
    SanitizationError,
)


@asynccontextmanager
async def litestar_exception_map():
    """Map the native application exceptions to litestar equivalents"""
    try:
        yield
    except SanitizationError as error:
        raise LitestarValidationException(
            detail="Data validation error", extra=error.message, status_code=422
        ) from None
