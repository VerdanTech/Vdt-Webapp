# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.user import User
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.ops.user.schemas.read import UserFullSchema, UserPublicSchema


class UserReadOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def profiles(
        self, client: User, user_ids: Optional[list[EntityIdType]]
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
        if user_ids is None:
            user_schema = UserFullSchema.from_model(client)
            return user_schema
        else:
            users = await self.user_repo.get_users_by_ids(
                ids=user_ids, return_first_none=True
            )
            if users is None:
                raise
            user_schemas = [UserPublicSchema.from_model(user) for user in users]
            return user_schemas
