from src.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)

from .auth import UserAuthOperations
from .read import UserReadOperations
from .verification import UserVerificationOperations
from .write import UserWriteOperations

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_read_operations(user_repo: AbstractUserRepository):
    """Configure and provide user read operations for dependency injection"""
    return UserWriteOperations(user_repo=user_repo)


async def provide_user_write_operations(user_repo: AbstractUserRepository):
    """Configure and provide user write operations for dependency injection"""
    return UserReadOperations(user_repo=user_repo)


async def provide_user_verification_operations(user_repo: AbstractUserRepository):
    """Configure and provide user verification operations for dependency injection"""
    return UserVerificationOperations(user_repo=user_repo)


async def provide_user_auth_operations():
    """Configure and provide user auth operations for dependency injection"""
    return UserAuthOperations()
