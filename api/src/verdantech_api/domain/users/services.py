from typing import Any

from api.src.verdantech_api.lib.email.generic import AsyncEmailClient
from api.src.verdantech_api.lib.services.orm import AsyncRepoService
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from .models import UserModel


class UserRepo(SQLAlchemyAsyncRepository[UserModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = UserModel


class UserService(AsyncRepoService[UserModel]):
    """Handles database operations for users"""

    repo_type = UserRepo

    def __init__(self, **repo_kwargs: Any) -> None:
        self.repo: UserRepo = self.repo_type_(**repo_kwargs)
        self.model_type = self.repo.model_type

    async def register():
        # validate email
        # create user
        # send verification email

        pass

    async def change_password():
        pass

    async def change_username():
        pass


class EmailVerificationService:
    """Handles verification of email for new users
    and for adding/changing primary email address"""

    def __init__(self, user: UserModel, email_client: AsyncEmailClient):
        self.user: UserModel = user
        self.email_client: AsyncEmailClient = email_client

    async def send_email_verification(self):
        pass

    async def resend_email_verification():
        # send verification email

        pass

    async def verify_email():
        # validate email
        # update user object

        pass


class PasswordResetService:
    """Handles password reset email verification"""

    def __init__(self, email_client: AsyncEmailClient):
        self.email_client: AsyncEmailClient = email_client

    async def reset_password():
        pass

    async def reset_password_confirm():
        pass


class AuthService:
    pass
