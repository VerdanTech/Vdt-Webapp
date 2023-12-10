# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.interfaces.persistence.user import AbstractUserRepository
from src.domain.user.entities import User

from .repository import UserAlchemyRepository

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_alchemy_repository(
    sql_transaction: AsyncSession,
) -> UserAlchemyRepository:
    """Configure and provide a user sqlalchemy repository for dependency injection"""
    return UserAlchemyRepository(
        transaction=sql_transaction,
    )
