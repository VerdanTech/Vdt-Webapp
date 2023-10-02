from .repository import client_provider, repo_provider, session_provider
from .serializer import serializer_provider

# ============================================================================
# PROVIDER METHODS
# ============================================================================

# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Merge provider
persistence_provider = (
    client_provider | session_provider | repo_provider | serializer_provider
)
