# Standard Library
from typing import Any, Optional

# External Libraries
from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTCookieAuth, Token
from sqlalchemy import select
from sqlalchemy.orm import joinedload

# VerdanTech Source
from src import settings
from src.adapters.persistence.sqlalchemy.litestar_lifespan import (
    get_alchemy_client,
    get_alchemy_transaction,
)
from src.adapters.persistence.sqlalchemy.mapper.user import UserAlchemyMapper
from src.adapters.persistence.sqlalchemy.mapper.user.user import UserAlchemyModel
from src.domain.user import User

from .user import urls as user_urls


async def retrieve_user_handler(
    token: "Token", connection: "ASGIConnection[Any, Any, Any, Any]"
) -> Optional[User]:
    alchemy_client = await get_alchemy_client(state=connection.state)
    async with get_alchemy_transaction(client=alchemy_client) as transaction:
        statement = (
            select(UserAlchemyModel)
            .options(joinedload(UserAlchemyModel.emails))
            .filter(UserAlchemyModel.id == int(token.sub))
        )
        query = await transaction.execute(statement)
        user_model = query.unique().scalar_one_or_none()

    if user_model is None:
        return None

    return UserAlchemyMapper.from_model(user_model)


jwt_cookie_auth = JWTCookieAuth[User](
    token_secret=settings.JWT_SECRET,
    retrieve_user_handler=retrieve_user_handler,
    exclude=["schema/"],
)
