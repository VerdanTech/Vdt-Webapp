# Standard Library
from typing import Protocol

# VerdanTech Source
from src.common.domain import 
from src.garden.domain.garden import Garden

from ..generic import AbstractRepository


class AbstractGardenRepository(AbstractRepository[Garden], Protocol):
    """Data persistence interface for the Garden domain model"""

    entity = Garden

    async def add(self, garden: Garden) -> Garden:
        """
        Persist a new garden entity to the repository.

        Args:
            garden (Garden): the garden entity to add.

        Returns:
            Garden: the garden entity after persistence.
        """
        ...

    async def update(self, garden: Garden) -> Garden:
        """
        Persist an existing garden entity to the repository.

        Args:
            garden (Garden): garden entity to update.

        Returns:
            Garden: the garden entity after persistence.
        """
        ...

    async def get_garden_by_key(self, key: str) -> Garden | None:
        """
        Given a garden key id, return the garden to whom it belongs.

        Args:
            key (str): the key to search for.

        Returns:
            Garden | None: the found garden, or None if no garden was found.
        """
        ...

    async def key_id_exists(self, key: str) -> bool:
        """
        Given a garden key id, return True if a matching garden exists.

        Args:
            key (str): the key to check existence of.

        Returns:
            bool: the result of the existence check.
        """
        ...
