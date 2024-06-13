# Standard Library
from typing import TYPE_CHECKING

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.common.interfaces.persistence.repository import AbstractRepository

if TYPE_CHECKING:
    # VerdanTech Source
    from src.common.domain import RootEntity


class BaseAlchemyRepository[RootEntityT: RootEntity](AbstractRepository[RootEntityT]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
