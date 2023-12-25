# Standard Library
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Protocol, TypeVar

# External Libraries
from litestar import Litestar
from litestar.datastructures import State as LitestarGlobalState

DBClientType = TypeVar("DBClientType")
DBClientTransactionType = TypeVar("DBClientTransactionType")


class AbstractLitestarDBLifecycleManager(Protocol):
    @staticmethod
    async def provide_client(state: LitestarGlobalState) -> DBClientType:
        """
        Given the application state, get the existing client.

        Args:
            state (LitestarGlobalState): litestar application state.

        Raises:
            ClientLifecycleError: raised if the client does not
                already exist in the application state.

        Returns:
            DBClientType: existing database client.
        """
        ...

    @staticmethod
    def set_client(state: LitestarGlobalState, client: DBClientType) -> None:
        """
        Given the application state and a client, set the client
        on the application state.

        Args:
            state (LitestarGlobalState): litestar application state.
            client (DBClientType): new database client to set.
        """
        ...

    @staticmethod
    def close_client(client: DBClientType) -> None:
        """
        Given a client, closes the client.

        Args:
            client (DBClientType): existing database client.
        """
        ...

    @asynccontextmanager
    @staticmethod
    async def client_lifecycle(app: Litestar) -> AsyncGenerator[None, None]:
        """
        Async lifecycle context manager used in Litestar's lifecycle attribute,
        set in src.asgi.litestar.lifecycle.py.

        1. Creates the client if it doesn't already exist.
        2. Yields to the application.
        3. Closes the client.

        Args:
            app (Litestar): litestar application.

        Returns:
            AsyncGenerator[None, None]: yields to application.
        """
        ...

    @staticmethod
    async def provide_session(
        client: DBClientType,
    ) -> AsyncGenerator[DBClientTransactionType, None]:
        """
        Given an existing client, begin and yield a transaction.

        Yields within a context manager mapping sqlalchemy exceptions
        to native application exceptions.

        Args:
            state (LitestarGlobalState): litestar global application
                state provided by default as a dependency injected
                into route handlers.

        Yields:
            Iterator[AsyncGenerator[AsyncSession, None]]:
                the created transaction.
        """
        ...
