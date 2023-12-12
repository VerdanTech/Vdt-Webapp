# External Libraries
from svcs import Registry

# VerdanTech Source
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user import controllers as user_ops

from .factories.infra.persistence.sqlalchemy import provide_user_alchemy_repository
from .factories.infra.security.crypt import provide_passlib_crypt
from .factories.ops.user.controllers import provide_user_write_ops
from .factories.ops.user.sanitizers import provide_user_sanitizer

registry = Registry()


# ======================================
# OPERATIONS CONTROLLERS
# ======================================

# User
registry.register_factory(user_ops.UserWriteOpsController, provide_user_write_ops)

# ======================================
# SANITIZERS
# ======================================

# User
registry.register_factory(UserSanitizer, provide_user_sanitizer)

# ======================================
# PERSISTENCE
# ======================================

# Repository
registry.register_factory(AbstractUserRepository, provide_user_alchemy_repository)

# ======================================
# EMAIL
# ======================================

registry.register_factory(AbstractPasswordCrypt, provide_passlib_crypt)

# ======================================
# SECURITY
# ======================================
