from sqlalchemy.ext.asyncio import AsyncSession
from src.verdantech_api.domain.models.user.entities import User

from .repository import UserAlchemyRepository

# ============================================================================
# PROVIDER METHODS
# ============================================================================


def provide_user_alchemy_repository(
    db_session: AsyncSession,
) -> UserAlchemyRepository:
    """Configure and provide a user sqlalchemy repository for dependency injection"""
    return UserAlchemyRepository(
        session=db_session,
    )
