from functools import partial
from typing import Callable, Generic, List

from src.domain.common.entities import Entity, RootEntityT
from src.utils.key_generator import key_generator

from ..generic import BaseRepository


class MockBaseRepository(BaseRepository[RootEntityT], Generic[RootEntityT]):
    """Base implementation of a mock, in-memory repository for testing"""

    def __init__(
        self, id_factory: Callable[[], None] = partial(key_generator, length=8)
    ) -> None:
        self.id_factory = id_factory
        self.collection = []

    def _generate_entity_id(self, entity: Entity) -> None:
        """Generate an ID for an entity given an ID factory set
            on the repository upon instantiation

        Args:
            entity (Entity): the entity to update with ID
        """
        entity.id = self.id_factory()

    def _add(self, entity: RootEntityT) -> RootEntityT:
        """Add a generic entity to the repository

        Args:
            entity (RootEntityT): entity to add

        Raises:
            ValueError: raised if the entity already exists

        Returns:
            RootEntityT: the entity added
        """

        # Existing entity
        if entity.id is not None:
            raise ValueError(
                f"ID field of {str(entity)} of type {str(type(entity))} already exists"
            )

        # New entity
        self._generate_entity_id(entity)
        self.collection.append(entity)
        return entity

    def _add_many(self, entities: List[RootEntityT]) -> List[RootEntityT]:
        """Add a list of generic entities to the repository

        Args:
            entities (List[RootEntityT]): entities to add

        Raises:
            ValueError: raised if any of the entities already exist

        Returns:
            List[RootEntityT]: entities added
        """
        persisted_entities = []

        for entity in entities:
            # Existing entity
            if entity.id is not None:
                raise ValueError(
                    f"""
                    ID field of {str(entity)} of type 
                    {str(type(entity))} already exists
                    """
                )

            # New entity
            self._generate_entity_id(entity)
            persisted_entities.append(entity)

        self.collection.extend(persisted_entities)
        return persisted_entities
