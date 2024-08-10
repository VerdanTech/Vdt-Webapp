# Standard Library
import uuid

# VerdanTech Source
from src.garden.domain import Garden
from src.garden.interfaces.repository import AbstractGardenRepository

from .base_repo_mock import MockBaseRepository


class MockGardenRepository(MockBaseRepository[Garden], AbstractGardenRepository):
    """Implementation of a mock garden repository for testing"""

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
        for garden in self.collection:
            if garden.id == id:
                return garden
        return None

    async def get_by_key(self, key: str) -> Garden | None:
        """
        Given a garden key return the garden to whom it belongs.

        Args:
            key (str): the key to search for.

        Returns:
            Garden | None: the found garden, or None if no
                garden was found.
        """
        for garden in self.collection:
            if garden.key == key:
                return garden
        return None

    async def key_exists(self, key: str) -> bool:
        """
        Given a garden key, return True if a matching garden exists.
        Comparison should be case insensitive.

        Args:
            key (str): the key to check existence of.

        Returns:
            bool: the result of the existence check.
        """
        for garden in self.collection:
            if garden.key.lower() == key.lower():
                return True
        return False
