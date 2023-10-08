from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
from src.verdantech_api import settings
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.infrastructure.persistence.mapper.generic import (
    AbstractSerializer,
)

from .repository import UserMotorRepository

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_motor_repository(
    client: AsyncIOMotorClient,
    client_session: AsyncIOMotorClientSession,
    user_serializer: AbstractSerializer[User],
) -> UserMotorRepository:
    """Configure and provide a user motor repository for dependency injection"""
    user_collection = client[settings.MONGO_DATABASE_NAME][
        settings.MONGO_USER_COLLECTION_NAME
    ]
    return UserMotorRepository(
        collection=user_collection,
        client_session=client_session,
        serializer=user_serializer,
    )
