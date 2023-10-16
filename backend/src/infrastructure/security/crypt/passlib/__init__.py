from src import settings

from .passlib import PasslibPasswordCrypt

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_passlib_crypt():
    """Provide passlib password crypt for dependency injection"""
    return PasslibPasswordCrypt()
