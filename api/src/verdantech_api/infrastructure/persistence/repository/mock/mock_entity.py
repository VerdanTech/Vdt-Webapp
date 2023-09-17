from typing import List

from src.verdantech_api.domain.models.common.entities import MockEntity

from .generic import MockBaseRepository


class MockEntityRepository(MockBaseRepository[MockEntity]):
    """Implementation of mock repository for mock entity object for testing"""

    entity = MockEntity

    async def add_many(self, mock_entities: List[MockEntity]) -> List[MockEntity]:
        """Add multiple mock entities to the repository

        Args:
            entities (List[MockEntity]): list of entities to add

        Returns:
            List[MockEntity]: the resultant entities after persistence
        """
        return self._add_many(mock_entities)

    async def str_field_exists(self, str_field: str) -> bool:
        """Check the existence of a str_field in the repository

        Args:
            str_field (str): the str_field to check uniqueness of

        Returns:
            bool: true if the str_field exists
        """
        for entity in self.collection:
            if entity.str_field == str_field:
                return True
        return False
