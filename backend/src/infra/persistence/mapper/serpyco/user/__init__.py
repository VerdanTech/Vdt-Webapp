from .serializer import UserSerpycoMapper

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_serpyco_mapper():
    """Configure and provide user serpyco mapper for dependency injection"""
    return UserSerpycoMapper()
