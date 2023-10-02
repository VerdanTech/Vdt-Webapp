from src.verdantech_api import settings
from src.verdantech_api.domain.interfaces.persistence.user.repository import (
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


# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Base providers
user_read_operations_provider = {settings.USER_READ_OP_PK: provide_user_read_operations}
user_write_operations_provider = {
    settings.USER_WRITE_OP_PK: provide_user_write_operations
}
user_verification_operations_provider = {
    settings.USER_VERIFICATION_OP_PK: provide_user_verification_operations
}
user_auth_operations_provider = {settings.USER_AUTH_OP_PK: provide_user_auth_operations}

# Merge provider
user_operations_provider = (
    user_read_operations_provider
    | user_write_operations_provider
    | user_verification_operations_provider
    | user_auth_operations_provider
)
