# Standard Library
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass

# External Libraries
from litestar import Litestar
from litestar.datastructures import State
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


@dataclass
class AlchemyClient:
    engine: AsyncEngine
    sessionmaker: AsyncSession


class AlchemyLitestarDBLifecycleManager:
    @staticmethod
    async def provide_client(state: State) -> AlchemyClient:
        """Given the application state, get the existing sqlalchemy engine

        Args:
            state (State): litestar application state

        Raises:
            ClientLifecycleError: raised if the client does not
                already exist in the application state

        Returns:
            AlchemyClient: existing sqlalchemy client
        """
        existing_client = getattr(state, settings.ALCHEMY_CLIENT_NAME, None)
        if existing_client is None:
            raise ClientLifecycleError(
                "SqlAlchemy Client (Engine) does not exist in the application state"
            )
        return existing_client

    @staticmethod
    def set_client(state: State, client: AlchemyClient) -> None:
        """Given the application state and a sqlalchemy client, set the client
            on the application state

        Args:
            state (State): litestar application state
            engine (AsyncEngine): new sqlalchemy engine
        """
        setattr(state, settings.ALCHEMY_CLIENT_NAME, client)

    @staticmethod
    async def close_client(client: AlchemyClient) -> None:
        """Given a sqlalchemy client, close the client

        Args:
            client (AlchemyClient): existing sqlalchemy client
        """
        await client.engine.dispose()

    @staticmethod
    async def _schema_init(client: AlchemyClient) -> None:
        """Create database tables"""
        async with client.engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    @staticmethod
    async def client_lifecycle(app: Litestar) -> AsyncGenerator[None, None]:
        """Async lifecycle context manager used in Litestar's lifecycle
            attribute, to open and finally close a sqlalchemy client

        Args:
            app (Litestar): litestar application

        Returns:
            AsyncGenerator[None, None]: yielded lifecycle
        """
        engine = create_async_engine(settings.ALCHEMY_URI)
        sessionmaker = async_sessionmaker(expire_on_commit=False)
        client = AlchemyClient(engine=engine, sessionmaker=sessionmaker)
        await AlchemyLitestarDBLifecycleManager._schema_init(client=client)
        AlchemyLitestarDBLifecycleManager.set_client(state=app.state, client=client)

        try:
            yield
        finally:
            await AlchemyLitestarDBLifecycleManager.close_client(client=client)

    @staticmethod
    async def provide_transaction(state: State) -> AsyncGenerator[AsyncSession, None]:
        """Given an existing client, start a session and
            transaction, and yield the session object

        Args:
            client (AlchemyClient): existing sqlalchemy client

        Yields:
            Iterator[AsyncGenerator[AsyncSession, None]]:
                the created session
        """
        async with alchemy_exception_map:
            client = AlchemyLitestarDBLifecycleManager.provide_client(state=state)
            async with client.sessionmaker(bind=client.engine) as session:
                async with session.begin():
                    yield session
