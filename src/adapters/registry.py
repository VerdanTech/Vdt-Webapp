# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Registry

# VerdanTech Source
from src.adapters.persistence.sqlalchemy.litestar_lifespan import AlchemyClient
from src.interfaces.email.client import AbstractEmailClient
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt

from .factories.email.client import provide_aiosmtplib_client
from .factories.email.emitter import provide_saq_email_emitter
from .factories.persistence.sqlalchemy import (
    provide_alchemy_client,
    provide_alchemy_transaction,
    provide_user_alchemy_repository,
)
from .factories.security.crypt import provide_passlib_crypt


def create_registry() -> Registry:
    registry = Registry()

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
