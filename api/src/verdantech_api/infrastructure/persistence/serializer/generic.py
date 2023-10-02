from typing import Any, Dict, Generic, Protocol

from src.verdantech_api.domain.models.common.entities import RootEntityT


class AbstractSerializer(Protocol, Generic[RootEntityT]):
    """Interface for python object -> dict serialization functionality.
    We only expect RootEntitys because they are supposed to define
    "consistency boundaries" in our domain logic. This concept maps
    well to collections in a db, and so there is one serialzer
    (and one repository) for each RootEntity.
    """

    entity: RootEntityT

    def to_dict(entity: RootEntityT) -> Dict[str, Any]:
        """Given a root entity, serialize into dictionary.

        Args:
            entity (RootEntity): the entity to serialize

        Returns:
            Dict[str, Any]: the resultant python dict
        """
        ...

    def from_dict(dict: Dict[str, Any]) -> RootEntityT:
        """Given a dict, deserialize into python object

        Args:
            dict (Dict[str, Any]): the dict to deserialize

        Returns:
            RootEntityT: the resultant object
        """
        ...
