# Standard Library
import pdb

# External Libraries
from litestar import Controller, Response, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.exceptions import ClientError, litestar_exception_map
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
    tags = ["users"]

    @post(
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        name=routes.USER_EMAIL_VERIFICATION_REQUEST_NAME,
        opt={"exclude_from_auth": True},
        summary="Email confirmation request.",
        description="Requests a new email verification email be sent to the email address.",
        response_description="An email confirmation has been sent to the address.",
        raises=[ClientError],
        operation_id=routes.USER_EMAIL_VERIFICATION_REQUEST_NAME,
    )
    async def user_email_confirmation_request(
        self,
        data: verification_ops_schemas.UserVerifyEmailRequestInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
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
        return Response(content="An email confirmation has been sent to the address.")

    @post(
        path=urls.USER_EMAIL_VERIFICATION_CONFIRM_URL,
        name=routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME,
        opt={"exclude_from_auth": True},
        summary="Email confirmation.",
        description="Closes an email confirmation and verifies the email address.",
        response_description="The email has been verified.",
        raises=[ClientError],
        operation_id=routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME,
    )
    async def user_email_confirmation_confirm(
        self,
        data: verification_ops_schemas.UserVerifyEmailConfirmInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
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
        return Response(content="The email has been verified.")

    @post(
        path=urls.USER_PASSWORD_RESET_REQUEST_URL,
        name=routes.USER_PASSWORD_RESET_REQUEST_NAME,
        opt={"exclude_from_auth": True},
        summary="Password reset request.",
        description="Open a new password reset request and sends confirmation email.",
        response_description="A password reset confirmation has been sent to the email address, if it exists.",
        operation_id=routes.USER_PASSWORD_RESET_REQUEST_NAME,
    )
    async def user_password_reset_request(
        self,
        data: verification_ops_schemas.UserPasswordResetRequestInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
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
        return Response(
            content="A password reset confirmation has been sent to the email address, if it exists."
        )

    @post(
        path=urls.USER_PASSWORD_RESET_CONFIRM_URL,
        name=routes.USER_PASSWORD_RESET_CONFIRM_NAME,
        opt={"exclude_from_auth": True},
        summary="Password reset confirm.",
        description="Closes a password reset request and changes the password",
        response_description="The password has been successfully updated.",
        operation_id=routes.USER_PASSWORD_RESET_CONFIRM_NAME,
    )
    async def user_password_reset_confirm(
        self,
        data: verification_ops_schemas.UserPasswordResetConfirmInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
        """
        Calls the password reset confirmation application operation.

        Args:
            data (UserPasswordResetConfirmInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        pdb.set_trace()
        svcs_container.register_local_value(State, state)
        user_verification_ops_controller, user_sanitizer = await svcs_container.aget(
            UserVerificationOpsController, UserSanitizer
        )
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)
        with litestar_exception_map():
            await user_verification_ops_controller.password_reset_confirm(
                data=data, user_sanitizer=user_sanitizer, password_crypt=password_crypt
            )
        return Response(content="The password has been successfully updated.")
