# External Libraries
from litestar import Controller, Request, Response, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src import exceptions
from src.common.entrypoints.litestar.auth import (
    TokenTypeEnum,
    access_token_to_cookie,
    decode_refresh_token,
    encode_access_token,
    encode_refresh_token,
    refresh_token_to_cookie, get_user_by_token
)
from src.user.ops import queries
from src.common.ops.queries import QueryResult, query_result_transform
from src import settings

@query_result_transform
class AccessInfoResult(QueryResult[None]):
    """
    Communicates information to the client regarding
    the access they have been granted via access token.

    Attributes:
        expiry_time_seconds (float): the number of seconds until
            the access expires and must be refreshed.
    """
    expiry_time_seconds: float

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
    ) -> Response[AccessInfoResult]:
        """
        Uses the application query and Litestar's built in JWT auth to log
        the user in with a JWT cookie authentication scheme.

        Args:
            data (UserPasswordVerificationQuery): input query.
            state (State): litestar application state.
            svcs_container (Container): service container.

        Returns:
            Response[AccessInfoResult]: a response containing the access
                information, including expiry time.
        """
        svcs_container.register_local_value(State, state)
        verification_result = await queries.verify_password(
            query=data, svcs_container=svcs_container
        )
        if verification_result.verified is True and verification_result.user_id:
            encoded_access_token = encode_access_token(verification_result.user_id)
            encoded_refresh_token = encode_refresh_token(verification_result.user_id)

            return Response(
                content=AccessInfoResult(expiry_time_seconds=settings.ACCESS_JWT_EXPIRY_TIMEDELTA.total_seconds()),
                cookies=[
                    refresh_token_to_cookie(encoded_refresh_token),
                    access_token_to_cookie(encoded_access_token),
                ],
            )
        else:
            raise exceptions.AuthenticationError()

    @post(
        path="refresh",
        summary="User authentication refresh",
        description="Refresh the authentication process for security..",
        operation_id="UserRefreshCommandOp",
    )
    async def user_refresh(
        self,
        state: State,
        request: Request,
    ) -> Response[AccessInfoResult]:
        """
        Retrieves the current auth info, and if valid exchanges the access
        and refresh tokens for new ones.

        Args:
            state (State): litestar application state.
            svcs_container (Container): service container.

        Returns(:
            Response[AccessInfoResult]: a response containing the access
                information, including expiry time.
        """
        # Retrieve the refresh token from the cookie.
        encoded_refresh_token = request.cookies[str(TokenTypeEnum.REFRESH)]
        if encoded_refresh_token is None:
            raise exceptions.AuthenticationError()

        # Decode the token, the result is a Token model instance
        refresh_token = decode_refresh_token(encoded_token=encoded_refresh_token)

        # Retrieve the user the token represents.
        user = await get_user_by_token(token=refresh_token, state=state)
        if user is None:
            raise exceptions.AuthenticationError()
        
        # Validate token
        # TODO: When a token denylist is added, check that here
        # Also add the used token to the denylist
        # Eventually, add a logout endpoint to do this as well

        # Issue new tokens
        encoded_access_token = encode_access_token(user.id_or_error())
        encoded_refresh_token = encode_refresh_token(user.id_or_error())

        return Response(
            content=AccessInfoResult(expiry_time_seconds=settings.ACCESS_JWT_EXPIRY_TIMEDELTA.total_seconds()),
            cookies=[
                refresh_token_to_cookie(encoded_refresh_token),
                access_token_to_cookie(encoded_access_token),
            ],
        )