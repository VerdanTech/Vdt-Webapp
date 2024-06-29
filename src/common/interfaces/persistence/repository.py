from __future__ import annotations

# Standard Library
from typing import Protocol

# VerdanTech Source
from src.common.domain import RootEntity


class AbstractRepository[RootEntityT: RootEntity](Protocol):
    """
    A Repository is an interface between the domain layer
    and the database layer.

    T: a Repository is characterized by one
        type of RootEntity. As RootEntitys are defined as entities
        which compose transactional and consistency boundaries,
        they are the objects that get persisted through interaction
        with the Repository.

    Protocol: (https://peps.python.org/pep-0544/)
    """

    touched_entities: list[RootEntityT]
    """Tracks the entities which have been affected so that new events may be caught."""

    async def add(self, entity: RootEntityT) -> RootEntityT:
        """
        Persist a new entity to the repository.

        Args:
            entity (RootEntityT): the entity to add.

        Returns:
            RootEntityT: the entity after persistence.
        """
        self.touched_entities.append(entity)
        return await self._add(entity)

    async def update(self, entity: RootEntityT) -> RootEntityT:
        """
        Update an existing entity to the repository.

        Args:
            entity (RootEntityT): the entity to update.

        Returns:
            RootEntityT: the entity after persistence.
        """
        self.touched_entities.append(entity)
        return await self._update(entity)

    async def delete(self, entity: RootEntityT) -> None:
        """
        Delete an existing entity from a repository.

        Args:
            entity (RootEntityT): the entity to delete.
        """
        self.touched_entities.append(entity)
        return await self._delete(entity)

    async def _add(self, entity: RootEntityT) -> RootEntityT:
        """
        Persist a new entity to the repository.

        Args:
            entity (RootEntityT): the entity to add.

        Returns:
            RootEntityT: the entity after persistence.
        """
        ...

    async def _update(self, entity: RootEntityT) -> RootEntityT:
        """
        Update an existing entity to the repository.

        Args:
            entity (RootEntityT): the entity to update.

        Returns:
            RootEntityT: the entity after persistence.
        """
        ...

    async def _delete(self, entity: RootEntityT) -> None:
        """
        Delete an existing entity from a repository.

        Args:
            entity (RootEntityT): the entity to delete.
        """
        ...
