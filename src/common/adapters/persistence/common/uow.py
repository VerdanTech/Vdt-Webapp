# External Libraries
from attr import define, field
from sqlalchemy.ext.asyncio import AsyncSession as AlchemySession, async_sessionmaker

# VerdanTech Source
from src import settings
from src.common.interfaces.persistence import AbstractRepositoryContainer, AbstractUow
from src.user.adapters.sqlalchemy.repository import UserAlchemyRepository

from ..sqlalchemy.client import AlchemyClient

sessionmaker = async_sessionmaker(expire_on_commit=False)


@define
class DatabaseClients:
    alchemy_client: AlchemyClient


@define
class StandardRepositoryContainer(AbstractRepositoryContainer):
    users: UserAlchemyRepository

    @classmethod
    def enter_uow(
        cls, alchemy_session: AlchemySession
    ) -> "StandardRepositoryContainer":
        return StandardRepositoryContainer(
            users=UserAlchemyRepository(session=alchemy_session)
        )


class StandardUow(AbstractUow):
    clients: DatabaseClients
    repos: StandardRepositoryContainer | None = field(default=None, init=False)
    alchemy_session: AlchemySession | None = field(default=None, init=False)

    def __init__(self, clients: DatabaseClients):
        self.clients = clients

    async def __aenter__(self):
        # Create sessions
        self.alchemy_session = sessionmaker(bind=self.clients.alchemy_client.engine)

        # Initialize repos
        self.repos = StandardRepositoryContainer.enter_uow(
            alchemy_session=self.alchemy_session
        )

        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)

        # Deinitialize repos
        self.repos = None

        # Close sessions
        if self.alchemy_session is None:
            # TODO Specify Exception
            raise Exception("SqlAlchemy session doesn't exist when it should")
        else:
            await self.alchemy_session.close()

    async def _commit(self) -> None:
        """
        Commits all changes to the database.
        """
        if self.alchemy_session is None:
            # TODO Specify Exception
            raise Exception("SqlAlchemy session doesn't exist when it should")
        else:
            if settings.ALCHEMY_TRANSACTION_COMMIT:
                await self.alchemy_session.commit()

    async def rollback(self) -> None:
        """
        Discards all changes to the database.
        """
        if self.alchemy_session is None:
            # TODO Specify Exception
            raise Exception("SqlAlchemy session doesn't exist when it should")
        else:
            await self.alchemy_session.rollback()
