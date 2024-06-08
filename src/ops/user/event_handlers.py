# External Libraries
from svcs import Container

# VerdanTech Source
from src import settings
from src.domain.user import events
from src.interfaces.persistence.common import AbstractUow
from src.utils.key_generator import generate_unique_key


async def send_email_confirmation(
    event: events.EmailPendingConfirmation, svcs_container: Container
) -> None:
    """
    Sends an email confirmation email.

    Args:
        event (events.EmailPendingConfirmation): pending confirmation event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Generate an email confirmation key if verification is True
        key = await generate_unique_key(
            length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            repo=uow.users,
            existence_method_name="email_confirmation_key_exists",
            existence_method_argument_name="key",
        )

        # await email_emitter.emit_user_email_confirmation(
        # email_address=address, username=user.username, key=key
        # )


async def send_password_reset(
    event: events.PasswordPendingReset, svcs_container: Container
) -> None:
    """
    Sends an password reset email.

    Args:
        event (events.PasswordPendingReset): pending reset confirmation event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Generate an email confirmation key if verification is True
        key = await generate_unique_key(
            length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            repo=uow.users,
            existence_method_name="password_reset_confirmation_key_exists",
            existence_method_argument_name="key",
        )

        # await email_emitter.emit_user_email_confirmation(
        # email_address=address, username=user.username, key=key
        # )


USER_ASGI_EVENT_HANDLERS = {
    events.UserCreated: [],
    events.EmailPendingConfirmation: [send_email_confirmation],
    events.PasswordPendingReset: [send_password_reset],
    events.UserUpdated: [],
}
