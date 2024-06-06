# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Registry

# VerdanTech Source
from src.domain.user import UserSanitizer
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import AlchemyClient
from src.interfaces.email.client import AbstractEmailClient
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user import controllers as user_ops

from .factories.infra.email.client import provide_aiosmtplib_client
from .factories.infra.email.emitter import provide_saq_email_emitter
from .factories.infra.persistence.sqlalchemy import (
    provide_alchemy_client,
    provide_alchemy_transaction,
    provide_user_alchemy_repository,
)
from .factories.infra.security.crypt import provide_passlib_crypt
from .factories.ops.user.controllers import (
    provide_user_auth_ops,
    provide_user_verification_ops,
    provide_user_write_ops,
)
from .factories.ops.user.sanitizers import provide_user_sanitizer


def create_registry() -> Registry:
    registry = Registry()

    # ======================================
    # OPERATIONS CONTROLLERS
    # ======================================

    # User
    registry.register_factory(user_ops.UserAuthOpsController, provide_user_auth_ops)
    registry.register_factory(user_ops.UserWriteOpsController, provide_user_write_ops)
    registry.register_factory(
        user_ops.UserVerificationOpsController, provide_user_verification_ops
    )

    # ======================================
    # SANITIZERS
    # ======================================

    # User
    registry.register_factory(UserSanitizer, provide_user_sanitizer)

    # ======================================
    # PERSISTENCE
    # ======================================

    # SqlAlchemy
    registry.register_factory(AlchemyClient, provide_alchemy_client)
    registry.register_factory(AsyncSession, provide_alchemy_transaction)

    # User Repository
    registry.register_factory(AbstractUserRepository, provide_user_alchemy_repository)

    # ======================================
    # QUEUE
    # ======================================

    # ======================================
    # EMAIL
    # ======================================

    # Client
    registry.register_factory(AbstractEmailClient, provide_aiosmtplib_client)

    # Emitter
    registry.register_factory(AbstractEmailEmitter, provide_saq_email_emitter)

    # ======================================
    # SECURITY
    # ======================================

    registry.register_factory(AbstractPasswordCrypt, provide_passlib_crypt)

    return registry
