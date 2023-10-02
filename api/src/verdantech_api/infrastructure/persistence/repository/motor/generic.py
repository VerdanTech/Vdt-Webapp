from typing import Any, Dict

from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection
from src.verdantech_api.domain.models.common.entities import RootEntityT

from ..generic import BaseRepository


class BaseMotorRepository(BaseRepository[RootEntityT]):
    def __init__(
        self,
        collection: AsyncIOMotorCollection,
        client_session: AsyncIOMotorClientSession,
        **kwargs: Dict[str, Any],
    ) -> None:
        super().__init__(**kwargs)
        self.collection = collection
        self.client_session = client_session
