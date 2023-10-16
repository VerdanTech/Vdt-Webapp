from typing import Any, Dict

from litestar.di import Provide
from src import settings
from src.dependencies import ApplicationDependencies

# Apply Litestar's dependency injection provider wrapper
all_wrapped_providers = {
    key: Provide(value) for key, value in ApplicationDependencies.all_providers.items()
}


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


# Select application-wide dependencies
application_layer_dependencies = select(settings.DB_CLIENT_PK, settings.DB_SESSION_PK)
