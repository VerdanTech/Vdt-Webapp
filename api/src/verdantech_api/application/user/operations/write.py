from litestar.contrib.repository.abc import AbstractAsyncRepository
from src.verdantech_api import settings
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services import VerificationService
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter
from src.verdantech_api.infrastructure.security.interfaces import AbstractPasswordCrypt

from ..schemas.write import UserCreateInput


class UserWriteOperations:
    def __init__(self, user_repo: AbstractAsyncRepository):
        self.user_repo = user_repo

    async def create(
        self,
        data: UserCreateInput,
        password_crypt: AbstractPasswordCrypt,
        email_emitter: EmailEmitter,
    ) -> User:
        """Main user creation operation

        Args:
            data (UserCreateInput): user creation data transfer object
            password_crypt (AbstractPasswordCrypt): encryption class
            email_emitter (EmailEmitter): email emit callable

        Returns:
            User: the user model created after persistence
        """
        # Validation
        normalized_username = ""
        normalized_email_address = ""
        password = ""
        key = await VerificationService.generate_open_email_confirmation_key(
            length=settings.EMAIL_VERIFICATION_KEY_LENGTH, user_repo=self.user_repo
        )

        user = User(username=data.username, username_norm=normalized_username)
        user.set_password(password=password, password_crypt=password_crypt)
        user.add_email(
            address=normalized_email_address, primary=True, verified=False, key=key
        )

        user = await self.user_repo.add(user)

        email_emitter(
            receiver=normalized_email_address,
            subject="Email verification - VerdanTech",
            filepath=settings.email_path("email_verification.html"),
            username=user.username,
            client_base_url=settings.CLIENT_BASE_URL,
            verification_url=settings.EMAIL_VERIFICATION_CLIENT_URL + key,
        )

        return user

    async def email_change():
        pass

    async def user_change():
        pass

    async def delete():
        pass
