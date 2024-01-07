# Standard Library
import pdb
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from litestar import Litestar
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool
from svcs import Container

# VerdanTech Source
from src import settings
from src.infra.persistence.sqlalchemy.repository import AlchemyClient

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
    # autoflush=False,
    # autocommit=False,
)


@asynccontextmanager
async def function_scoped_sql_transaction(
    alchemy_uri: str,
) -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(
        alchemy_uri,
        # isolation_level="AUTOCOMMIT",
        echo=True,
    )
    async with sessionmaker(bind=engine) as transaction:
            yield transaction
