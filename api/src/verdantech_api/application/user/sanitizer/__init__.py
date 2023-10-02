from src.verdantech_api import settings

from .object import provide_user_sanitizer

# ============================================================================
# PROVIDER METHODS
# ============================================================================

# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Base provider
user_sanitizer_provider = {settings.USER_SANITIZER_PK: provide_user_sanitizer}
