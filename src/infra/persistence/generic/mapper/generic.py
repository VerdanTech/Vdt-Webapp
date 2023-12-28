# Standard Library
from typing import Generic, Protocol, TypeVar

# VerdanTech Source
from src.domain.common import RootEntity

type DatabaseModelT = TypeVar("DatabaseModelT")


class AbstractMapper[T: RootEntity](Protocol):
    """
    Interface for python object -> database representation functionality.
    We only expect RootEntitys because they are supposed to define
    "consistency boundaries" in our domain logic. This concept maps
    well to database transactions, and so there is one mapper
    (and one repository) for each RootEntity.
    """

    entity: T
    model: DatabaseModelT

    @classmethod
    def to_model(entity: RootEntity) -> DatabaseModelT:
        """
        Given a root entity, map into a database representation.

        Args:
            entity (RootEntity): the entity to map.

        Returns:
            DatabaseModelT: the resultant database representation.
        """
        ...

    @classmethod
    def from_model(model: DatabaseModelT) -> RootEntity:
        """
        Given a database representation, map into a root entity.

        Args:
            DatabaseModelT: the database representation to map.

        Returns:
            RootEntity: the resultant root entity.
        """
        ...
