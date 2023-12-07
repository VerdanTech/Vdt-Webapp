# VerdanTech Source
from src.interfaces.persistence.user.repository import AbstractUserRepository

from .controllers import write


async def provide_user_write_ops(
    user_repo: AbstractUserRepository,
) -> write.UserWriteOpsController:
    """
    Provide the user write operations controller for dependency injection.
    """
    return write.UserWriteOpsController(user_repo=user_repo)
