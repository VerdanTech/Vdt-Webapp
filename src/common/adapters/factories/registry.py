# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Registry

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy import AlchemyClient
from src.common.interfaces.email import AbstractEmailClient
from src.common.interfaces.email import AbstractEmailEmitter
from src.common.interfaces.persistence.repository import AbstractUow
from src.common.interfaces.security.crypt import AbstractPasswordCrypt

from .email.client import provide_aiosmtplib_client
from .email.emitter import provide_saq_email_emitter
from .persistence.sqlalchemy import (
    provide_alchemy_client,
    provide_alchemy_uow,
)
from .security.crypt import provide_passlib_crypt


def create_registry() -> Registry:
    registry = Registry()

    # ======================================
    # PERSISTENCE
    # ======================================

    # SqlAlchemy
    registry.register_factory(AlchemyClient, provide_alchemy_client)
    registry.register_factory(AbstractUow, provide_alchemy_uow)

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
