# External Libraries
from litestar import Request, Response

# VerdanTech Source
from src import exceptions


def application_exception_handler(_: Request, exc: exceptions.ApplicationException):
    """
    Transform an ApplicationException into an Http Response.
    """
    return Response(
        status_code=exc.status_code, content={"detail": str(exc), "extra": exc.extra}
    )
