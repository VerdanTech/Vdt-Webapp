from typing import Any

from api.src.verdantech_api.lib.email.generic import AsyncEmailClient
from api.src.verdantech_api.lib.services.orm import AsyncRepoService
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from ..models import PasswordResetConfirmationModel


class PasswordResetService:
    """Handles password reset email verification"""

    def __init__(self, email_client: AsyncEmailClient):
        self.email_client: AsyncEmailClient = email_client

    async def reset_password():
        pass

    async def reset_password_confirm():
        pass
