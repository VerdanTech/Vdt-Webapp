# Standard Library
import pdb

# External Libraries
from litestar import Controller, Response, post, status_codes
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.auth import jwt_cookie_auth
from src.asgi.litestar.exceptions import ClientError, litestar_exception_map
from src.domain.user import UserSanitizer
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user.controllers.auth import UserAuthOpsController
from src.ops.user.schemas import auth as auth_ops_schemas
from src.ops.user.schemas.read import UserFullSchema

from .. import routes, urls


class UserAuthApiController(Controller):
    """User authentication operations controller"""

    path = urls.USER_AUTH_CONTROLLER_BASE
    tags = ["users"]

    @post(
        path=urls.USER_LOGIN_URL,
        name=routes.USER_LOGIN_NAME,
        opt={"exclude_from_auth": True},
        summary="User login",
        description="Authenticate the request with JWT cookie authentication.",
        response_description="The authenticated user schema",
        operation_id=routes.USER_LOGIN_NAME,
    )
    async def user_login(
        self,
        data: auth_ops_schemas.UserLoginInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[UserFullSchema]:
        """
        Uses the application operation and Litestar's built in JWT auth to log
        the user in with a JWT cookie authentication scheme.

        Args:
            data (schemas.UserLoginInput): input DTO.
            state (State): litestar application state.
            svcs_container (Container): svcs service container.

        Returns:
            Response[UserFullSchema]: a response containing JWT authenticated User schema.
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
            raise ClientError(status_code=status_codes.HTTP_401_UNAUTHORIZED)
        else:
            return jwt_cookie_auth.login(
                identifier=str(user.id), response_body=UserFullSchema.from_model(user)
            )
