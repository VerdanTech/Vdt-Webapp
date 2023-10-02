from typing import Any, Dict, List

from litestar.di import Provide
from src.verdantech_api.application import application_provider
from src.verdantech_api.infrastructure import infrastructure_provider

# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Merge provider
# Complete set of provider functions for dependency injection
all_providers = application_provider | infrastructure_provider

# Apply Litestar's dependency injection provider wrapper
all_wrapped_providers = {key: Provide(value) for key, value in all_providers.items()}


def select(*keys: str) -> Dict[str, Any]:
    """Return a subset of all providers

    Args:
        keys (List[str]): list of keys to return

    Returns:
        Dict[str, Any]: filtered provider dict
    """
    return {
        key: all_wrapped_providers[key] for key in keys if key in all_wrapped_providers
    }
