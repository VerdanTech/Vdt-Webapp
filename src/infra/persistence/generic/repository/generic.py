# Standard Library
import inspect
from typing import Any, Type

# VerdanTech Source
from src.domain.common import RootEntity
from src.interfaces.persistence import exceptions
from src.interfaces.persistence.generic import AbstractRepository


class BaseRepository[T: RootEntity](AbstractRepository):
    """
    A Repository is an interface between the domain layer
    and the database layer.

    Base implementation of a Repository including dynamic call functionality.
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

        if not bypass_validation:
            self.validate_async_dynamic_call_signature(
                method_name=method_name, **kwargs
            )

        # Retrieve attribute from repository object
        if not hasattr(self, method_name):
            raise ValueError("Invalid call signature")
        method = getattr(self, method_name)

        return await method(**kwargs)

    def validate_async_dynamic_call_signature(self, method_name: str, **kwargs) -> None:
        """
        Validates that an async method with the given name exists on the repository
        and that the supplied kwargs matches the method's signature.

        Args:
            method_name (str): the name of the method to validate against.
            **method_kwargs: the dictionary of keyword arguments
                that the method is expected to accept.

        Raises:
            InterfaceRepositoryError: If the method does not exist, is not an async method,
            or does not accept the specified keyword arguments.
        """
        method = getattr(self, method_name, None)

        if method is None or not inspect.iscoroutinefunction(method):
            raise exceptions.InterfaceRepositoryError(
                f"The method {method_name} does not exist or is not an async method on {type(self).__name__}."
            )

        # Get the signature of the method
        sig = inspect.signature(method)
        params = sig.parameters

        # Check if all kwargs are in the function's parameters
        if not all(k in params for k in kwargs):
            raise exceptions.InterfaceRepositoryError(
                f"The method {method_name} does not accept the specified keyword arguments."
            )

        # Check if all required parameters are present in the kwargs
        for param_name, param in params.items():
            if param.default is inspect.Parameter.empty and param_name not in kwargs:
                raise exceptions.InterfaceRepositoryError(
                    f"The method {method_name} requires a '{param_name}' argument which is not provided."
                )
