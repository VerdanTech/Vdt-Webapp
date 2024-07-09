# Standard Library
import uuid
from typing import Any

# External Libraries
from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTCookieAuth, Token
from sqlalchemy import select

# VerdanTech Source
from src import settings
from src.common.adapters.persistence.common.uow import (
    sessionmaker as alchemy_sessionmaker,
)
from src.common.adapters.persistence.sqlalchemy import get_alchemy_client
from src.user.adapters.sqlalchemy.mapper import user_email_table, user_table
from src.user.domain import User


async def retrieve_user_handler(
    token: "Token", connection: "ASGIConnection[Any, Any, Any, Any]"
) -> User | None:
    """
    Retrieves a user from the database based on the token.

    Used by Litestar to supply an authenticated user object to the ops layer.

    Args:
        token (Token):
        connection (ASGIConnection[Any, Any, Any, Any]): _description_

    Returns:
        User | None: the user, if one matching the token was found.
    """
    alchemy_client = await get_alchemy_client(state=connection.state)
    alchemy_session = alchemy_sessionmaker(bind=alchemy_client.engine)
    async with alchemy_session.begin():
        statement = (
            select(User)
            .join(user_email_table)
            .filter(user_table.c.id == uuid.UUID(token.sub))
        )
        query = await alchemy_session.execute(statement)
        user = query.unique().scalar_one_or_none()

    if user is None:
        return None

    return user


jwt_cookie_auth = JWTCookieAuth[User](
    token_secret=settings.JWT_SECRET,
    retrieve_user_handler=retrieve_user_handler,
    exclude=["/schema"],
)
