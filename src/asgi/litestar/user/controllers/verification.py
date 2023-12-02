# External Libraries
from backend.src.domain.user.services.sanitizers import UserSanitizer
from litestar import Controller, post

# VerdanTech Source
from src import settings
from src.asgi.litestar import dependencies
from src.asgi.litestar.exceptions import litestar_exception_map
from src.infra.email.litestar_emitter import EmailEmitter
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.user.controllers import UserVerificationOpsController
from src.ops.user.schemas.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailConfirmInput,
    UserVerifyEmailRequestInput,
)

from .. import urls


class UserVerificationController(Controller):
    """User verification controller"""

    path = urls.USER_VERIFICATION_CONTROLLER_BASE
    # dependencies = dependencies.select(
    # settings.USER_REPOSITORY_PK, settings.USER_VERIFICATION_OP_PK
    # )

    @post(
        name="users:email_verify_request",
        summary="Email verification request",
        description="Open new email confirmation and send confirmation email",
        tags=["users"],
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        # dependencies=providers.select(
        # settings.USER_SANITIZER_PK,
        # settings.EMAIL_CLIENT_PK,
        # settings.EMAIL_EMITTER_PK,
        # ),
    )
    async def user_email_verification_request(
        self,
        data: UserVerifyEmailRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
        user_verification_operations: UserVerificationOpsController,
    ) -> None:
        """Call the email confirmation request application operation

        Args:
            data (UserVerifyEmailRequestInput): input DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            email_emitter (EmailEmitter): email emitter awaitable
            user_verification_operations (UserVerificationOpsController):
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
    )
    async def user_email_verification_confirm(
        self,
        data: UserVerifyEmailConfirmInput,
        user_verification_operations: UserVerificationOpsController,
    ) -> None:
        """Call the email verification confirmation application operation

        Args:
            data (UserVerifyEmailConfirmInput): input DTO
            user_verification_operations (UserVerificationOpsController):
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
        # dependencies=providers.select(
        # settings.USER_SANITIZER_PK,
        # settings.EMAIL_CLIENT_PK,
        # settings.EMAIL_EMITTER_PK,
        # ),
    )
    async def user_password_reset_request(
        self,
        data: UserPasswordResetRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
        user_verification_operations: UserVerificationOpsController,
    ) -> None:
        """Call the password reset request application operation

        Args:
            data (UserPasswordResetRequestInput): input DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            email_emitter (EmailEmitter): email emitter awaitable
            user_verification_operations (UserVerificationOpsController):
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
        # dependencies=providers.select(
        # settings.USER_SANITIZER_PK, settings.PASSWORD_CRYPT_PK
        # ),
    )
    async def user_password_reset_confirm(
        self,
        data: UserPasswordResetConfirmInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
        user_verification_operations: UserVerificationOpsController,
    ) -> None:
        """Call the password reset confirm application operation

        Args:
            data (UserPasswordResetConfirmInput): input DTO
            user_sanitizer (UserSanitizer): user object sanitizer
            password_crypt (AbstractPasswordCrypt): password encryption inteface
            user_verification_operations (UserVerificationOpsController):
                application operations
        """
        async with litestar_exception_map:
            await user_verification_operations.password_reset_confirm(
                data=data, user_sanitizer=user_sanitizer, password_crypt=password_crypt
            )
