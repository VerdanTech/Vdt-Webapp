# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.common.adapters.persistence.common import BaseRepository
from .mapper import BaseAlchemyModel
from src.common.domain import RootEntity


class BaseAlchemyRepository[RootEntityT: RootEntity, AlchemyModelT: BaseAlchemyModel](
    BaseRepository[RootEntityT]
):
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self.session = session
