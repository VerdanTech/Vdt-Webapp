import inspect
from typing import Any, Dict, Generic, Optional

from src.domain.common.entities import RootEntityT
from src.utils.sanitizers.object import ObjectSanitizer

from ..mapper.generic import AbstractMapper, DatabaseModelT


class BaseRepository(Generic[RootEntityT]):
    """Base implementation of interface for domain model persistence"""

    entity: RootEntityT

    def __init__(
        self,
        mapper: Optional[AbstractMapper] = None,
    ) -> None:
        if mapper:
            self.mapper = mapper

    async def async_dynamic_call(
        self, method_name: str, **kwargs: Dict[str, Any]
    ) -> Any:
        """Calls the method on the repository given the method name.
            Used to configure unique sanitizations

        Args:
            method_name (str): name of the method to call

        Raises:
            AttributeError: raised if method does not exist
            TypeError: raised if method is not a callable
            TypeError: raised if method is not async

        Returns:
            Any: the result of the method
        """

        # Retrieve attribute from repository object
        method = getattr(self, method_name, None)

        # Guard against method not found
        if method is None:
            raise AttributeError(
                f"The method {method_name} does not exist on {type(self).__name__}"
            )

        # Guard against attribute not being a method
        if not callable(method):
            raise TypeError(f"{method_name} on {type(self).__name__} is not callable")

        # Guard against attribute not being an async method
        if not inspect.iscoroutinefunction(method):
            raise TypeError(
                f"{method_name} on {type(self).__name__} is not an async function"
            )

        return await method(**kwargs)
