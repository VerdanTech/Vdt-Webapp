from src.verdantech_api import settings
from src.verdantech_api.application.user.operations import (
    provide_user_auth_operations,
    provide_user_read_operations,
    provide_user_verification_operations,
    provide_user_write_operations,
)
from src.verdantech_api.application.user.sanitizer import provide_user_sanitizer
from src.verdantech_api.infrastructure.email import provide_litestar_email_emitter
from src.verdantech_api.infrastructure.email.aiosmtplib import provide_aiosmtplib_client
from src.verdantech_api.infrastructure.persistence.mapper.serpyco import (
    provide_user_serpyco_serializer,
)
from src.verdantech_api.infrastructure.persistence.repository.motor import (
    MotorLitestarDBLifecycleManager,
    provide_user_motor_repository,
)
from src.verdantech_api.infrastructure.security.crypt.passlib import (
    provide_passlib_crypt,
)

# ============================================================================
# PROVIDER SELECTION
# ============================================================================


class ApplicationDependencies:
    # ======================================
    # APPLICATION OPERATIONS
    # ======================================

    # User
    user_read_operations_provider = {
        settings.USER_READ_OP_PK: provide_user_read_operations
    }
    user_write_operations_provider = {
        settings.USER_WRITE_OP_PK: provide_user_write_operations
    }
    user_verification_operations_provider = {
        settings.USER_VERIFICATION_OP_PK: provide_user_verification_operations
    }
    user_auth_operations_provider = {
        settings.USER_AUTH_OP_PK: provide_user_auth_operations
    }

    # ======================================
    # SANITIZERS
    # ======================================

    user_sanitizer_provider = {settings.USER_SANITIZER_PK: provide_user_sanitizer}

    # ======================================
    # PERSISTENCE
    # ======================================

    # Database
    db_client_provider = {
        settings.DB_CLIENT_PK: MotorLitestarDBLifecycleManager.provide_client
    }
    db_session_provider = {
        settings.DB_SESSION_PK: MotorLitestarDBLifecycleManager.provide_session
    }

    # Serializer
    user_serializer_provider = {
        settings.USER_SERIALIZER_PK: provide_user_serpyco_serializer
    }

    # Repositories
    user_repo_provider = {settings.USER_REPOSITORY_PK: provide_user_motor_repository}

    # ======================================
    # EMAIL
    # ======================================

    email_client_provider = {settings.EMAIL_CLIENT_PK: provide_aiosmtplib_client}
    email_emitter_provider = {settings.EMAIL_EMITTER_PK: provide_litestar_email_emitter}

    # ======================================
    # SECURITY
    # ======================================

    password_crypt_provider = {settings.PASSWORD_CRYPT_PK: provide_passlib_crypt}

    # ======================================
    # MERGE ALL DEPENDENCIES
    # ======================================

    all_providers = (
        user_read_operations_provider
        | user_write_operations_provider
        | user_verification_operations_provider
        | user_auth_operations_provider
        | user_sanitizer_provider
        | db_client_provider
        | db_session_provider
        | user_serializer_provider
        | user_repo_provider
        | email_client_provider
        | email_emitter_provider
        | password_crypt_provider
    )
