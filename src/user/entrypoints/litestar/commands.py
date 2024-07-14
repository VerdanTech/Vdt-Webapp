# External Libraries
from litestar import Controller, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.entrypoints.litestar.exceptions import litestar_exception_map
from src.common.entrypoints.litestar.utils import url_to_route_name
from src.common.ops.processors import asgi_processor
from src.user.domain import commands

from . import urls


class UserCommandController(Controller):
    """
    User ASGI controller.
    """

    path = urls.USER_COMMAND_CONTROLLER_BASE
    tags = ["users"]

    @post(
        path=urls.USER_CREATE_URL,
        name=url_to_route_name(urls.USER_ROUTER_URL_BASE, urls.USER_CREATE_URL),
        opt={"exclude_from_auth": True},
        summary="User registration.",
        description=f"Registers a new user. Requires email confirmation: {settings.EMAIL_CONFIRMATION.verification_required}.",
        operation_id=commands.UserCreateCommand.to_operation_id(),
    )
    async def user_create(
        self,
        data: commands.UserCreateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the user creation application command.

        Args:
            data (UserCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container
            )

    @post(
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        name=url_to_route_name(
            urls.USER_ROUTER_URL_BASE, urls.USER_EMAIL_VERIFICATION_REQUEST_URL
        ),
        opt={"exclude_from_auth": True},
        summary="Email confirmation request.",
        description="Requests a new email verification email be sent to the email address.",
        response_description="An email confirmation has been sent to the address.",
        operation_id=commands.UserRequestEmailConfirmationCommand.to_operation_id(),
    )
    async def user_request_email_confirmation(
        self,
        data: commands.UserRequestEmailConfirmationCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the email confirmation request application command.

        Args:
            data (UserRequestEmailConfirmationCommand): input command.
            state (State): Litestar global state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container
            )

    @post(
        path=urls.USER_EMAIL_VERIFICATION_CONFIRM_URL,
        name=url_to_route_name(
            urls.USER_ROUTER_URL_BASE, urls.USER_EMAIL_VERIFICATION_CONFIRM_URL
        ),
        opt={"exclude_from_auth": True},
        summary="Email confirmation.",
        description="Closes an email confirmation and verifies the email address.",
        response_description="The email has been verified.",
        operation_id=commands.UserConfirmEmailConfirmationCommand.to_operation_id(),
    )
    async def user_confirm_email_confirmation(
        self,
        data: commands.UserConfirmEmailConfirmationCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the email confirmation confirm application command.

        Args:
            data (UserConfirmEmailConfirmationCommand): input command.
            state (State): Litestar global state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container
            )

    @post(
        path=urls.USER_PASSWORD_RESET_REQUEST_URL,
        name=url_to_route_name(
            urls.USER_ROUTER_URL_BASE, urls.USER_PASSWORD_RESET_REQUEST_URL
        ),
        opt={"exclude_from_auth": True},
        summary="Password reset request.",
        description="Open a new password reset request and sends confirmation email.",
        response_description="A password reset confirmation has been sent to the email address, if it exists.",
        operation_id=commands.UserRequestPasswordResetCommand.to_operation_id(),
    )
    async def user_request_password_reset(
        self,
        data: commands.UserRequestPasswordResetCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the password reset request application command.

        Args:
            data (UserRequestPasswordResetCommand): input command
            state (State): Litestar global state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container
            )

    @post(
        path=urls.USER_PASSWORD_RESET_CONFIRM_URL,
        name=url_to_route_name(
            urls.USER_ROUTER_URL_BASE, urls.USER_PASSWORD_RESET_CONFIRM_URL
        ),
        opt={"exclude_from_auth": True},
        summary="Password reset confirm.",
        description="Closes a password reset request and changes the password",
        response_description="The password has been successfully updated.",
        operation_id=commands.UserConfirmPasswordResetCommand.to_operation_id(),
    )
    async def user_confirm_password_reset(
        self,
        data: commands.UserConfirmPasswordResetCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the password reset confirmation application command.

        Args:
            data (UserConfirmPasswordResetCommand): input command
            state (State): Litestar global state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container
            )
