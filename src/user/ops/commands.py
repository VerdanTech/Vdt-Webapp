# External Libraries
from svcs import Container

# VerdanTech Source
from src import exceptions, settings
from src.common.interfaces.persistence import AbstractUow
from src.common.interfaces.security import AbstractPasswordCrypt
from src.common.ops.processors import asgi_processor
from src.user.domain import User, commands, events


@asgi_processor.add_command()
async def create_user(
    command: commands.UserCreateCommand,
    svcs_container: Container,
    client: None = None,
) -> None:
    """
    Main user creation operation.

    Args:
        command (commands.UserCreateCommand): user creation command.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, password_crypt = await svcs_container.aget_abstract(
        AbstractUow, AbstractPasswordCrypt
    )

    async with uow:
        # Validate command against database state ie., existing fields
        await command.validate_against_uow(uow=uow)

        # Create a new user
        user = User(username=command.username)

        # Set the user's password
        await user.set_password(
            password=command.password1.get_secret_value(), password_crypt=password_crypt
        )

        # Set the user's email address
        user.email_create(
            address=command.email_address,
            max_emails=settings.USER_MAX_EMAILS,
            verification=True,
        )

        # Persist user
        user = await uow.repos.users.add(user)
        await uow.commit()
        user.events.append(
            events.UserCreatedEvent(
                userid=user.id_or_error(),
                username=user.username,
                email_address=command.email_address,
            )
        )


@asgi_processor.add_command()
async def update_user(
    command: commands.UserUpdateCommand,
    svcs_container: Container,
    client: User | None = None,
) -> None:
    """
    User username, email, and password update operation.

    Args:
        command (commands.UserUpdateCommand): user update command.
        svcs_container (Container): service locator.
    """
    if client is None:
        raise exceptions.AuthenticationError(
            "Client set to non on an authenticated route."
        )

    # Locate services
    uow, password_crypt = await svcs_container.aget_abstract(
        AbstractUow, AbstractPasswordCrypt
    )

    async with uow:
        # Validate command against database state ie., existing fields
        await command.validate_against_uow(uow=uow)

        # Authenticate password
        if not await client.verify_password(
            password=command.password.get_secret_value(), password_crypt=password_crypt
        ):
            raise exceptions.AuthenticationError(
                field_errors=[("password", "Incorrect password")]
            )

        # Update the requested fields
        if command.new_username:
            client.username = command.new_username

        if command.new_email_address:
            client.email_create(
                address=command.new_email_address,
                max_emails=settings.USER_MAX_EMAILS,
                verification=settings.EMAIL_CONFIRMATION.verification_required,
            )

        if command.new_password1:
            await client.set_password(
                password=command.new_password1.get_secret_value(),
                password_crypt=password_crypt,
                overwrite=True,
            )

        # Persist user
        await uow.repos.users.update(client)
        await uow.commit()


@asgi_processor.add_command()
async def request_email_confirmation(
    command: commands.UserRequestEmailConfirmationCommand, svcs_container: Container
) -> None:
    """
    Given an unverified email, create a new email confirmation,
    and send an email confirmation email.

    Args:
        command (commands.UserRequestEmailConfirmationCommand): email confirmation request command.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Retrieve user from persistence
        user = await uow.repos.users.get_by_email_address(
            email_address=command.email_address
        )
        if user is None:
            raise exceptions.NotFoundError(
                field_errors=[("email_address", "The email address does not exist.")]
            )

        # Request a new email confirmation
        user.events.append(
            events.EmailPendingConfirmationEvent(
                username=user.username, email_address=command.email_address
            )
        )


@asgi_processor.add_command()
async def confirm_email_confirmation(
    command: commands.UserConfirmEmailConfirmationCommand, svcs_container: Container
) -> None:
    """
    Given an email confirmation key, verify the email
    if it exists and is in a verifiable state.

    Args:
        command (commands.UserConfirmEmailConfirmationCommand): email confirmation confirm command.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Retrieve user from persistence
        user = await uow.repos.users.get_by_email_confirmation_key(key=command.key)
        if user is None:
            raise exceptions.NotFoundError(
                non_form_errors=[("This verification key does not exist.")]
            )

        # Verify email
        user.email_confirmation_confirm(
            key=command.key,
            max_emails=settings.USER_MAX_EMAILS,
            expiry_time_hours=settings.EMAIL_VERIFICATON_EXPIRY_TIME_HOURS,
        )

        # Persist user
        await uow.repos.users.update(user)
        await uow.commit()


@asgi_processor.add_command()
async def request_password_reset(
    command: commands.UserRequestPasswordResetCommand, svcs_container: Container
) -> None:
    """
    Given an email, find the user associated, open up a new
    password reset request, and emit the reset email.

    Args:
        command (commands.UserRequestPasswordResetCommand): password reset request command.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Retrieve user from persistence
        user = await uow.repos.users.get_by_email_address(
            email_address=command.email_address
        )
        if user is None:
            raise exceptions.NotFoundError(
                field_errors=[("email_address", "The email address does not exist.")]
            )

        # Validate the address provided was the user's primary email
        primary_email = user.primary_email
        if not command.email_address == primary_email.address:
            raise exceptions.NotFoundError(
                field_errors=[("email_address", "The email address does not exist.")]
            )

        # Request a new password reset
        user.events.append(
            events.PasswordPendingResetEvent(
                user_id=user.id,
                username=user.username,
                email_address=command.email_address,
            )
        )


@asgi_processor.add_command()
async def confirm_password_reset(
    command: commands.UserConfirmPasswordResetCommand, svcs_container: Container
) -> None:
    """
    Given a user ID, password confirmation key,
    and new password, find the user if it exists, validate
    the key, and set the new password.

    Args:
        command (commands.UserUpdateCommand): user password reset confirm command.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, password_crypt = await svcs_container.aget_abstract(
        AbstractUow, AbstractPasswordCrypt
    )

    async with uow:
        # Retrieve user from persistence
        user = await uow.repos.users.get_by_password_reset_confirmation(
            user_id=command.user_id, key=command.key
        )
        if user is None:
            raise exceptions.NotFoundError(
                non_form_errors=["This verification key does not exist."]
            )

        # Reset password
        await user.password_reset_confirm(
            user_id=command.user_id,
            key=command.key,
            new_password=command.new_password1.get_secret_value(),
            password_crypt=password_crypt,
        )

        # Persist user
        await uow.repos.users.update(user)
        await uow.commit()
