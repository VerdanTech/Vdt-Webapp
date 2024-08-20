# Standard Library
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src import exceptions
from src.common.domain.models import Ref
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.ops.processors import asgi_processor
from src.garden.domain import Garden, RoleEnum, commands, events
from src.garden.domain.models import GardenMembership
from src.user.domain import User

from .queries import generate_unique_garden_key


@asgi_processor.add_command()
async def create_garden(
    command: commands.GardenCreateCommand, svcs_container: Container, client: User
) -> None:
    """
    Main garden creation operation.

    1. Validates the command against the database state.
    2. Generates a unique garden key if one was not provided.
    3. Creates a new garden.
    4. Creates a membership for the creator.
    5. Persists the garden.
    6. Emits the PendingInvites event.

    Args:
        command (commands.GardenCreateCommand): garden creation command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Validate command against database state ie., existing fields
        await command.validate_against_uow(uow=uow)

        # Generate a new garden key if one was not provided
        key: str
        if command.key is None:
            key_result = await generate_unique_garden_key(
                svcs_container=svcs_container, client=client
            )
            key = key_result.key
        else:
            key = command.key

        # Create a new garden
        garden = Garden(
            name=command.name,
            key=key,
            creator_ref=client.ref,
            description=command.description,
        )

        # Create a membership for the creator.
        creator_membership = GardenMembership(
            inviter_ref=None,
            user_ref=client.ref,
            role=RoleEnum.ADMIN,
            accepted_at=datetime.now(),
        )
        garden.memberships.add(creator_membership)

        # Persist garden
        garden = await uow.repos.gardens.add(garden)
        await uow.commit()

        # TODO: I'm not sure if the id will be updated upon commit(). If not, add query here. If yes, remove this.
        if not garden.persisted:
            raise exceptions.DomainIntegrityException("Add a query here to get id.")

        # Create all invitations
        garden.events.append(
            events.PendingInvites(
                garden_ref=garden.ref,
                client_ref=client.ref,
                admin_usernames=command.admin_usernames,
                editor_usernames=command.editor_usernames,
                viewer_usernames=command.viewer_usernames,
            )
        )


@asgi_processor.add_command()
async def create_invites(
    command: commands.GardenMembershipCreateCommand,
    svcs_container: Container,
    client: User,
) -> None:
    """
    Create a new set of garden membership invites by emitting the PendingInvites event.

    Args:
        command (commands.GardenMembershipCreateCommand): invite creation command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.

    Raises:
        GardenAuthorizationException: raised if the client does
            not have the required permissions on their GardenMembership.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    # Create all invitations
    uow.events.append(
        events.PendingInvites(
            garden_ref=Ref(id=command.garden_id),
            client_ref=client.ref,
            admin_usernames=command.admin_usernames,
            editor_usernames=command.editor_usernames,
            viewer_usernames=command.viewer_usernames,
        )
    )


@asgi_processor.add_command()
async def accept_invite(
    command: commands.GardenMembershipAcceptCommand,
    svcs_container: Container,
    client: User,
) -> None:
    """
    Accepts a GardenMembership invite.

    Args:
        command (commands.GardenMembershipAcceptCommand): membership acceptance command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.

    Raises:
        EntityNotFound: raised if data.garden_key does not exist.

    Returns:
        GardenMembership: the membership after persistence.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Retrieve garden
        garden = await uow.repos.gardens.get_by_key(command.garden_key)
        if garden is None:
            raise exceptions.NotFoundError(non_form_errors=[("Garden does not exist")])

        # Accept the invite - raises on failure
        garden.accept_membership(user=client)

        # Persist garden
        await uow.repos.gardens.update(garden)
        await uow.commit()


@asgi_processor.add_command()
async def delete_membership(
    command: commands.GardenMembershipDeleteCommand,
    svcs_container: Container,
    client: User,
) -> None:
    """
    Removes the client from the garden.

    Args:
        command (commands.GardenMembershipDeleteCommand): membership deletion command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.

    Raises:
        EntityNotFound: raised if the garden key does not exist.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        garden = await uow.repos.gardens.get_by_key(command.garden_key)
        if garden is None:
            raise exceptions.NotFoundError(non_form_errors=[("Garden does not exist")])

        # Remove client's membership
        garden.remove_membership(user=client)

        # Persist garden
        await uow.repos.gardens.update(garden)
        await uow.commit()


@asgi_processor.add_command()
async def revoke_membership(
    command: commands.GardenMembershipRevokeCommand,
    svcs_container: Container,
    client: User,
) -> None:
    """
    Removes a User that is not the client from a Garden.

    Args:
        command (commands.GardenMembershipRevokeCommand): membership revoke command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.

    Raises:
        EntityNotFound: raised if command.user_id or
            command.garden_id do not exist.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Retrieve garden
        garden = await uow.repos.gardens.get_by_id(command.garden_id)
        if garden is None:
            raise exceptions.NotFoundError(non_form_errors=[("Garden does not exist")])

        # Retrieve user
        user = await uow.repos.users.get_by_id(command.user_id)
        if user is None:
            raise exceptions.NotFoundError(non_form_errors=[("User does not exist")])

        # Remove the membership
        garden.revoke_membership(client=client, subject=user)

        # Persist garden
        await uow.repos.gardens.update(garden)
        await uow.commit()


@asgi_processor.add_command()
async def change_role(
    command: commands.GardenMembershipRoleChangeCommand,
    svcs_container: Container,
    client: User,
) -> None:
    """
    Changes the role of a GardenMembership.

    Args:
        command (commands.GardenMembershipDeleteCommand): membership role change command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.

    Raises:
        EntityNotFound: raised if command.user_id or
            command.garden_id do not exist.
    """
    # Locate services
    uow = await svcs_container.aget_abstract(AbstractUow)

    async with uow:
        # Retrieve garden
        garden = await uow.repos.gardens.get_by_id(command.garden_id)
        if garden is None:
            raise exceptions.NotFoundError(non_form_errors=[("Garden does not exist")])

        # Retrieve user
        user = await uow.repos.users.get_by_id(command.user_id)
        if user is None:
            raise exceptions.NotFoundError(non_form_errors=[("User does not exist")])

        # Change the role on the membership
        garden.change_role(
            client=client, subject=user, garden=garden, new_role=command.role
        )

        # Persist garden
        await uow.repos.gardens.update(garden)
        await uow.commit()
