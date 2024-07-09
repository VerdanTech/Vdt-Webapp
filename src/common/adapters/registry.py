# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Registry

# VerdanTech Source
from src.common.adapters.email import provide_aiosmtplib_client
from src.common.adapters.events.nats import provide_nats_event_node
from src.common.adapters.persistence.common import provide_standard_uow
from src.common.adapters.persistence.sqlalchemy import (
    AlchemyClient,
    provide_alchemy_client,
)
from src.common.adapters.security import provide_passlib_crypt
from src.common.interfaces.email import AbstractEmailClient
from src.common.interfaces.events import AbstractEventNode
from src.common.interfaces.persistence import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt


def create_registry() -> Registry:
    registry = Registry()

    # ======================================
    # PERSISTENCE
    # ======================================

    # Unit of work
    registry.register_factory(AbstractUow, provide_standard_uow)

    # SqlAlchemy
    registry.register_factory(AlchemyClient, provide_alchemy_client)

    # ======================================
    # EVENTS
    # ======================================

    # Event node
    registry.register_factory(AbstractEventNode, provide_nats_event_node)

    # ======================================
    # EMAIL
    # ======================================

    # Client
    registry.register_factory(AbstractEmailClient, provide_aiosmtplib_client)

    # ======================================
    # SECURITY
    # ======================================

    registry.register_factory(AbstractPasswordCrypt, provide_passlib_crypt)

    return registry
