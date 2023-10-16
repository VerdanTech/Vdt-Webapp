from src import settings
from src.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.domain.user.exceptions import (
    EmailConfirmationKeyNotFound,
    PasswordResetConfirmationNotFound,
    UserNotFound,
)
from src.domain.user.services.sanitization import UserSanitizer
from src.infrastructure.email.litestar_emitter import EmailEmitter

from ..schemas.api.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailConfirmInput,
    UserVerifyEmailRequestInput,
)
from ..services.email.addition import new_email_verification
from ..services.password.reset import close_password_reset, new_password_reset
from ..services.sanitization.inputs import (
    sanitize_password_reset_confirm,
    sanitize_password_reset_request,
    sanitize_verify_email_request,
)


class UserVerificationOperations:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def email_verification_request(
        self,
        data: UserVerifyEmailRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
    ) -> None:
        """Given an unverified email, create a new email confirmation,
            and send an email confirmation email

        Args:
            data (UserVerifyEmailRequestInput):
                verification request DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            email_emitter (EmailEmitter): email emitter awaitable

        Raises:
            UserNotFound: raised if no user with the email
                was found
        """
        # Sanitize input data
        sanitized_data = await sanitize_verify_email_request(
            data=data, user_sanitizer=user_sanitizer
        )

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_address(
            email_address=sanitized_data["email_address"]
        )
        if user is None:
            raise UserNotFound("The email does not exist")

        # Add new email verification
        await new_email_verification(
            user=user,
            address=sanitized_data["email_address"],
            key_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        # Persist user
        await self.user_repo.update(user)

    async def email_verification_confirm(
        self, data: UserVerifyEmailConfirmInput
    ) -> None:
        """Given an email verification key, verify the email
            if it exists and is in a verifiable state

        Args:
            data (UserVerifyEmailConfirmInput):
                verification key DTO

        Raises:
            EmailConfirmationKeyNotFound: raised if no user
                with matching email confirmation found
        """
        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_confirmation_key(
            email_confirmation_key=data.key
        )
        if user is None:
            raise EmailConfirmationKeyNotFound(
                "The email verification key does not exist"
            )

        # Verify email
        user.verify_email(key=data.key)

        # Persist user
        await self.user_repo.update(user)

    async def password_reset_request(
        self,
        data: UserPasswordResetRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
    ) -> None:
        """Given an email, find the user associated, open up a new
            password reset request, and send the reset email

        Args:
            data (UserPasswordResetRequestInput): password reset
                request DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            email_emitter (EmailEmitter): email emitter awaitable

        Raises:
            UserNotFound: raised if a user with the email
                is nof found
        """
        # Sanitize input data
        sanitized_data = await sanitize_password_reset_request(
            data=data, user_sanitizer=user_sanitizer
        )

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_address(
            email_address=sanitized_data["email_address"]
        )
        if user is None:
            raise UserNotFound("The email does not exist")

        # Add new password reset confirmation
        await new_password_reset(
            user=user,
            address=sanitized_data["email_address"],
            key_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        # Persist user
        await self.user_repo.update(user)

    async def password_reset_confirm(
        self,
        data: UserPasswordResetConfirmInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
    ):
        """Given a user ID, password confirmation key, old password
            and new password, find the user if it exists, validate
            the old password, and set the new password

        Args:
            data (UserPasswordResetConfirmInput): password
                reset confirm DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            password_crypt (AbstractPasswordCrypt): password
                encryption service

        Raises:
            PasswordResetConfirmationNotFound: raised if the
                reset confirmation details fail to specify
                an existing user
        """
        # Sanitize input data
        sanitized_data = await sanitize_password_reset_confirm(
            data=data, user_sanitizer=user_sanitizer
        )

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_password_reset_confirmation(
            user_id=data.user_id, password_reset_confirmation_key=data.key
        )
        if user is None:
            raise PasswordResetConfirmationNotFound("The password reset does not exist")

        # Reset password
        await close_password_reset(
            user=user,
            old_password=data.old_password,
            new_password=sanitized_data["password"],
            password_crypt=password_crypt,
        )

        # Persist user
        await self.user_repo.update(user)
