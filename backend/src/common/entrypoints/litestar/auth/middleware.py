# External Libraries
from litestar.connection import ASGIConnection
from litestar.middleware import AbstractAuthenticationMiddleware, AuthenticationResult
from litestar.middleware.base import DefineMiddleware

from .query import get_user_by_token
from .token import TokenTypeEnum, decode_access_token


class DefaultJwtAuthenticationMiddleware(AbstractAuthenticationMiddleware):
    async def authenticate_request(
        self, connection: ASGIConnection
    ) -> AuthenticationResult:
        """
        Given a request, parse the request api key stored in the header
        and retrieve the user correlating to the token from the DB.

        If the user does not exist, do not raise an exception. Instead,
        return the user as None in the AuthenticationResult. This allows
        routes to be open to non-authenticated users but return different
        content when authenticated users access it.
        """

        # Retrieve the access token from the cookies
        if str(TokenTypeEnum.ACCESS) not in connection.cookies:
            return AuthenticationResult(None, None)
        encoded_access_token = connection.cookies[str(TokenTypeEnum.ACCESS)]

        # Decode the token, the result is a Token model instance
        access_token = decode_access_token(encoded_token=encoded_access_token)

        # Retrieve the user the token represents.
        user = await get_user_by_token(token=access_token, state=connection.state)

        if user:
            return AuthenticationResult(user=user, auth=access_token)
        else:
            return AuthenticationResult(None, None)


default_auth_mw = DefineMiddleware(DefaultJwtAuthenticationMiddleware)
