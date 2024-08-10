# Standard Library
from typing import TYPE_CHECKING

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.common.interfaces.persistence.repository import AbstractRepository

if TYPE_CHECKING:
    # VerdanTech Source
    from src.common.domain import RootEntity


class BaseAlchemyRepository[RootEntityT: RootEntity](AbstractRepository[RootEntityT]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _add(self, entity: RootEntityT) -> RootEntityT:
        """
        Persist a new entity to the repository.

        Args:
            entity (RootEntityT): the entity to add.

        Returns:
            RootEntityT: the entity after persistence.
        """
        self.session.add(entity)
        return entity

    async def _update(self, entity: RootEntityT) -> RootEntityT:
        """
        Update an existing entity to the repository.

        Args:
            entity (RootEntityT): the entity to update.

        Returns:
            RootEntityT: the entity after persistence.
        """
        entity = await self.session.merge(entity)
        return entity

    async def _delete(self, entity: RootEntityT) -> None:
        """
        Delete an existing entity from a repository.

        Args:
            entity (RootEntityT): the entity to delete.
        """
        await self.session.delete(entity)
