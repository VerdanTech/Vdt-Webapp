# Standard Library
import uuid
from typing import Protocol

# VerdanTech Source
from src.common.interfaces.persistence import AbstractRepository
from src.garden.domain import Garden


class AbstractGardenRepository(AbstractRepository[Garden], Protocol):
    """Data persistence interface for the Garden domain model"""

    # ======================================
    # General methods
    # ======================================

    async def get_by_id(self, id: uuid.UUID) -> Garden | None:
        """
        Given an ID return the garden to whom it belongs.

        Args:
            id (uuid.UUID): the id to search for.

        Returns:
            Garden | None: the found garden, or None if no
                garden was found.
        """
        ...

    async def get_by_name(self, name: str) -> Garden | None:
        """
        Given a garden name return the garden to whom it belongs.

        Args:
            name (str): the name to search for.

        Returns:
            Garden | None: the found garden, or None if no
                garden was found.
        """
        ...

    async def get_by_key(self, key: str) -> Garden | None:
        """
        Given a garden key return the garden to whom it belongs.

        Args:
            key (str): the key to search for.

        Returns:
            Garden | None: the found garden, or None if no
                garden was found.
        """
        ...

    async def key_exists(self, key: str) -> bool:
        """
        Given a garden key, return True if a matching garden exists.

        Args:
            key (str): the key to check existence of.

        Returns:
            bool: the result of the existence check.
        """
        ...
