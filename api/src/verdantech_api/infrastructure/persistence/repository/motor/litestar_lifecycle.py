from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Protocol

from litestar import Litestar
from litestar.datastructures import State
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
from pymongo import errors as pymongo_errors
from src.verdantech_api import settings

from ..exceptions import ClientLifecycleError
from .exceptions import motor_exception_map


class MotorLitestarDBLifecycleManager(Protocol):
    @staticmethod
    async def provide_client(state: State) -> AsyncIOMotorClient:
        """Given the application state, get the existing client

        Args:
            state (State): litestar application state

        Raises:
            ClientLifecycleError: raised if the client does not
                already exist in the application state

        Returns:
            AsyncIOMotorClient: existing motor client
        """
        existing_client = getattr(state, settings.MONGO_CLIENT_NAME, None)
        if existing_client is None:
            raise ClientLifecycleError(
                "Mongo motor client does not exist in the application state"
            )
        return existing_client

    @staticmethod
    def set_client(state: State, client: AsyncIOMotorClient) -> None:
        """Given the application state and a client, set the client
            on the application state

        Args:
            state (State): litestar application state
            client (AsyncIOMotorClient): new motor client
        """
        setattr(state, settings.MONGO_CLIENT_NAME, client)

    @staticmethod
    async def close_client(client: AsyncIOMotorClient) -> None:
        """Given a client, close the connection

        Args:
            client (AsyncIOMotorClient): existing motor client
        """
        await client.close()

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
        existing_client = MotorLitestarDBLifecycleManager.get_client(state=app.state)
        if existing_client is None:
            client = AsyncIOMotorClient(settings.MONGO_URI)
            MotorLitestarDBLifecycleManager.set_client(state=app.State, client=client)

        try:
            yield
        finally:
            await MotorLitestarDBLifecycleManager.close_client(client=client)

    @staticmethod
    async def provide_session(
        client: AsyncIOMotorClient,
    ) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
        """Given an existing client, start a session and
            transaction, and yield the session object

        Args:
            client (AsyncIOMotorClient): existing motor client

        Yields:
            Iterator[AsyncGenerator[AsyncIOMotorClientSession, None]]:
                the created session
        """
        async with await client.start_session() as session, motor_exception_map():
            async with session.start_transaction():
                yield session
