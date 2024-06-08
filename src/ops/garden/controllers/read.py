# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.user import User
from src.interfaces.persistence.garden.garden import AbstractGardenRepository


class GardenReadOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        self.garden_repo = garden_repo

    """
    async def get_by_keys(
        self, client: User, garden_key: list[str]
    ) -> list[GardenFullSchema]:
        gardens = await self.garden_repo.get_gardens_by_keys(
            ids=user_ids, return_first_none=True
        )
        if users is None:
            raise
        user_schemas = [UserPublicSchema.from_model(user) for user in users]
        return user_schemas
    """
