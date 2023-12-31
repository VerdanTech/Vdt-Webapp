# External Libraries
from svcs import Container

# VerdanTech Source
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.ops.user.controllers import verification, write


async def provide_user_auth_ops(
    svcs_container: Container,
) -> auth.UserAuthOpsController:
    """
    Provide the user auth operations controller for dependency injection.
    """
    user_repo = await svcs_container.aget_abstract(AbstractUserRepository)
    return auth.UserAuthOpsController(user_repo=user_repo)


async def provide_user_write_ops(
    svcs_container: Container,
) -> write.UserWriteOpsController:
    """
    Provide the user write operations controller for dependency injection.
    """
    user_repo = await svcs_container.aget_abstract(AbstractUserRepository)
    return write.UserWriteOpsController(user_repo=user_repo)


async def provide_user_verification_ops(
    svcs_container: Container,
) -> verification.UserVerificationOpsController:
    """
    Provide the user verification operations controller for dependency injection.
    """
    user_repo = await svcs_container.aget_abstract(AbstractUserRepository)
    return verification.UserVerificationOpsController(user_repo=user_repo)
