# External Libraries
from svcs import Container

# VerdanTech Source
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.ops.user.controllers import write


async def provide_user_write_ops(
    svcs_container: Container,
) -> write.UserWriteOpsController:
    """
    Provide the user write operations controller for dependency injection.
    """
    user_repo = await svcs_container.aget_abstract(AbstractUserRepository)
    return write.UserWriteOpsController(user_repo=user_repo)
