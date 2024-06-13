from __future__ import annotations

# Standard Library
from typing import TYPE_CHECKING, Generator, Protocol

# VerdanTech Source
from src.common.domain import Event
from src.common.domain.models import RootEntity

if TYPE_CHECKING:
    # VerdanTech Source
    from src.user.interfaces import AbstractUserRepository


class AbstractRepositoryContainer(Protocol):
    users: AbstractUserRepository

    @classmethod
    def enter_uow(cls) -> AbstractRepositoryContainer:
        ...

    @property
    def touched_entities(self) -> Generator[RootEntity, None, None]:
        """
        Returns all entities that have been touched by
        any repository.

        Yields:
            RootEntity: all touched entities.
        """
        for user in self.users.touched_entities:
            yield user


class AbstractUow(Protocol):
    """
    A Unit Of Work (UoW) is a context manager for commiting and rolling back
    database operations.

    It encapsulates all repositories for conveinence.
    """

    repos: AbstractRepositoryContainer

    async def __aenter__(self) -> AbstractUow:
        return self

    async def __aexit__(self, *args) -> None:
        await self.rollback()

    async def commit(self) -> None:
        """
        Commits all changes to the database.
        """
        await self._commit()

    def collect_new_events(self) -> Generator[Event, None, None]:
        """
        Yields all unhandled events on the entities which were touched during the operation.

        Yields:
            Generator[Event, None, None]: all new events.
        """
        for entity in self.repos.touched_entities:
            while entity.events:
                yield entity.events.pop(0)

    async def _commit(self) -> None:
        """
        Commits all changes to the database.
        """
        ...

    async def rollback(self) -> None:
        """
        Discards all changes to the database.
        """
        ...
