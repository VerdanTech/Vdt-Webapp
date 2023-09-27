from litestar import Controller, post
from src.verdantech_api.api.exceptions import litestar_exception_map
from src.verdantech_api.application.user.operations import UserVerificationOperations
from src.verdantech_api.application.user.schemas.api.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailConfirmInput,
    UserVerifyEmailRequestInput,
)
from src.verdantech_api.domain.interfaces.security.crypt.password_crypt import (
    AbstractPasswordCrypt,
)
from src.verdantech_api.domain.models.user.services.sanitization import UserSanitizer
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter

from ..urls import urls


class UserVerificationController(Controller):
    """User verification controller"""

    dependencies = {"user_repo": "", "user_verification_operations": ""}

    @post(
        name="users:email_verify_request",
        summary="Email verification request",
        description="Open new email confirmation and send confirmation email",
        tags=["users"],
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        dto=UserVerifyEmailRequestInput,
        dependencies={"user_sanitizer": "", "email_emitter": ""},
    )
    async def user_email_verification_request(
        self,
        data: UserVerifyEmailRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
        user_verification_operations: UserVerificationOperations,
    ):
        """Call the email confirmation request application operation

        Args:
            data (UserVerifyEmailRequestInput): input DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            email_emitter (EmailEmitter): email emitter awaitable
            user_verification_operations (UserVerificationOperations):
                application operations
        """
        async with litestar_exception_map:
            await user_verification_operations.email_verification_request(
                data=data, user_sanitizer=user_sanitizer, email_emitter=email_emitter
            )

    @post(
        name="users:email_verify_confirm",
        summary="Email verification confirmation",
        description="Close email confirmation and verify email",
        tags=["users"],
        path=urls.USER_EMAIL_VERIFICATION_CONFIRM_URL,
        dto=UserVerifyEmailConfirmInput,
    )
    async def user_email_verification_confirm(
        self,
        data: UserVerifyEmailConfirmInput,
        user_verification_operations: UserVerificationOperations,
    ) -> None:
        """Call the email verification confirmation application operation

        Args:
            data (UserVerifyEmailConfirmInput): input DTO
            user_verification_operations (UserVerificationOperations):
                application operations
        """
        async with litestar_exception_map:
            await user_verification_operations.email_verification_confirm(data=data)

    @post(
        name="users:password_reset_request",
        summary="Password reset request",
        description="Open a new password reset request and send confirmation email",
        tags=["users"],
        path=urls.USER_PASSWORD_RESET_REQUEST_URL,
        dto=UserPasswordResetRequestInput,
        dependencies={"user_sanitizer": "", "email_emitter": ""},
    )
    async def user_password_reset_request(
        self,
        data: UserPasswordResetRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
        user_verification_operations: UserVerificationOperations,
    ) -> None:
        """Call the password reset request application operation

        Args:
            data (UserPasswordResetRequestInput): input DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            email_emitter (EmailEmitter): email emitter awaitable
            user_verification_operations (UserVerificationOperations):
                application operations
        """
        async with litestar_exception_map:
            await user_verification_operations.password_reset_request(
                data=data,
                user_sanitizer=user_sanitizer,
                email_emitter_email=email_emitter,
            )

    @post(
        name="users:password_reset_confirm",
        summary="Password reset confirm",
        description="Close a password reset request and change password",
        tags=["users"],
        path=urls.USER_PASSWORD_RESET_CONFIRM_URL,
        dto=UserPasswordResetConfirmInput,
        dependencies={"user_sanitizer": "", "password_crypt": ""},
    )
    async def user_password_reset_confirm(
        self,
        data: UserPasswordResetConfirmInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
        user_verification_operations: UserVerificationOperations,
    ):
        """Call the password reset confirm application operation

        Args:
            data (UserPasswordResetConfirmInput): input DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            password_crypt (AbstractPasswordCrypt): password encryption inteface
            user_verification_operations (UserVerificationOperations):
                application operations
        """
        async with litestar_exception_map:
            await user_verification_operations.password_reset_confirm(
                data=data, user_sanitizer=user_sanitizer, password_crypt=password_crypt
            )
