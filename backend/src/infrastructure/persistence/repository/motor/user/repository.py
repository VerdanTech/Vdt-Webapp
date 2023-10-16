from motor.motor_asyncio import AsyncIOMotorCollection
from src.domain.common.entities import RootEntity
from src.domain.user.entities import User

from ..exceptions import motor_exception_map
from ..generic import BaseMotorRepository


class UserMotorRepository(BaseMotorRepository[User]):
    """Mongo motor implementation of user repository"""

    entity = User

    async def add(self, user: User) -> User:
        """Persist a new user object to the repository

        Args:
            user (User): the user object to add

        Returns:
            User: the resultant persisted user object
        """
        with motor_exception_map:
            user_dict = self.serializer.to_dict(user)
            user_dict = await self.collection.insert_one(user_dict)
            user = self.serializer.from_dict(user_dict)
            return user
