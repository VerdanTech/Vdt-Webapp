# External Libraries
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.interfaces.email.client import AbstractEmailClient
from src.common.interfaces.events import AbstractEventNode
from src.common.interfaces.persistence import AbstractUow
from src.common.ops.processors import asgi_processor, task_processor
from src.user.domain import events
from src.utils.key_generator import generate_unique_key


@asgi_processor.add_event()
async def process_email_confirmation(
    event: events.EmailPendingConfirmation, svcs_container: Container
) -> None:
    """
    Creates a new email confirmation and queues an email notification.

    Args:
        event (events.EmailPendingConfirmation): pending confirmation event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, event_node = await svcs_container.aget_abstract(AbstractUow, AbstractEventNode)

    async with uow:
        # Generate an email confirmation key if verification is True
        key = await generate_unique_key(
            length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            repo=uow.users,
            existence_method_name="email_confirmation_key_exists",
            existence_method_argument_name="key",
        )

        # Emit the email sending event to the task backend
        await event_node.emit(
            events.EmailConfirmationCreated(
                email_address=event.email_address, username=event.username, key=key
            ),
            subject="general_domain_events",
        )


@asgi_processor.add_event()
async def process_password_reset(
    event: events.PasswordPendingReset, svcs_container: Container
) -> None:
    """
    Creates a new password reset and queues an email notification.

    Args:
        event (events.PasswordPendingReset): pending reset confirmation event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, event_node = await svcs_container.aget_abstract(AbstractUow, AbstractEventNode)

    async with uow:
        # Generate an email confirmation key if verification is True
        key = await generate_unique_key(
            length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            repo=uow.users,
            existence_method_name="password_reset_confirmation_key_exists",
            existence_method_argument_name="key",
        )

        # Emit the email sending event to the task backend
        await event_node.emit(
            events.PasswordResetConfirmationCreated(
                user_id=event.user_id,
                email_address=event.email_address,
                username=event.username,
                key=key,
            ),
            subject="general_domain_events",
        )


@task_processor.add_event()
async def send_email_confirmation(
    event: events.EmailConfirmationCreated, svcs_container: Container
) -> None:
    """
    Sends an email confirmation email.

    Args:
        event (events.EmailConfirmationCreated): email confirmation created event.
        svcs_container (Container): service locator.
    """
    # Locate services
    email_client = await svcs_container.aget_abstract(AbstractEmailClient)

    # Send the email
    await email_client.compile_and_send(
        filepath=settings.EMAIL_FILEPATH_EMAIL_CONFIRMATION,
        receiver=event.email_address,
        subject=settings.EMAIL_SUBJECT_EMAIL_CONFIRMATION,
        username=event.username,
        client_base_url=settings.CLIENT_BASE_URL,
        verification_url=settings.CLIENT_EMAIL_VERIFICATION_URL + event.key,
    )


@task_processor.add_event()
async def send_password_reset(
    event: events.PasswordResetConfirmationCreated, svcs_container: Container
) -> None:
    """
    Sends a password reset email.

    Args:
        event (events.PasswordResetConfirmationCreated): password reset created event.
        svcs_container (Container): service locator.
    """
    # Locate services
    email_client = await svcs_container.aget_abstract(AbstractEmailClient)

    # Send the email
    await email_client.compile_and_send(
        filepath=settings.EMAIL_FILEPATH_EMAIL_CONFIRMATION,
        receiver=event.email_address,
        subject=settings.EMAIL_SUBJECT_EMAIL_CONFIRMATION,
        user_id=event.user_id,
        username=event.username,
        client_base_url=settings.CLIENT_BASE_URL,
        verification_url=settings.CLIENT_EMAIL_VERIFICATION_URL + event.key,
    )
