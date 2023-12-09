# Standard Library
from contextlib import asynccontextmanager

# External Libraries
from litestar.exceptions import ValidationException as LitestarValidationException

# VerdanTech Source
from src.utils.sanitizers.spec import SpecError


@asynccontextmanager
async def litestar_exception_map():
    """Map the native application exceptions to litestar equivalents"""
    try:
        yield
    except SpecError as error:
        raise LitestarValidationException(
            detail="Data validation error", extra=error.message, status_code=422
        ) from None
