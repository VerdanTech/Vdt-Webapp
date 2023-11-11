from typing import Any, Dict, Generic, Protocol, TypeVar

from src.domain.common.entities import RootEntityT

DatabaseModelT = TypeVar("DatabaseModelT")


class AbstractMapper(Protocol, Generic[RootEntityT]):
    """Interface for python object -> database representation functionality.
    We only expect RootEntitys because they are supposed to define
    "consistency boundaries" in our domain logic. This concept maps
    well to database transactions, and so there is one mapper
    (and one repository) for each RootEntity.
    """

    entity: RootEntityT
    model: DatabaseModelT

    @classmethod
    def to_model(entity: RootEntityT) -> DatabaseModelT:
        """Given a root entity, map into a database representation.

        Args:
            entity (RootEntity): the entity to map

        Returns:
            DatabaseModelT: the resultant database representation
        """
        ...

    @classmethod
    def from_model(model: DatabaseModelT) -> RootEntityT:
        """Given a database representation, map into python object

        Args:
            DatabaseModelT: the database representation to map

        Returns:
            RootEntityT: the resultant pythonobject
        """
        ...
