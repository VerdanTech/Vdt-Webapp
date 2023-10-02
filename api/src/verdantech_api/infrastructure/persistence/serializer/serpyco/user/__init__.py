from src.verdantech_api import settings
from src.verdantech_api.domain.models.user.services.sanitization import UserSanitizer

from .serializer import UserSerpycoSerializezr

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_serpyco_serializer(user_sanitizer: UserSanitizer):
    """Configure and provide user serpyco serializer for dependency injection"""
    return UserSerpycoSerializezr(sanitizer=user_sanitizer)


# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Base provider
user_serpyco_serializer_provider = {
    settings.USER_SANITIZER_PK: provide_user_serpyco_serializer
}
