from __future__ import annotations

# Standard Library
from typing import Any, Generator, Protocol, Type

# VerdanTech Source
from src.domain.common import Event, RootEntity

from .user import AbstractUserRepository


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
    touched_entities: set[T]
    """Tracks the entities which have been affected so that new events may be caught."""

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


class AbstractUow(Protocol):
    """
    A Unit Of Work (UoW) is a context manager for commiting and rolling back
    database operations.

    It encapsulates all repositories for conveinence.
    """

    users: AbstractUserRepository

    async def __aenter__(self) -> AbstractUow:
        return self

    async def __aexit__(self, *args) -> None:
        await self.rollback()

    async def commit(self) -> None:
        """
        Commits all changes to the database.
        """
        await self._commit()

    def collect_new_evets(self) -> Generator[Event, None, None]:
        """
        Yields all unhandled events on the touched entities.

        Yields:
            Generator[Event, None, None]: _description_
        """
        for entity in self.users.touched_entities:
            while entity.events:
                yield entity.events.pop(0)

    async def _commit(self) -> None:
        """
        Commits all changes to the database.
        """
        ...

    async def rollback(self) -> None:
        """
        Discards all changes to the database.
        """
        ...
