from contextlib import asynccontextmanager
from typing import AsyncGenerator, Protocol, TypeVar

from litestar import Litestar
from litestar.datastructures import State

DBClientType = TypeVar("DBClientType")
DBClientSessionType = TypeVar("DBClientSessionType")


class AbstractLitestarDBLifecycleManager(Protocol):
    @staticmethod
    def provide_client(state: State) -> DBClientType:
        """Given the application state, get the existing client

        Args:
            state (State): litestar application state

        Raises:
            ClientLifecycleError: raised if the client does not
                already exist in the application state

        Returns:
            DBClientType: existing database client
        """
        ...

    @staticmethod
    def set_client(state: State, client: DBClientType) -> None:
        """Given the application state and a client, set the client
            on the application state

        Args:
            state (State): litestar application state
            client (DBClientType): new database client
        """
        ...

    @staticmethod
    def close_client(client: DBClientType) -> None:
        """Given a client, close the connection

        Args:
            client (DBClientType): existing database client
        """
        ...

    @asynccontextmanager
    @staticmethod
    async def client_lifecycle(app: Litestar) -> AsyncGenerator[None, None]:
        """Async lifecycle context manager used in Litestar's lifecycle
            attribute, to open and finally close a motor client connection

        Args:
            app (Litestar): litestar application

        Returns:
            AsyncGenerator[None, None]: yielded lifecycle
        """
        ...

    @staticmethod
    async def provide_session(
        client: DBClientType,
    ) -> AsyncGenerator[DBClientSessionType, None]:
        """Given an existing client, start a session and
            transaction, and yield the session object

        Args:
            client (DBClientType): existing database client

        Yields:
            Iterator[AsyncGenerator[DBClientSessionType, None]]:
                the created session
        """
        ...
