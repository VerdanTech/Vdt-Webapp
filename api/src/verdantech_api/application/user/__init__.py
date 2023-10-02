from .operations import user_operations_provider
from .sanitizer import user_sanitizer_provider

# ============================================================================
# PROVIDER METHODS
# ============================================================================

# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Merge provider
user_application_provider = user_sanitizer_provider | user_operations_provider
