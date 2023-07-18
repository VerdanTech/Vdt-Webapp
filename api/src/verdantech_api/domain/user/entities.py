from typing import List

from litestar.contrib.repository.abc import AbstractAsyncRepository
from src.verdantech_api.infrastructure.security.interfaces import AbstractPasswordCrypt
from src.verdantech_api.infrastructure.validators.interfaces import AbstractObjectValidator

from ..common.entities import RootEntity
from ..garden.values import GardenMembershipRef
from .values import Email, EmailConfirmation, PasswordResetConfirmation


class User(RootEntity):
    username: str
    normalized_username: str
    hashed_password: str | None
    emails: List[Email]
    memberships: List[GardenMembershipRef]
    is_active: bool = True
    is_superuser: bool = False
    password_reset_confirmation: PasswordResetConfirmation | None

    @classmethod
    async def create_user(
        cls,
        username: str,
        email_address: str,
        password1: str,
        password2: str,
        verification_key: str,
        user_validator: AbstractObjectValidator,
        password_crypt: AbstractPasswordCrypt,
        user_repo: AbstractAsyncRepository,
    ) -> "User":

        normalized_username, normalized_email_address = cls.full_clean(username=username, email_address=email_address, password1=password1, password2=password2, user_validator=user_validator)

        user = User(
            username=username,
            normalized_username=normalized_username,
            emails=[
                Email(
                    address=normalized_email_address,
                    verified=False,
                    confirmation=EmailConfirmation(key=verification_key),
                )
            ],
        )
        user.set_password(password=password1, password_crypt=password_crypt)

        user = user_repo.add(user)

        return User
    
    @classmethod
    async def full_clean():
        pass

    @classmethod
    async def repo_check():
        pass

    async def set_password(self, password: str, password_crypt: AbstractPasswordCrypt) -> None:
        hashed_password = await password_crypt.get_password_hash(password)
        self.hashed_password = hashed_password
