from litestar.contrib.repository.abc import AbstractAsyncRepository
from src.verdantech_api import settings
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services import VerificationService
from src.verdantech_api.domain.utils.sanitizers.object import ObjectSanitizer
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter

from ..schemas.api.write import UserCreateInput
from ..services.sanitization.password import (
    PasswordInputMismatch,
    validate_password_match,
)


class UserWriteOperations:
    def __init__(self, user_repo: AbstractAsyncRepository):
        self.user_repo = user_repo

    async def create(
        self,
        data: UserCreateInput,
        user_sanitizer: ObjectSanitizer,
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
        validate_password_match(password1=data.password1, password2=data.password2)

        sanitized_data = user_sanitizer.sanitize(
            input={
                "username": data.username,
                "email_address": data.email_address,
                "password": data.password1,
            }
        )

        user = User(username=sanitized_data["username"])
        user.set_password(
            password=sanitized_data["password"], password_crypt=password_crypt
        )

        if True:  # Todo: email verification setting
            key = await VerificationService.generate_open_email_confirmation_key(
                length=settings.EMAIL_VERIFICATION_KEY_LENGTH, user_repo=self.user_repo
            )
            user.add_email(
                address=sanitized_data["email_address"],
                primary=True,
                key=key,
            )
        else:
            user.add_verified_email(
                address=sanitized_data["email_address"], primary=True
            )

        user = await self.user_repo.add(user)

        email_emitter(
            receiver=sanitized_data["email_address"],
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
