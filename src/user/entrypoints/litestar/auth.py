# External Libraries
from litestar import Controller, Response, post, status_codes
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.auth import jwt_cookie_auth
from src.common.entrypoints.litestar.exceptions import (
    ClientError,
    litestar_exception_map,
)
from src.common.entrypoints.litestar.utils import url_to_route_name
from src.user.ops import queries

from . import urls


class UserAuthController(Controller):
    """
    User auth ASGI controller.
    """

    path = urls.USER_COMMAND_CONTROLLER_BASE
    tags = ["users"]

    @post(
        path=urls.USER_LOGIN_URL,
        name=url_to_route_name(urls.USER_LOGIN_URL),
        opt={"exclude_from_auth": True},
        summary="User login",
        description="Authenticate the request with JWT cookie authentication.",
    )
    async def user_login(
        self,
        data: queries.PasswordVerificationQuery,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[None]:
        """
        Uses the application query and Litestar's built in JWT auth to log
        the user in with a JWT cookie authentication scheme.

        Args:
            data (PasswordVerificationQuery): input query.
            state (State): litestar application state.
            svcs_container (Container): service container.

        Returns:
            Response[None]: a response containing the success code.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            verification_result = await queries.verify_password(
                query=data, svcs_container=svcs_container
            )
            if verification_result.verified is True:
                return jwt_cookie_auth.login(
                    identifier=str(verification_result.user_id),
                    response_body=None,
                )
            else:
                raise ClientError(status_code=status_codes.HTTP_401_UNAUTHORIZED)
