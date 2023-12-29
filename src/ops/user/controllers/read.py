# VerdanTech Source
from src.interfaces.persistence.user.repository import AbstractUserRepository


class UserReadOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def list(self):
        pass

    async def detail(self):
        pass

    async def check_username(self):
        pass

    async def check_email(self):
        pass

    async def check_password(self):
        pass
