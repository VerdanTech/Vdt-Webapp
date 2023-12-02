# Standard Library
from contextlib import asynccontextmanager

# External Libraries
from backend.src.utils.sanitizers.sanitization.sanitization import SanitizationError
from litestar.exceptions import ValidationException as LitestarValidationException


@asynccontextmanager
async def litestar_exception_map():
    """Map the native application exceptions to litestar equivalents"""
    try:
        yield
    except SanitizationError as error:
        raise LitestarValidationException(
            detail="Data validation error", extra=error.message, status_code=422
        ) from None
