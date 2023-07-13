from typing import TYPE_CHECKING

from pydantic import SecretStr

if TYPE_CHECKING:
    from src.verdantech_api.lib.crypt.generic import PasswordCrypt

    from ..services.user import UserService
    from ..services.validation import UserFieldsSanitizerService
    from ..services.verifictaion import VerificationService


class UserWriteOperations:
    def __init__(
        self,
        user_fields_sanitizer_service: UserFieldsSanitizerService,
        user_service: UserService,
        verification_service: VerificationService,
        password_crypt: PasswordCrypt,
    ):
        self.user_fields_sanitizer_service = user_fields_sanitizer_service
        self.user_service = user_service
        self.verification_service = verification_service
        self.password_crypt = password_crypt

    async def create(self, username: str, email: str, password1: str, password2: str):
        # Validate fields
        username, email, password = self.user_fields_sanitizer.sanitize_fields(
            username=username, email=email, password1=password1, password2=password2
        )

        # Generate hashed password
        hashed_password: SecretStr = await self.password_crypt.get_password_hash(
            password1
        )

        user, email = self.user_service.create_new_user(
            username=username, email=email, hashed_password=hashed_password
        )

        # Send email verification
        await self.verification_service.emit_email_verification(email=email)

        return user

    async def email_change():
        pass

    async def user_change():
        pass

    async def delete():
        pass
