from typing import Any, Dict, Generic

from serpyco import Serializer as SerpycoSerializer
from src.verdantech_api.domain.models.common.entities import RootEntityT


class BaseSerpycoMapper(Generic[RootEntityT]):
    """Implementation of a dict mapper interface using serpyco.
    Serpyco is a favoured library due to its speed and
    design for dataclasses. Currently, no serialization
    specific schema is required because serpyco inspects
    dataclass fields itself, but if the serpyco validation
    logic to be used, serializer specific objects and logic
    for conversion between them and domain objects may
    be required, as mapper specific implementation
    details can't be included in the domain layer.
    """

    entity: RootEntityT
    model: Dict[str, Any]
    serializer: SerpycoSerializer

    @classmethod
    def to_model(cls, entity: RootEntityT) -> Dict[str, Any]:
        """Given a root entity, map into dictionary.

        Args:
            entity (RootEntity): the entity to serialize

        Returns:
            Dict[str, Any]: the resultant python dict
        """
        entity = cls._pre_to_dict(entity)
        return cls.serializer.dump(entity)

    @classmethod
    def from_model(cls, dict: Dict[str, Any]) -> RootEntityT:
        """Given a dict, map into python object

        Args:
            dict (Dict[str, Any]): the dict to deserialize

        Returns:
            RootEntityT: the resultant object
        """
        dict = cls._pre_from_dict(dict)
        return cls.serializer.load(dict)

    def _pre_to_model(cls, entity: RootEntityT) -> RootEntityT:
        """Pre-process the entity to be serialized. Call the
            object sanitizer attached to the serializer instance.

        Args:
            entity (RootEntityT): entity to be serialized

        Returns:
            RootEntityT: the entity after pre-processing
        """
        return entity

    def _pre_from_model(cls, dict: Dict[str, Any]) -> Dict[str, Any]:
        """Pre-process the dict to be deserialized.

        Args:
            dict (Dict[str, Any]): the dict to be deserialized

        Returns:
            Dict[str, Any]: the dict after pre-processing
        """
        return dict
