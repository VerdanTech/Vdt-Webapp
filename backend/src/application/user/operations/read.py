from src.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)


class UserReadOperations:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def check_username():
        pass

    async def list():
        pass

    async def detail():
        pass
