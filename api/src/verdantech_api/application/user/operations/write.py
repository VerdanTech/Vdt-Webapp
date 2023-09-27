from src.verdantech_api import settings
from src.verdantech_api.domain.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services.sanitization import UserSanitizer
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter

from ..schemas.api.write import UserCreateInput
from ..services.email.addition import add_first_email
from ..services.sanitization.inputs import sanitize_user_create


class UserWriteOperations:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def create(
        self,
        data: UserCreateInput,
        user_sanitizer: UserSanitizer,
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
        sanitized_data = await sanitize_user_create(
            data=data, user_sanitizer=user_sanitizer
        )

        user = User(username=sanitized_data["username"])
        await user.set_password(
            password=sanitized_data["password"], password_crypt=password_crypt
        )
        await add_first_email(
            user=user,
            email_address=sanitized_data["email_address"],
            require_email_verification=settings.REQUIRE_EMAIL_VERIFICATION,
            verification_key_length=settings.VERIFICATION_KEY_MAX_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        user = await self.user_repo.add(user)

        return user

    async def email_change():
        pass

    async def username_change():
        pass

    async def password_change():
        pass

    async def delete():
        pass
