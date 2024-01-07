# Standard Library
from contextlib import asynccontextmanager
from typing import AsyncGenerator

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

sessionmaker = async_sessionmaker(
    expire_on_commit=False,
)


@asynccontextmanager
async def function_scoped_sql_transaction(
    alchemy_uri: str,
) -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(alchemy_uri, echo=True, isolation_level="AUTOCOMMIT")
    async with sessionmaker(bind=engine) as transaction:
        yield transaction
