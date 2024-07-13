# External Libraries
from attr import define
from sqlalchemy.ext.asyncio import AsyncSession as AlchemySession

# VerdanTech Source
from src.common.interfaces.persistence import AbstractRepositoryContainer
from src.garden.adapters.sqlalchemy import GardenAlchemyRepository
from src.user.adapters.sqlalchemy import UserAlchemyRepository


@define
class StandardRepositoryContainer(AbstractRepositoryContainer):
    users: UserAlchemyRepository
    gardens: GardenAlchemyRepository

    @classmethod
    def enter_uow(
        cls, alchemy_session: AlchemySession
    ) -> "StandardRepositoryContainer":
        return StandardRepositoryContainer(
            users=UserAlchemyRepository(session=alchemy_session),
            gardens=GardenAlchemyRepository(session=alchemy_session),
        )
