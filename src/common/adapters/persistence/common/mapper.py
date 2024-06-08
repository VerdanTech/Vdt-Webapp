# Standard Library
from typing import Protocol

# VerdanTech Source
from src.common.domain import RootEntity


class AbstractMapper[RootEntityT: RootEntity, DatabaseModelT](Protocol):
    """
    Interface for python object -> database representation functionality.
    We only expect RootEntitys because they are supposed to define
    "consistency boundaries" in our domain logic. This concept maps
    well to database transactions, and so there is one mapper
    (and one repository) for each RootEntity.
    """

    @staticmethod
    def to_model(entity: RootEntityT) -> DatabaseModelT:
        """
        Given a root entity, map into a database representation.

        Args:
            entity (RootEntityT): the entity to map.

        Returns:
            DatabaseModelT: the resultant database representation.
        """
        ...

    @staticmethod
    def from_model(model: DatabaseModelT) -> RootEntity:
        """
        Given a database representation, map into a root entity.

        Args:
            DatabaseModelT: the database representation to map.

        Returns:
            RootEntity: the resultant root entity.
        """
        ...
