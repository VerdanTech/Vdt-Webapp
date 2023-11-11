from src import settings
from src.infra.email import provide_litestar_email_emitter
from src.infra.email.aiosmtplib import provide_aiosmtplib_client
from src.infra.persistence.repository.alchemy.litestar_lifecycle import (
    AlchemyLitestarDBLifecycleManager,
)
from src.infra.persistence.repository.alchemy.user import (
    provide_user_alchemy_repository,
)
from src.infra.security.crypt.passlib import provide_passlib_crypt
from src.ops.user.controllers import (
    provide_user_auth_operations,
    provide_user_read_operations,
    provide_user_verification_operations,
    provide_user_write_operations,
)
from src.ops.user.sanitizer import provide_user_sanitizer

# ============================================================================
# PROVIDER SELECTION
#
# Methods which provide dependencies for injection are called providers.
# This file provides a centralized location for configuring providers for injection.
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
        settings.DB_CLIENT_PK: AlchemyLitestarDBLifecycleManager.provide_client
    }
    db_session_provider = {
        settings.DB_SESSION_PK: AlchemyLitestarDBLifecycleManager.provide_transaction
    }

    # Repositories
    user_repo_provider = {settings.USER_REPOSITORY_PK: provide_user_alchemy_repository}

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
        | user_repo_provider
        | email_client_provider
        | email_emitter_provider
        | password_crypt_provider
    )
