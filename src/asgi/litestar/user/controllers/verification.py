# External Libraries
from litestar import Controller, post

# VerdanTech Source
from src import providers
from src.asgi.litestar import select_dependencies
from src.asgi.litestar.exceptions import litestar_exception_map
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.user.controllers import UserVerificationOpsController
from src.ops.user.schemas import verification as schemas

from .. import urls


class UserVerificationController(Controller):
    """User verification controller"""

    path = urls.USER_VERIFICATION_CONTROLLER_BASE
    # dependencies = dependencies.select(
    # providers.USER_REPOSITORY_PK, providers.USER_VERIFICATION_OP_PK
    # )

    @post(
        name="users:email_verify_request",
        summary="Email verification request",
        description="Open new email confirmation and send confirmation email",
        tags=["users"],
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        # dependencies=providers.select(
        # providers.USER_SANITIZER_PK,
        # providers.EMAIL_CLIENT_PK,
        # providers.EMAIL_EMITTER_PK,
        # ),
    )
    async def user_email_verification_request(
        self,
        data: schemas.UserVerifyEmailRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: AbstractEmailEmitter,
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
        data: schemas.UserVerifyEmailConfirmInput,
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
        # providers.USER_SANITIZER_PK,
        # providers.EMAIL_CLIENT_PK,
        # providers.EMAIL_EMITTER_PK,
        # ),
    )
    async def user_password_reset_request(
        self,
        data: schemas.UserPasswordResetRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: AbstractEmailEmitter,
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
        # providers.USER_SANITIZER_PK, settings.PASSWORD_CRYPT_PK
        # ),
    )
    async def user_password_reset_confirm(
        self,
        data: schemas.UserPasswordResetConfirmInput,
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
