from src.verdantech_api import settings

from .litestar_lifecycle import MotorLitestarDBLifecycleManager
from .user import user_repo_provider

# ============================================================================
# PROVIDER METHODS
# ============================================================================

# ============================================================================
# PROVIDER DICTS
# ============================================================================

# Base providers
motor_client_provider = {
    settings.DB_CLIENT_PK: MotorLitestarDBLifecycleManager.provide_client
}
motor_session_provider = {
    settings.DB_SESSION_PK: MotorLitestarDBLifecycleManager.provide_session
}

# Merge provider
motor_repo_provider = user_repo_provider
