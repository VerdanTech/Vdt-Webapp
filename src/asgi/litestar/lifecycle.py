# ============================================================================
# Litestar has the ability to configure both callables and context managers
# into the startup and shutdown of the application. This is used to manage
# a connection to the database.
# ============================================================================

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.litestar_lifecycle import (
    AlchemyLitestarDBLifecycleManager,
)

lifecycle = [AlchemyLitestarDBLifecycleManager.client_lifecycle]
