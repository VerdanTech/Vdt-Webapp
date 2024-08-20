# External Libraries
from litestar.connection import ASGIConnection
from litestar.middleware import AbstractAuthenticationMiddleware, AuthenticationResult
from litestar.middleware.base import DefineMiddleware
from sqlalchemy import select

# VerdanTech Source
from src.common.adapters.persistence.common.uow import (
    sessionmaker as alchemy_sessionmaker,
)
from src.common.adapters.persistence.sqlalchemy import get_alchemy_client
from src.user.adapters.sqlalchemy.mapper import user_email_table, user_table
from src.user.domain import User

from .token import decode_jwt_token

API_KEY_HEADER = "X-API-KEY"


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

        # retrieve the auth header
        auth_header = connection.headers.get(API_KEY_HEADER)
        if not auth_header:
            return AuthenticationResult(None, None)

        # decode the token, the result is a ``Token`` model instance
        token = decode_jwt_token(encoded_token=auth_header)

        alchemy_client = await get_alchemy_client(state=connection.state)
        alchemy_session = alchemy_sessionmaker(bind=alchemy_client.engine)

        async with alchemy_session.begin():
            statement = (
                select(User).join(user_email_table).filter(user_table.c.id == token.sub)
            )
            query = await alchemy_session.execute(statement)
            user = query.unique().scalar_one_or_none()

        if user:
            return AuthenticationResult(user=user, auth=token)
        else:
            return AuthenticationResult(None, None)


default_auth_mw = DefineMiddleware(DefaultJwtAuthenticationMiddleware)
