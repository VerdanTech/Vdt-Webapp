# Standard Library
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass

# External Libraries
from litestar import Litestar
from litestar.datastructures import State as LitestarGlobalState
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# VerdanTech Source
from src import settings
from src.infra.persistence.generic.repository.exceptions import ClientLifecycleError
from src.infra.persistence.sqlalchemy.mapper.model import Base

from .exceptions import alchemy_exception_map

sessionmaker = async_sessionmaker(expire_on_commit=False)


@dataclass
class AlchemyClient:
    engine: AsyncEngine


class AlchemyLitestarDBLifecycleManager:
    @staticmethod
    async def provide_client(state: LitestarGlobalState) -> AlchemyClient:
        """
        Given the application state, get the existing sqlalchemy client.

        Args:
            state (LitestarGlobalState): litestar global application state.

        Raises:
            ClientLifecycleError: raised if the client does not
                already exist in the application state.

        Returns:
            AlchemyClient: existing sqlalchemy client.
        """
        existing_client = getattr(state, settings.ALCHEMY_CLIENT_NAME, None)
        if existing_client is None:
            raise ClientLifecycleError(
                "SqlAlchemy Client (Engine) does not exist in the application state"
            )
        return existing_client

    @staticmethod
    def set_client(state: LitestarGlobalState, client: AlchemyClient) -> None:
        """
        Given the application state and a sqlalchemy client, set the client
        on the application state.

        Args:
            state (LitestarGlobalState): litestar global application state.
            client (AlchemyClient): new sqlalchemy client to set.
        """
        setattr(state, settings.ALCHEMY_CLIENT_NAME, client)

    @staticmethod
    async def close_client(client: AlchemyClient) -> None:
        """Given a sqlalchemy client, close the client.

        Args:
            client (AlchemyClient): existing sqlalchemy client.
        """
        await client.engine.dispose()

    @staticmethod
    async def _schema_init(client: AlchemyClient) -> None:
        """
        Given a sqlalchemy client, initialize table metadata on that client.

        Args:
            client(AlchemyClient): existing sqlalchemy client.
        """
        async with client.engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    @staticmethod
    async def client_lifecycle(app: Litestar) -> AsyncGenerator[None, None]:
        """
        Async lifecycle context manager used in Litestar's lifecycle attribute,
        set in src.asgi.litestar.lifecycle.py.

        1. Creates the engine and initializes
            table metadata, if no client exists already.
        2. Yields to the application.
        3. Closes the client.

        See: (https://docs.litestar.dev/2/usage/applications.html)

        Args:
            app (Litestar): litestar application.

        Returns:
            AsyncGenerator[None, None]: yields to application.
        """
        client = getattr(app.state, settings.ALCHEMY_CLIENT_NAME, None)
        if client is None:
            engine = create_async_engine(settings.ALCHEMY_URI)
            client = AlchemyClient(engine=engine)
            AlchemyLitestarDBLifecycleManager.set_client(state=app.state, client=client)

        await AlchemyLitestarDBLifecycleManager._schema_init(client=client)

        try:
            yield
        finally:
            await AlchemyLitestarDBLifecycleManager.close_client(client=client)

    @staticmethod
    async def provide_transaction(
        state: LitestarGlobalState,
    ) -> AsyncGenerator[AsyncSession, None]:
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
        client = await AlchemyLitestarDBLifecycleManager.provide_client(state=state)
        async with sessionmaker(bind=client.engine) as transaction:
            async with alchemy_exception_map():
                async with transaction.begin():
                    yield transaction
