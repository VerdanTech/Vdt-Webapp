# Standard Library
from contextlib import contextmanager

# External Libraries
from litestar import status_codes
from litestar.exceptions import (
    ClientException as LitestarClientException,
    InternalServerException as LitestarServerException,
)

# VerdanTech Source
from src import exceptions
from src.exceptions import ExceptionResponseEnum


class ServerError(LitestarServerException):
    """Raised on any error not due to a bad request."""

    status_code: int = status_codes.HTTP_500_INTERNAL_SERVER_ERROR


class ClientError(LitestarClientException):
    """Raised on error with the client request, that was not already raised in schema validation."""

    status_code: int = status_codes.HTTP_422_UNPROCESSABLE_ENTITY


@contextmanager
def litestar_exception_map():
    """Map the native application exceptions to litestar equivalents."""
    try:
        yield
    except exceptions.ApplicationException as exc:
        match exc.response:
            case ExceptionResponseEnum.SERVER_ERROR:
                raise ServerError(detail=str(exc))
            case ExceptionResponseEnum.CLIENT_ERROR:
                raise ClientError(detail=str(exc))
