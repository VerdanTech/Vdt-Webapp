# VerdanTech Source
from src import settings
from src.infra.email.client.providers import provide_aiosmtplib_client
from src.infra.email.emitter.providers import provide_litestar_email_emitter
from src.infra.security.crypt.providers import provide_passlib_crypt

# ============================================================================
# PROVIDER SELECTION
#
# Methods which provide dependencies for injection are called providers.
# This file provides a centralized location for configuring providers for injection.
# ============================================================================


class ApplicationDependencies:
    # ======================================
    # OPERATIONS CONTROLLERS
    # ======================================

    # User
    user_ops_provider = {
        settings.USER_READ_OP_PK: provide_user_read_ops,
        settings.USER_WRITE_OP_PK: provide_user_write_ops,
        settings.USER_VERIFICATION_OP_PK: provide_user_verification_ops,
        settings.USER_AUTH_OP_PK: provide_user_auth_ops,
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
    """
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
    )"""
