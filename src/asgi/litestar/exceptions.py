# Standard Library
from contextlib import contextmanager

# External Libraries
from litestar import MediaType, Request, Response, status_codes
from litestar.exceptions import ClientException
from litestar.types import ExceptionHandlersMap

# VerdanTech Source
from src.ops import exceptions as ops_exceptions
from src.utils.sanitizers.spec import SpecError


@contextmanager
def litestar_exception_map():
    """Map the native application exceptions to litestar equivalents."""
    try:
        yield
    except ops_exceptions.EntityNotFound:
        raise ClientException(detail="Entity not found.", status_code=404, extra=None)


def spec_error_handler(request: Request, exc: SpecError) -> Response:
    """
    Transform a SpecError into an http response.

    Args:
        request (Request): route handler request object.
        exc (SpecError): raised exception.

    Returns:
        Response: http response to return.
    """
    status_code = status_codes.HTTP_422_UNPROCESSABLE_ENTITY
    spec_error_message = exc.message

    return Response(
        media_type=MediaType.JSON,
        content=spec_error_message,
        status_code=status_code,
    )


exception_handlers: ExceptionHandlersMap = {SpecError: spec_error_handler}
