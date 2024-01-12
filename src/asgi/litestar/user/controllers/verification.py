
# External Libraries
from litestar import Controller, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.exceptions import litestar_exception_map
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.user.controllers import UserVerificationOpsController
from src.ops.user.schemas import verification as verification_ops_schemas

from .. import routes, urls


class UserVerificationApiController(Controller):
    """
    User email and password verification ASGI controller.
    """

    path = urls.USER_VERIFICATION_CONTROLLER_BASE

    @post(
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        name=routes.USER_EMAIL_VERIFICATION_REQUEST_NAME,
        opt={"exclude_from_auth": True},
        summary="Email confirmation request",
        description="Create a new email confirmation and send confirmation email.",
        operation_id=routes.USER_EMAIL_VERIFICATION_REQUEST_NAME,
        tags=["users"],
    )
    async def user_email_confirmation_request(
        self,
        data: verification_ops_schemas.UserVerifyEmailRequestInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the email confirmation request application operation.

        Args:
            data (UserVerifyEmailRequestInput): input DTO.
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        svcs_container.register_local_value(State, state)
        user_verification_ops_controller, user_sanitizer = await svcs_container.aget(
            UserVerificationOpsController, UserSanitizer
        )
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)
        with litestar_exception_map():
            await user_verification_ops_controller.email_confirmation_request(
                data=data, user_sanitizer=user_sanitizer, email_emitter=email_emitter
            )

    @post(
        path=urls.USER_EMAIL_VERIFICATION_CONFIRM_URL,
        name=routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME,
        opt={"exclude_from_auth": True},
        summary="Email confirmation confirm.",
        description="Close email confirmation and verify email.",
        operation_id=routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME,
        tags=["users"],
    )
    async def user_email_confirmation_confirm(
        self,
        data: verification_ops_schemas.UserVerifyEmailConfirmInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the email confirmation confirm application operation.

        Args:
            data (UserVerifyEmailConfirmInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        svcs_container.register_local_value(State, state)
        user_verification_ops_controller, user_sanitizer = await svcs_container.aget(
            UserVerificationOpsController, UserSanitizer
        )
        with litestar_exception_map():
            await user_verification_ops_controller.email_confirmation_confirm(
                data=data, user_sanitizer=user_sanitizer
            )

    @post(
        path=urls.USER_PASSWORD_RESET_REQUEST_URL,
        name=routes.USER_PASSWORD_RESET_REQUEST_NAME,
        opt={"exclude_from_auth": True},
        summary="Password reset request",
        description="Open a new password reset request and send confirmation email",
        operation_id=routes.USER_PASSWORD_RESET_REQUEST_NAME,
        tags=["users"],
    )
    async def user_password_reset_request(
        self,
        data: verification_ops_schemas.UserPasswordResetRequestInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the password reset request application operation.

        Args:
            data (UserPasswordResetRequestInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        svcs_container.register_local_value(State, state)
        user_verification_ops_controller, user_sanitizer = await svcs_container.aget(
            UserVerificationOpsController, UserSanitizer
        )
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)
        with litestar_exception_map():
            await user_verification_ops_controller.password_reset_request(
                data=data,
                user_sanitizer=user_sanitizer,
                email_emitter=email_emitter,
            )

    @post(
        path=urls.USER_PASSWORD_RESET_CONFIRM_URL,
        name=routes.USER_PASSWORD_RESET_CONFIRM_NAME,
        opt={"exclude_from_auth": True},
        summary="Password reset confirm",
        description="Close a password reset request and change password",
        operation_id=routes.USER_PASSWORD_RESET_CONFIRM_NAME,
        tags=["users"],
    )
    async def user_password_reset_confirm(
        self,
        data: verification_ops_schemas.UserPasswordResetConfirmInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the password reset confirmation application operation.

        Args:
            data (UserPasswordResetConfirmInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        svcs_container.register_local_value(State, state)
        user_verification_ops_controller, user_sanitizer = await svcs_container.aget(
            UserVerificationOpsController, UserSanitizer
        )
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)
        with litestar_exception_map():
            await user_verification_ops_controller.password_reset_confirm(
                data=data, user_sanitizer=user_sanitizer, password_crypt=password_crypt
            )
