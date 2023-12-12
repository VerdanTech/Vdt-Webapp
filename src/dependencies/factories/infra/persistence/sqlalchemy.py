# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession
from svcs import Container

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_alchemy_repository(
    svcs_container: Container,
) -> UserAlchemyRepository:
    """Configure and provide a user sqlalchemy repository for dependency injection"""
    sql_transaction = await svcs_container.aget(AsyncSession)
    return UserAlchemyRepository(
        transaction=sql_transaction,
    )
