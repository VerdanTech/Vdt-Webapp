from src.verdantech_api.domain.models.user.entities import User

from ..exceptions import alchemy_exception_map
from ..generic import BaseAlchemyRepository


class UserAlchemyRepository(BaseAlchemyRepository[User]):
    """SQLAlchemy implementation of user repository"""

    entity = User

    async def add(self, user: User) -> User:
        """Persist a new user object to the repository

        Args:
            user (User): the user object to add

        Returns:
            User: the resultant persisted user object
        """
        with alchemy_exception_map:
            user_model = self._entity_to_model(user)
            user_model = self.transaction.add(user_model)
            await self.transaction.flush()
            await self.transaction.expunge(user_model)
            user = self._model_to_entity(user_model)
            return user
