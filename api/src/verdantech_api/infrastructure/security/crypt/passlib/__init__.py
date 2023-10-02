from src.verdantech_api import settings

from .passlib import PasslibPasswordCrypt

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_passlib_crypt():
    """Provide passlib password crypt for dependency injection"""
    return PasslibPasswordCrypt()


# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Base provider
passlib_crypt_provider = {settings.PASSWORD_CRYPT_PK: provide_passlib_crypt}
