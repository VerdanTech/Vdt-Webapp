from src.verdantech_api.domain.models.common.entities import RootEntity
from src.verdantech_api.domain.models.user.entities import User

from ..generic import BaseRepository


class UserMongoRepository(BaseRepository[User]):
    entity = User

    async def add_user(self, entity: RootEntity) -> RootEntity:
        ...
