# Standard Library
import pdb
import uuid

# External Libraries
from svcs import Container

# VerdanTech Source
from src import exceptions, settings
from src.common.interfaces.email.client import AbstractEmailClient
from src.common.interfaces.events import AbstractEventNode
from src.common.interfaces.persistence import AbstractUow
from src.common.ops.processors import asgi_processor, task_processor
from src.user.domain import events


@asgi_processor.add_event()
async def process_email_confirmation(
    event: events.EmailPendingConfirmationEvent, svcs_container: Container
) -> None:
    """
    Creates a new email confirmation and queues an email notification.

    Args:
        event (events.EmailPendingConfirmationEvent): pending confirmation event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, event_node = await svcs_container.aget_abstract(AbstractUow, AbstractEventNode)

    async with uow:
        # Retrieve the user
        user = await uow.get_by_email(event.email_address)
        if user is None:
            raise exceptions.NotFoundError("User does not exist")

        # Generate an email confirmation key
        key = uuid.uuid4()

        # Set the email confirmation key for the user
        user.email_confirmation_create(address=event.email_address, key=key)
        await uow.update(user)
        await uow.commit()

        # Emit the email sending event to the task backend
        await event_node.emit(
            events.EmailConfirmationCreatedEvent(
                email_address=event.email_address, username=event.username, key=key
            ),
            subject="general_domain_events",
        )


@asgi_processor.add_event()
async def process_password_reset(
    event: events.PasswordPendingResetEvent, svcs_container: Container
) -> None:
    """
    Creates a new password reset and queues an email notification.

    Args:
        event (events.PasswordPendingResetEvent): pending reset confirmation event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, event_node = await svcs_container.aget_abstract(AbstractUow, AbstractEventNode)

    async with uow:
        # Generate an email confirmation key if verification is True
        key = uuid.uuid4()

        # Emit the email sending event to the task backend
        await event_node.emit(
            events.PasswordResetConfirmationCreatedEvent(
                user_id=event.user_id,
                email_address=event.email_address,
                username=event.username,
                key=key,
            ),
            subject="general_domain_events",
        )


@task_processor.add_event()
async def send_email_confirmation(
    event: events.EmailConfirmationCreatedEvent, svcs_container: Container
) -> None:
    """
    Sends an email confirmation email.

    Args:
        event (events.EmailConfirmationCreatedEvent): email confirmation created event.
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
        verification_url=settings.CLIENT_EMAIL_VERIFICATION_URL + str(event.key),
    )


@task_processor.add_event()
async def send_password_reset(
    event: events.PasswordResetConfirmationCreatedEvent, svcs_container: Container
) -> None:
    """
    Sends a password reset email.

    Args:
        event (events.PasswordResetConfirmationCreatedEvent): password reset created event.
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
        verification_url=settings.CLIENT_EMAIL_VERIFICATION_URL + str(event.key),
    )
