# External Libraries
from attr import define
from sqlalchemy.ext.asyncio import AsyncSession as AlchemySession

# VerdanTech Source
from src.common.interfaces.persistence import AbstractRepositoryContainer
from src.user.adapters.sqlalchemy.repository import UserAlchemyRepository


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
