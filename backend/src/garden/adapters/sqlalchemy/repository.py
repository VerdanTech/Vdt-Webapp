# Standard Library
import uuid

# External Libraries
from sqlalchemy import func, select

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy.repository import BaseAlchemyRepository
from src.garden.domain.models import Garden
from src.garden.interfaces.repository import AbstractGardenRepository

from .mapper import garden_table

# from .mapper import garden_table, garden_membership_table


class GardenAlchemyRepository(BaseAlchemyRepository[Garden], AbstractGardenRepository):
    """SQLAlchemy implementation of garden repository"""

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
        statement = select(Garden).filter(garden_table.c.id == id)
        query = await self.session.execute(statement)
        garden = query.unique().scalar_one_or_none()
        return garden

    async def get_by_key(self, key: str) -> Garden | None:
        """
        Given a garden key return the garden to whom it belongs.

        Args:
            key (str): the key to search for.

        Returns:
            Garden | None: the found garden, or None if no
                garden was found.
        """
        statement = select(Garden).filter(garden_table.c.key == key)
        query = await self.session.execute(statement)
        garden = query.unique().scalar_one_or_none()
        return garden

    async def key_exists(self, key: str) -> bool:
        """
        Given a garden key, return True if a matching garden exists.
        Comparison should be case insensitive.

        Args:
            key (str): the key to check existence of.

        Returns:
            bool: the result of the existence check.
        """
        statement = select(Garden).filter(
            func.lower(garden_table.c.key) == func.lower(key)
        )
        query = await self.session.execute(statement)
        garden = query.scalar_one_or_none()

        return garden is not None

    # ======================================
    # Query-only methods
    # ======================================
