# Standard Library
import asyncio
import pdb
from functools import partial
from typing import AsyncGenerator
from unittest import mock

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from testcontainers.postgres import PostgresContainer

# VerdanTech Source
from src.asgi.litestar.app import create_app
from tests.infra.persistence.sqlalchemy.repository.lifespan import (
    function_scoped_sql_transaction,
)

from .sqlalchemy import function_scoped_sql_transaction


@pytest.fixture
def postgres():
    with PostgresContainer() as postgres:
        postgres.driver = "asyncpg"
        connection_details = postgres.get_connection_url()
        print(connection_details)
        yield postgres


@pytest.fixture
async def alchemy_transaction(postgres) -> AsyncGenerator[AsyncSession, None]:
    async with function_scoped_sql_transaction(
        alchemy_uri=postgres.get_connection_url()
    ) as transaction:
        yield transaction
