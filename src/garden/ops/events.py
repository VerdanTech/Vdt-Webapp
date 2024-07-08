# External Libraries
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.domain import Ref
from src.common.interfaces.email.client import AbstractEmailClient
from src.common.interfaces.events import AbstractEventNode
from src.common.interfaces.persistence import AbstractUow
from src.common.ops.processors import asgi_processor, task_processor
from src.garden.domain import GardenInvite, GardenMembership, RoleEnum, events
from src.garden.domain.exceptions import GardenAuthorizationException
from src.garden.domain.permission import PermissionRouter


@asgi_processor.add_event()
async def process_garden_invite(
    event: events.PendingInvites, svcs_container: Container
) -> None:
    """
    Creates garden memberships and queues email notification.

    Args:
        event (events.PendingInvites): pending invites event.
        svcs_container (Container): service locator.
    """
    # Locate services
    uow, event_node = await svcs_container.aget_abstract(AbstractUow, AbstractEventNode)

    async with uow:
        # Retrieve the garden and client
        garden = await uow.repos.gardens.get_by_id(event.garden_ref.id)
        client = await uow.repos.users.get_by_id(event.client_ref.id)

        # Retrieve client's membership
        client_membership = garden.get_membership(user=client)
        if client_membership is None:
            raise GardenAuthorizationException(
                "Not authorized to perform operations in this Garden."
            )

        # For each of the admin, editor, and viewer ids
        # which were provided and for which the client has
        # permission to authorize for, create a GardenInvite
        # for every existing user and append them to the list.
        invites: list[GardenInvite] = []
        if event.admin_ids and client_membership.authorize(
            operation=PermissionRouter.invite(role=RoleEnum.ADMIN),
        ):
            users = await uow.repos.users.get_by_ids(event.admin_ids)
            admin_invites = [
                GardenInvite(
                    user_ref=Ref(id=user.id_or_error()),
                    role=RoleEnum.ADMIN,
                    user_username=user.username,
                    user_email=user.primary_email.address,
                )
                for user in users
            ]
            invites += admin_invites
        if event.editor_ids and client_membership.authorize(
            operation=PermissionRouter.invite(role=RoleEnum.EDIT),
        ):
            users = await uow.repos.users.get_by_ids(event.editor_ids)
            editor_invites = [
                GardenInvite(
                    user_ref=Ref(id=user.id_or_error()),
                    role=RoleEnum.EDIT,
                    user_username=user.username,
                    user_email=user.primary_email.address,
                )
                for user in users
            ]
            invites += editor_invites
        if event.viewer_ids and client_membership.authorize(
            operation=PermissionRouter.invite(role=RoleEnum.VIEW),
        ):
            users = await uow.repos.users.get_by_ids(event.viewer_ids)
            viewer_invites = [
                GardenInvite(
                    user_ref=Ref(id=user.id_or_error()),
                    role=RoleEnum.VIEW,
                    user_username=user.username,
                    user_email=user.primary_email.address,
                )
                for user in users
            ]
            invites += viewer_invites

        # Create the memberships
        memberships = [
            GardenMembership(
                garden_ref=garden.ref,
                inviter_ref=event.client_ref,
                user_ref=invite.user_ref,
                role=invite.role,
                accepted=False,
            )
            for invite in invites
        ]

        # Persist the garden
        garden.memberships = garden.memberships.update(memberships)
        await uow.repos.gardens.update(garden)
        await uow.commit()

        # Emit the email sending event to the task backend
        if invites:
            await event_node.emit(
                events.InvitesCreated(
                    inviter_username=client.username,
                    garden_name=garden.name,
                    garden_key=garden.key,
                    invites=invites,
                ),
                subject="general_domain_events",
            )


@task_processor.add_event()
async def send_garden_invite(
    event: events.InvitesCreated, svcs_container: Container
) -> None:
    """
    Sends garden invite emails.

    Args:
        event (events.InvitesCreated): garden memberships created event.
        svcs_container (Container): service locator.
    """
    # Locate services
    email_client = await svcs_container.aget_abstract(AbstractEmailClient)

    # Send the emails
    for invite in event.invites:
        await email_client.compile_and_send(
            filepath=settings.EMAIL_FILEPATH_GARDEN_INVITE,
            receiver=invite.user_email,
            subject=settings.EMAIL_SUBJECT_EMAIL_CONFIRMATION,
            username=invite.user_username,
            role=str(invite.role),
            inviter_username=event.inviter_username,
            garden_name=event.garden_name,
            garden_url=settings.CLIENT_GARDENS_URL + str(event.garden_key),
        )
