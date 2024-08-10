# Standard Library
import uuid
from typing import Callable, List

# VerdanTech Source
from src.common.domain import Entity, RootEntity
from src.common.interfaces.persistence.exceptions import (
    ObjectAlreadyExists,
    ObjectNotFound,
)
from src.common.interfaces.persistence.repository import AbstractRepository


class MockBaseRepository[T: RootEntity](AbstractRepository[T]):

    """Base implementation of a mock, in-memory repository for testing"""

    def __init__(self, id_factory: Callable[[], uuid.UUID] = uuid.uuid4) -> None:
        self.id_factory = id_factory
        self.collection = []

    def _generate_entity_id(self, entity: Entity) -> None:
        """Generate an ID for an entity given an ID factory set
            on the repository upon instantiation

        Args:
            entity (Entity): the entity to update with ID
        """
        entity.id = self.id_factory()

    async def _add(self, entity: T) -> T:
        """Add a generic entity to the repository

        Args:
            entity (RootEntity): entity to add

        Raises:
            ObjectAlreadyExists: raised if the entity already exists

        Returns:
            RootEntity: the entity added
        """
        self._generate_entity_id(entity)
        self.collection.append(entity)
        self.touched_entities.append(entity)
        return entity

    async def _add_many(self, entities: List[T]) -> List[T]:
        """Add a list of generic entities to the repository

        Args:
            entities (List[RootEntity]): entities to add

        Raises:
            ObjectAlreadyExists: raised if any of the entities already exist

        Returns:
            List[RootEntity]: entities added
        """
        persisted_entities = []

        for entity in entities:
            # Existing entity
            if entity.id is not None:
                raise ObjectAlreadyExists(
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

    async def _update(self, entity: T) -> T:
        """
        Persist an existing entity to the repository.

        Args:
            entity (T): entity to update.

        Raises:
            ObjectNotFound: raised if the entity does not exist.

        Returns:
            T: the entity after persistence.
        """
        for i, existing_entity in enumerate(self.collection):
            if existing_entity.id == entity.id:
                self.collection[i] = entity
                self.touched_entities.append(entity)
                return entity
        raise ObjectNotFound("The user does not presently exist in the repository")

    async def _delete(self, entity: T) -> None:
        """
        Delete an existing entity from the repository.

        Args:
            entity (T): entity to delete

        Raises:
            ObjectNotFound: raised if the entity does not exist.
        """
        for i, existing_entity in enumerate(self.collection):
            if existing_entity.id == entity.id:
                self.collection.pop(i)
                return
        raise ObjectNotFound("The user does not presently exist in the repository")
