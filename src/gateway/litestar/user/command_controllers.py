# External Libraries
from litestar import Controller, Response, post, status_codes
from litestar.datastructures import State

# VerdanTech Source
from src import settings
from src.domain.user import commands
from src.gateway.litestar.auth import jwt_cookie_auth
from src.gateway.litestar.exceptions import ClientError, litestar_exception_map
from src.interfaces.persistence.common import AbstractUow
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.common import MessageBus
from src.ops.exceptions import EntityNotFound

from . import urls
from src.gateway.litestar.utils import url_to_route_name


class UserCommandController(Controller):
    """
    User ASGI controller.
    """

    path = urls.USER_COMMAND_CONTROLLER_BASE
    tags = ["users"]

    @post(
        path=urls.USER_CREATE_URL,
        name=url_to_route_name(urls.USER_CREATE_URL),
        opt={"exclude_from_auth": True},
        summary="User registration.",
        description=f"Registers a new user. Requires email confirmation: {settings.EMAIL_CONFIRMATION.verification_required}.",
        operation_id=url_to_route_name(urls.USER_CREATE_URL),
    )
    async def user_create(
        self, data: commands.CreateUser, state: State, bus: MessageBus
    ) -> None:
        """
        Calls the user creation application operation.

        Args:
            data (CreateUser): input command.
            state (State): Litestar global app satte.
            svcs_container (Container): service locator.
        """
        bus.svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await bus.handle(message=data)

    @post(
        path=urls.USER_LOGIN_URL,
        name=url_to_route_name(urls.USER_LOGIN_URL),
        opt={"exclude_from_auth": True},
        summary="User login",
        description="Authenticate the request with JWT cookie authentication.",
        operation_id=url_to_route_name(urls.USER_LOGIN_URL),
    )
    async def user_login(
        self, data: commands.Login, state: State, bus: MessageBus
    ) -> Response[None]:
        """
        Uses the application operation and Litestar's built in JWT auth to log
        the user in with a JWT cookie authentication scheme.

        Args:
            data (schemas.UserLoginInput): input DTO.
            state (State): litestar application state.
            svcs_container (Container): svcs service container.

        Returns:
            Response[UserFullSchema]: a response containing the success code.
        """
        bus.svcs_container.register_local_value(State, state)
        uow, password_crypt = await bus.svcs_container.aget_abstract(
            AbstractUow, AbstractPasswordCrypt
        )
        async with uow:
            with litestar_exception_map():
                # Retrieve user from persistence
                user = await uow.users.get_user_by_email_address(
                    email_address=data.email_address
                )
                if user is None:
                    raise EntityNotFound("The email address does not exist.")

                # Todo: verify email is confirmed if settings.EMAIL_CONFIRMATION is REQUIRED_FOR_LOGIN

                # Verify password
                if await user.verify_password(
                    password=data.password, password_crypt=password_crypt
                ):
                    return jwt_cookie_auth.login(
                        identifier=str(user.id),
                        response_body=None,
                    )

                else:
                    raise ClientError(status_code=status_codes.HTTP_401_UNAUTHORIZED)

    @post(
        path=urls.USER_EMAIL_VERIFICATION_REQUEST_URL,
        name=url_to_route_name(urls.USER_EMAIL_VERIFICATION_REQUEST_URL),
        opt={"exclude_from_auth": True},
        summary="Email confirmation request.",
        description="Requests a new email verification email be sent to the email address.",
        response_description="An email confirmation has been sent to the address.",
        raises=[ClientError],
        operation_id=url_to_route_name(urls.USER_EMAIL_VERIFICATION_REQUEST_URL),
    )
    async def user_email_confirmation_request(
        self, data: commands.RequestEmailConfirmation, state: State, bus: MessageBus
    ) -> Response[str]:
        """
        Calls the email confirmation request application operation.

        Args:
            data (UserVerifyEmailRequestInput): input DTO.
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        bus.svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await bus.handle(message=data)
        return Response(content="An email confirmation has been sent to the address.")

    @post(
        path=urls.USER_EMAIL_VERIFICATION_CONFIRM_URL,
        name=url_to_route_name(urls.USER_EMAIL_VERIFICATION_CONFIRM_URL),
        opt={"exclude_from_auth": True},
        summary="Email confirmation.",
        description="Closes an email confirmation and verifies the email address.",
        response_description="The email has been verified.",
        raises=[ClientError],
        operation_id=url_to_route_name(urls.USER_EMAIL_VERIFICATION_CONFIRM_URL),
    )
    async def user_email_confirmation_confirm(
        self, data: commands.ConfirmEmailConfirmation, state: State, bus: MessageBus
    ) -> Response[str]:
        """
        Calls the email confirmation confirm application operation.

        Args:
            data (UserVerifyEmailConfirmInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        bus.svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await bus.handle(message=data)
        return Response(content="The email has been verified.")

    @post(
        path=urls.USER_PASSWORD_RESET_REQUEST_URL,
        name=url_to_route_name(urls.USER_PASSWORD_RESET_REQUEST_URL),
        opt={"exclude_from_auth": True},
        summary="Password reset request.",
        description="Open a new password reset request and sends confirmation email.",
        response_description="A password reset confirmation has been sent to the email address, if it exists.",
        operation_id=url_to_route_name(urls.USER_PASSWORD_RESET_REQUEST_URL),
    )
    async def user_password_reset_request(
        self, data: commands.RequestPasswordReset, state: State, bus: MessageBus
    ) -> Response[str]:
        """
        Calls the password reset request application operation.

        Args:
            data (UserPasswordResetRequestInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        bus.svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await bus.handle(message=data)
        return Response(
            content="A password reset confirmation has been sent to the email address, if it exists."
        )

    @post(
        path=urls.USER_PASSWORD_RESET_CONFIRM_URL,
        name=url_to_route_name(urls.USER_PASSWORD_RESET_CONFIRM_URL),
        opt={"exclude_from_auth": True},
        summary="Password reset confirm.",
        description="Closes a password reset request and changes the password",
        response_description="The password has been successfully updated.",
        operation_id=url_to_route_name(urls.USER_PASSWORD_RESET_CONFIRM_URL),
    )
    async def user_password_reset_confirm(
        self, data: commands.ConfirmPasswordReset, state: State, bus: MessageBus
    ) -> Response[str]:
        """
        Calls the password reset confirmation application operation.

        Args:
            data (UserPasswordResetConfirmInput): input DTO
            state (State): Litestar global state.
            svcs_container (Container): svcs service
                locator container.
        """
        bus.svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await bus.handle(message=data)
        return Response(content="The password has been successfully updated.")
