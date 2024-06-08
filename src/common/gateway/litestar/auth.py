# Standard Library
from typing import Any, Optional

# External Libraries
from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTCookieAuth, Token
from sqlalchemy import select
from sqlalchemy.orm import joinedload

# VerdanTech Source
from src import settings
from src.common.adapters.persistence.sqlalchemy import (
    get_alchemy_client,
)
from src.common.adapters.persistence.sqlalchemy.uow import AlchemyUow
from src.user.adapters.sqlalchemy.mapper import UserAlchemyModel
from src.user.domain import User


async def retrieve_user_handler(
    token: "Token", connection: "ASGIConnection[Any, Any, Any, Any]"
) -> Optional[User]:
    alchemy_client = await get_alchemy_client(state=connection.state)
    uow = AlchemyUow(client=alchemy_client)
    async with uow:
        statement = (
            select(UserAlchemyModel)
            .options(joinedload(UserAlchemyModel.emails))
            .filter(UserAlchemyModel.id == int(token.sub))
        )
        query = await uow.session.execute(statement)
        user_model = query.unique().scalar_one_or_none()

    if user_model is None:
        return None

    # TODO
    #return UserAlchemyMapper.from_model(user_model)
    return None


jwt_cookie_auth = JWTCookieAuth[User](
    token_secret=settings.JWT_SECRET,
    retrieve_user_handler=retrieve_user_handler,
    exclude=["schema/"],
)

