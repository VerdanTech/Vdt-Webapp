from litestar.contrib.repository.abc import AbstractAsyncRepository

from .write import UserWriteOperations


def provide_user_write_operations(user_repo: AbstractAsyncRepository):
    return UserWriteOperations(user_repo=user_repo)
