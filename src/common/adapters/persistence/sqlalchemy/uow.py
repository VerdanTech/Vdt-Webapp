# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

# VerdanTech Source
from src import settings
from src.common.interfaces.persistence import AbstractUow

from .client import AlchemyClient
from src.user.adapters.sqlalchemy.repository import UserAlchemyRepository

sessionmaker = async_sessionmaker(expire_on_commit=False)


class AlchemyUow(AbstractUow):
    session: AsyncSession

    def __init__(self, client: AlchemyClient):
        self.client = client

    async def __aenter__(self):
        self.session = sessionmaker(bind=self.client.engine)
        self.users = UserAlchemyRepository(session=self.session)
        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def _commit(self) -> None:
        """
        Commits all changes to the database.
        """
        if settings.ALCHEMY_TRANSACTION_COMMIT:
            await self.session.commit()

    async def rollback(self) -> None:
        """
        Discards all changes to the database.
        """
        await self.session.rollback()
