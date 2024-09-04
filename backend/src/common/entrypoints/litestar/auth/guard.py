# External Libraries
from litestar.connection import ASGIConnection
from litestar.handlers.base import BaseRouteHandler

# VerdanTech Source
from src import exceptions


def requires_account(connection: ASGIConnection, _: BaseRouteHandler) -> None:
    """
    Rejects the request early if it requires an account.
    Note that the ops layer should still be designed to check
    if the user passed in is genuine.

    Args:
        connection (ASGIConnection): the connection, with
            the authenticated user object or None

    Raises:
        exceptions.AuthorizationError: raised if the connection
            should be blocked
    """
    if not connection.user:
        raise exceptions.AuthorizationError()
