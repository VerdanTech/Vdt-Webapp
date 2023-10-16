from typing import Any, Dict, Generic, Protocol

from src.domain.common.entities import RootEntityT


class AbstractAsyncRepository(Generic[RootEntityT], Protocol):
    """Base interface of repository for domain model persistence"""

    entity: RootEntityT

    async def async_dynamic_call(
        self, method_name: str, **kwargs: Dict[str, Any]
    ) -> Any:
        """Calls the method on the repository given the method name.
            Used to configure unique sanitizations

        Args:
            method_name (str): name of the method to call
            kwargs (Dict[str, Any]): passed to the method

        Raises:
            AttributeError: raised if method does not exist
            TypeError: raised if method is not a callable
            TypeError: raised if method is not async

        Returns:
            Any: the result of the method
        """
        ...
