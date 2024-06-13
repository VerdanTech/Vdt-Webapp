# External Libraries
from attr import define

# VerdanTech Source
from src.common.interfaces.persistence.uow import (
    AbstractRepositoryContainer,
    AbstractUow,
)

from .user_mock import MockUserRepository


@define
class MockRepositoryContainer(AbstractRepositoryContainer):
    users: MockUserRepository

    @classmethod
    def enter_uow(cls) -> "MockRepositoryContainer":
        return MockRepositoryContainer(users=MockUserRepository())


class MockUow(AbstractUow):
    async def __aenter__(self):
        # Initialize repos
        self.repos = MockRepositoryContainer.enter_uow()

        return await super().__aenter__()

    async def _commit(self) -> None:
        """
        Commits all changes to the database.
        """
        pass

    async def rollback(self) -> None:
        """
        Discards all changes to the database.
        """
        pass
