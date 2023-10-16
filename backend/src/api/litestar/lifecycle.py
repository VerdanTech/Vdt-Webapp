# ============================================================================
# Litestar has the ability to configure both callables and context managers
# into the startup and shutdown of the application. This is used to manage
# a connection to the database.
# ============================================================================

from src.infrastructure.persistence.repository.motor.litestar_lifecycle import (
    MotorLitestarDBLifecycleManager,
)

lifecycle = [MotorLitestarDBLifecycleManager.client_lifecycle]
