# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.adapters.persistence.common import BaseRepository
from src.adapters.persistence.sqlalchemy.mapper.common import BaseAlchemyModel
from src.domain.common import RootEntity


class BaseAlchemyRepository[RootEntityT: RootEntity, AlchemyModelT: BaseAlchemyModel](
    BaseRepository[RootEntityT]
):
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self.session = session
