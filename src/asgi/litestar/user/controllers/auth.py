# Standard Library
import pdb

# External Libraries
from litestar import Controller, Response, post, status_codes
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.auth import jwt_cookie_auth
from src.asgi.litestar.exceptions import litestar_exception_map
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user.controllers.auth import UserAuthOpsController
from src.ops.user.schemas import auth as auth_ops_schemas

from .. import routes, urls


class UserAuthApiController(Controller):
    """User authentication operations controller"""

    path = urls.USER_AUTH_CONTROLLER_BASE

    @post(
        path=urls.USER_LOGIN_URL,
        name=routes.USER_LOGIN_NAME,
        opt={"exclude_from_auth": True},
        summary="User login",
        description="Authenticate the request with JWT cookie authentication.",
        operation_id=routes.USER_EMAIL_VERIFICATION_REQUEST_NAME,
        tags=["users"],
    )
    async def user_login(
        self,
        data: auth_ops_schemas.UserLoginInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[User] | Response:
        """
        Uses the application operation and Litestar's built in JWT auth to log
        the user in with a JWT cookie authentication scheme.

        Args:
            data (schemas.UserLoginInput): input DTO.
            state (State): litestar application state.
            svcs_container (Container): svcs service container.

        Returns:
            Response[User] | Response: a response containing JWT auth or None.
        """
        svcs_container.register_local_value(State, state)
        user_auth_ops_controller, user_sanitizer = await svcs_container.aget(
            UserAuthOpsController, UserSanitizer
        )
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)
        with litestar_exception_map():
            user = await user_auth_ops_controller.login(
                data=data, user_sanitizer=user_sanitizer, password_crypt=password_crypt
            )
        if user is None:
            return Response(
                status_code=status_codes.HTTP_401_UNAUTHORIZED, content=None
            )
        else:
            return jwt_cookie_auth.login(identifier=str(user.id), response_body=user)
