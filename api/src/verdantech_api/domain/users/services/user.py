from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from ..models.models import EmailModel, UserModel
from ..models.repos import EmailRepo, UserRepo

if TYPE_CHECKING:
    from verdantech_api.lib.crypt.generic import PasswordCrypt


class UserSelector:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    async def list():
        pass

    async def detail():
        pass


class UserService:
    def __init__(self, user_repo: UserRepo, email_repo: EmailRepo):
        self.user_repo = user_repo
        self.email_repo = email_repo

    async def create_new_user(
        self, username: str, email: str, hashed_password: str
    ) -> Tuple[UserModel, EmailModel]:
        # assumes fields are validated

        # Construct models
        new_user = UserModel(username=username, password_hash=hashed_password)
        new_email = EmailModel(address=email)
        new_user.emails = {new_email}

        # Add to repos
        user = await self.user_repo.add(new_user)
        email = await self.email_repo.add(new_email)

        return user, email
