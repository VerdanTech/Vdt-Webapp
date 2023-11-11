from src.interfaces.persistence.user.repository import AbstractUserRepository


class UserReadOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def list():
        pass

    async def detail():
        pass

    async def check_username():
        pass

    async def check_email():
        pass

    async def check_password():
        pass
