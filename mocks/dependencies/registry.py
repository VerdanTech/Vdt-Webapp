# Standard Library
from unittest import mock

# External Libraries
from svcs import Registry

# VerdanTech Source
from src.dependencies.factories.ops.user.controllers import (
    provide_user_auth_ops,
    provide_user_verification_ops,
    provide_user_write_ops,
)
from src.dependencies.factories.ops.user.sanitizers import provide_user_sanitizer
from src.user.domain import UserSanitizer
from src.common.interfaces.email import AbstractEmailEmitter
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user import controllers as user_ops

from .factories.infra.persistence.repository import provide_user_mock_repository
from .factories.infra.security.crypt import provide_mock_crypt


def configure_registry() -> Registry:
    mock_registry = Registry()

    # ======================================
    # OPERATIONS CONTROLLERS
    # ======================================

    # User
    mock_registry.register_factory(
        user_ops.UserAuthOpsController, provide_user_auth_ops
    )
    mock_registry.register_factory(
        user_ops.UserWriteOpsController, provide_user_write_ops
    )
    mock_registry.register_factory(
        user_ops.UserVerificationOpsController, provide_user_verification_ops
    )

    # ======================================
    # SANITIZERS
    # ======================================

    # User
    mock_registry.register_factory(UserSanitizer, provide_user_sanitizer)

    # ======================================
    # PERSISTENCE
    # ======================================

    # Repository
    mock_registry.register_factory(AbstractUserRepository, provide_user_mock_repository)

    # ======================================
    # EMAIL
    # ======================================

    mock_registry.register_value(
        AbstractEmailEmitter, mock.MagicMock(spec=AbstractEmailEmitter)
    )

    # ======================================
    # SECURITY
    # ======================================

    mock_registry.register_factory(AbstractPasswordCrypt, provide_mock_crypt)

    return mock_registry


mock_registry = configure_registry()
