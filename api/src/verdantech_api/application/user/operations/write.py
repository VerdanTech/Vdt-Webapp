from src.verdantech_api import settings
from src.verdantech_api.domain.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services import EmailAdditionService
from src.verdantech_api.domain.models.user.services.sanitization import UserSanitizer
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter

from ..schemas.api.write import UserCreateInput
from ..services.email.verification import EmailVerificationService
from ..services.sanitization.values.user_create import sanitize_user_create


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
        sanitized_data = sanitize_user_create(data=data, user_sanitizer=user_sanitizer)

        user = User(username=sanitized_data["username"])
        user.set_password(
            password=sanitized_data["password"], password_crypt=password_crypt
        )
        if settings.REQUIRE_EMAIL_VERIFICATION:
            key = await EmailAdditionService.add_first_email_verification_required(
                user=user,
                address=sanitized_data["email_address"],
                key_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
                user_repo=self.user_repo,
            )
            await EmailVerificationService.emit_email_verification_email(
                email_address=user.emails[0].address,
                username=user.username,
                key=key,
                email_emitter=email_emitter,
            )
        else:
            EmailAdditionService.add_first_email_verification_not_required(
                user=user, address=sanitized_data["email_address"]
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
