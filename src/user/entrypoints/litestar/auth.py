# External Libraries
from litestar import Controller, Response, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src import exceptions
from src.common.entrypoints.litestar.auth import jwt_auth
from src.user.ops import queries


class UserAuthController(Controller):
    """
    User auth ASGI controller.
    """

    path = "auth"
    tags = ["users"]

    @post(
        path="login",
        opt={"exclude_from_auth": True},
        summary="User login",
        description="Authenticate the request with JWT cookie authentication.",
        operation_id="UserLoginCommandOp",
    )
    async def user_login(
        self,
        data: queries.UserPasswordVerificationQuery,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
        """
        Uses the application query and Litestar's built in JWT auth to log
        the user in with a JWT cookie authentication scheme.

        Args:
            data (UserPasswordVerificationQuery): input query.
            state (State): litestar application state.
            svcs_container (Container): service container.

        Returns:
            Response[None]: a response containing the success code.
        """
        svcs_container.register_local_value(State, state)
        verification_result = await queries.verify_password(
            query=data, svcs_container=svcs_container
        )
        if verification_result.verified is True:
            return jwt_auth.login(
                identifier=str(verification_result.user_id),
                response_body="Authentication successful",
            )
        else:
            raise exceptions.AuthenticationError()
