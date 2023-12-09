# VerdanTech Source
from src import providers
from src.infra.email.client import providers as email_clients
from src.infra.email.emitter import providers as email_emitters
from src.infra.persistence.sqlalchemy.repository.litestar_lifecycle import (
    AlchemyLitestarDBLifecycleManager,
)
from src.infra.persistence.sqlalchemy.repository.user import providers as user_repos
from src.infra.security.crypt import providers as crypts
from src.ops.user import providers as user_ops, sanitizers as user_sanitizers

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
        # settings.USER_READ_OPS_PK: provide_user_read_ops,
        providers.USER_WRITE_OPS_PK: user_ops.provide_user_write_ops,
        # settings.USER_VERIFICATION_OPS_PK: provide_user_verification_ops,
        # settings.USER_AUTH_OPS_PK: provide_user_auth_ops,
    }

    # ======================================
    # SANITIZERS
    # ======================================

    sanitizer_provider = {
        providers.USER_SANITIZER_PK: user_sanitizers.provide_user_sanitizer
    }

    # ======================================
    # PERSISTENCE
    # ======================================

    # Database
    sql_provider = {
        providers.SQL_CLIENT_PK: AlchemyLitestarDBLifecycleManager.provide_client,
        providers.SQL_TRANSACTION_PK: AlchemyLitestarDBLifecycleManager.provide_transaction,
    }

    # Repositories
    user_repo_provider = {
        providers.USER_STORE_REPO_PK: user_repos.provide_user_alchemy_repository
    }

    # ======================================
    # EMAIL
    # ======================================

    email_provider = {
        providers.EMAIL_CLIENT_PK: email_clients.provide_aiosmtplib_client,
        providers.EMAIL_EMITTER_PK: email_emitters.provide_litestar_email_emitter,
    }

    # ======================================
    # SECURITY
    # ======================================

    password_crypt_provider = {
        providers.PASSWORD_CRYPT_PK: crypts.provide_passlib_crypt
    }

    # ======================================
    # MERGE ALL DEPENDENCIES
    # ======================================
    all_providers = (
        user_ops_provider
        | sanitizer_provider
        | sql_provider
        | user_repo_provider
        | email_provider
        | password_crypt_provider
    )
