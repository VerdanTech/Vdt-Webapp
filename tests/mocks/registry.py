# Standard Library
from unittest.mock import MagicMock

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSession
from svcs import Registry

# VerdanTech Source
from src.common.interfaces.email import AbstractEmailClient
from src.common.interfaces.events import AbstractEventNode
from src.common.interfaces.persistence import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from tests.mocks.persistence.factories import provide_mock_uow
from tests.mocks.security.factories import provide_mock_password_crypt


def create_mock_registry() -> Registry:
    registry = Registry()

    # ======================================
    # PERSISTENCE
    # ======================================

    # Unit of work
    registry.register_factory(AbstractUow, provide_mock_uow)

    # ======================================
    # EVENTS
    # ======================================

    # Event node
    registry.register_factory(
        AbstractEventNode, lambda: MagicMock(spec=AbstractEventNode)
    )

    # ======================================
    # EMAIL
    # ======================================

    # Client
    registry.register_factory(
        AbstractEmailClient, lambda: MagicMock(spec=AbstractEmailClient)
    )

    # ======================================
    # SECURITY
    # ======================================

    registry.register_factory(AbstractPasswordCrypt, provide_mock_password_crypt)

    return registry


mock_registry = create_mock_registry()
