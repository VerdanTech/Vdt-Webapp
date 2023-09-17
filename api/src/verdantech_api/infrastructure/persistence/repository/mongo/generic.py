from typing import TYPE_CHECKING, Any, Dict

from src.verdantech_api.domain.models.common.entities import RootEntityT

"""
if TYPE_CHECKING:
    from motor.motor_asyncio import AsyncIOMotorCollection



from ..generic import BaseRepository


class MongoMotorRepository(BaseRepository[RootEntityT]):
    
    def __init__(
        self, collection: AsyncIOMotorCollection, **kwargs: Dict[str, Any]
    ) -> None:
        super().__init__(**kwargs)
        self.collection = collection
"""
