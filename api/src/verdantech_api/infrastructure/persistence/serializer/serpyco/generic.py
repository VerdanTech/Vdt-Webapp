from typing import Any, Dict, Generic

from serpyco import Serializer as SerpycoSerializer
from src.verdantech_api.domain.models.common.entities import RootEntityT
from src.verdantech_api.domain.utils.sanitizers.object import ObjectSanitizer


class SerpycoSerializer(Generic[RootEntityT]):
    """Implementation of serializer interface using serpyco.
    Serpyco is a favoured library due to its speed and
    design for dataclasses. Currently, no serialization
    specific schema is required because serpyco inspects
    dataclass fields itself, but if another library is
    to be used, serializer specific objects and logic
    for conversion between them and domain objects may
    be required, as serializer specific implementation
    details can't be included in the domain layer.
    """

    entity: RootEntityT
    serializer: SerpycoSerializer

    def __init__(self, sanitizer: ObjectSanitizer = None):
        self.sanitizer = sanitizer

    def to_dict(self, entity: RootEntityT) -> Dict[str, Any]:
        """Given a root entity, serialize into dictionary.

        Args:
            entity (RootEntity): the entity to serialize

        Returns:
            Dict[str, Any]: the resultant python dict
        """
        entity = self._pre_to_dict(entity)
        return self.serializer.dump(entity)

    def from_dict(self, dict: Dict[str, Any]) -> RootEntityT:
        """Given a dict, deserialize into python object

        Args:
            dict (Dict[str, Any]): the dict to deserialize

        Returns:
            RootEntityT: the resultant object
        """
        dict = self._pre_from_dict(dict)
        return self.serializer.load(dict)

    def _pre_to_dict(self, entity: RootEntityT) -> RootEntityT:
        """Pre-process the entity to be serialized. Call the
            object sanitizer attached to the serializer instance.

        Args:
            entity (RootEntityT): entity to be serialized

        Returns:
            RootEntityT: the entity after pre-processing
        """
        if self.sanitizer is not None:
            try:
                self.sanitizer.sanitize_object(object=entity)
            except NotImplementedError:
                pass
        return entity

    def _pre_from_dict(self, dict: Dict[str, Any]) -> Dict[str, Any]:
        """Pre-process the dict to be deserialized.

        Args:
            dict (Dict[str, Any]): the dict to be deserialized

        Returns:
            Dict[str, Any]: the dict after pre-processing
        """
        return dict
