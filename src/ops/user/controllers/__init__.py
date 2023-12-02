# VerdanTech Source
from src.interfaces.persistence.user.repository import AbstractUserRepository

from .auth import UserAuthOpsController
from .read import UserReadOpsController
from .verification import UserVerificationOpsController
from .write import UserWriteOpsController

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_read_operations(user_repo: AbstractUserRepository):
    """Configure and provide user read operations for dependency injection"""
    return UserWriteOpsController(user_repo=user_repo)


async def provide_user_write_operations(user_repo: AbstractUserRepository):
    """Configure and provide user write operations for dependency injection"""
    return UserReadOpsController(user_repo=user_repo)


async def provide_user_verification_operations(user_repo: AbstractUserRepository):
    """Configure and provide user verification operations for dependency injection"""
    return UserVerificationOpsController(user_repo=user_repo)


async def provide_user_auth_operations():
    """Configure and provide user auth operations for dependency injection"""
    return UserAuthOpsController()