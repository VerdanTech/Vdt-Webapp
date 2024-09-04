# External Libraries
from litestar.datastructures import State
from sqlalchemy import select

# VerdanTech Source
from src.common.adapters.persistence.common.uow import (
    sessionmaker as alchemy_sessionmaker,
)
from src.common.adapters.persistence.sqlalchemy import get_alchemy_client
from src.user.adapters.sqlalchemy.mapper import user_table
from src.user.domain import User

from .token import Token


async def get_user_by_token(token: Token, state: State) -> User | None:
    """
    Given a jwt token, retrieves the user it represents.

    Args:
        token (Token): the token containing the user's ID.
        state (State): Litestar global state.

    Returns:
        User | None: the user, or none if no user was found.
    """
    alchemy_client = await get_alchemy_client(state=state)
    alchemy_session = alchemy_sessionmaker(bind=alchemy_client.engine)

    async with alchemy_session.begin():
        statement = select(User).filter(user_table.c.id == token.sub)
        query = await alchemy_session.execute(statement)
        user = query.unique().scalar_one_or_none()
    return user
