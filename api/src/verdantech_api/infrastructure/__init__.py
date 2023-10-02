from .email import email_provider
from .persistence import persistence_provider
from .security import security_provider

# ============================================================================
# PROVIDER METHODS
# ============================================================================

# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Merge provider
infrastructure_provider = email_provider | persistence_provider | security_provider
