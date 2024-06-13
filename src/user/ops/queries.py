# Standard Library
import uuid
from datetime import datetime
from typing import Optional

# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.domain import EntityIdType
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.ops.processors import asgi_processor
from src.common.ops.queries import (
    Query,
    QueryResult,
    query_result_transform,
    query_transform,
)
from src.user.domain import User

"""
Note: The UUID class is used directly instead of the EntityIdType alias
because Litestar schema generation currently types it as Any. 
"""


@query_result_transform
class EmailSchema(QueryResult):
    """Schema for returning a detailed representation of an Email."""

    address: str
    primary: bool
    verified: bool


@query_result_transform
class UserFullSchema(QueryResult):
    """
    Schema for returning a detailed representation of a User
    to that User.
    """

    id: uuid.UUID
    username: str
    emails: list[EmailSchema]
    is_superuser: bool
    created_at: datetime | None


@query_result_transform
class UserPublicSchema(QueryResult):
    """
    Schema for returning a detailed representation of a User,
    to other Users.
    """

    id: uuid.UUID
    username: str


@query_transform
class ProfilesQuery(Query):
    user_ids: Optional[list[EntityIdType]]


@asgi_processor.add_query()
async def profiles(
    self,
    query: ProfilesQuery,
    svcs_container: Container,
    client: User | None = None,
) -> list[UserPublicSchema] | UserFullSchema:
    """
    Returns the client's full profile or a list of public profiles
    if a list of IDs is given.

    Args:
        client (User): the client user.
        user_ids (Optional[list[EntityIdType]]): an optional list of
            user profiles to retrieve.

    Returns:
        list[UserPublicSchema] | UserFullSchema: the full schema of the client
            or the public schemas of the requested IDs.
    """
    if query.user_ids is None:
        user_schema = UserFullSchema.from_model(client)
        return user_schema

    else:
        # Locate services
        uow = await svcs_container.aget_abstract(AbstractUow)

        async with uow:
            users = await self.user_repo.get_users_by_ids(ids=query.user_ids)
            if users is None:
                raise
            user_schemas = [UserPublicSchema.from_model(user) for user in users]
            return user_schemas
