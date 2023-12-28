# Standard Library
from typing import Any, Protocol, Type

# VerdanTech Source
from src.domain.common import RootEntity

from .exceptions import InterfaceRepositoryError


class AbstractRepository[T: RootEntity](Protocol):
    """
    A Repository is an interface between the domain layer
    and the database layer.

    T: a Repository is characterized by one
        type of RootEntity. As RootEntitys are defined as entities
        which compose transactional and consistency boundaries,
        they are the objects that get persisted through interaction
        with the Repository.

    Protocol: (https://peps.python.org/pep-0544/)
    """

    entity: Type[T]

    async def async_dynamic_call(
        self,
        method_name: str,
        bypass_validation: bool = False,
        **kwargs,
    ) -> Any:
        """
        Calls the method on the repository given the method name
        and keyword arguments. Used to configure unique Specs.

        Args:
            method_name (str): name of the method to call.
            bypass_validation (bool): whether to call
                self.validate_async_dynamic_call_signature.
                Used when the arguments have been pre-validated.
            **kwargs: the arguments to the method.

        Returns:
            Any: the result of the method.
        """
        ...

    def validate_async_dynamic_call_signature(self, method_name: str, **kwargs) -> None:
        """
        Validates that an async method with the given name exists on the repository
        and that it accepts the specified keyword arguments.

        Args:
            method_name (str): The name of the method to validate.
            **kwargs: The dictionary of keyword arguments
                that the method is expected to accept.

        Raises:
            InterfaceRepositoryError: If the method does not exist, is not an async method,
            or does not accept the specified keyword arguments.
        """
        ...
