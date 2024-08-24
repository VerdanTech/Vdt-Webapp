# External Libraries
from litestar import Controller, Request, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar import requires_account
from src.common.ops.processors import asgi_processor
from src.garden.domain import commands


class GardenCommandController(Controller):
    """
    Garden command ASGI controller.
    """

    path = "command"
    tags = ["gardens"]

    @post(
        path="create",
        summary="Garden creation.",
        description="Creates a new Garden and invites requested users.",
        operation_id=commands.GardenCreateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def garden_create(
        self,
        data: commands.GardenCreateCommand,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden creation command.

        Args:
            request (Request): Litestar incoming request object.
            data (GardenCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        await asgi_processor.handle_effect(
            effect=data, svcs_container=svcs_container, client=request.user
        )

    @post(
        path="invite",
        summary="Garden membership invitiation.",
        description="Creates new Garden Memberships and sends email confirmation emails.",
        operation_id=commands.GardenMembershipCreateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def invite(
        self,
        data: commands.GardenMembershipCreateCommand,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden invitation application command.

        Args:
            request (Request): Litestar incoming request object.
            data (GardenMembershipCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        await asgi_processor.handle_effect(
            effect=data, svcs_container=svcs_container, client=request.user
        )

    @post(
        path="accept_invite",
        summary="Garden membership invitiation acceptance.",
        description="Accepts a Garden Membership.",
        operation_id=commands.GardenMembershipAcceptCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def accept_invite(
        self,
        data: commands.GardenMembershipAcceptCommand,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden accept invitation application command.

        Args:
            request (Request): Litestar incoming request object.
            data (GardenMembershipAcceptCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        await asgi_processor.handle_effect(
            effect=data, svcs_container=svcs_container, client=request.user
        )

    @post(
        path="leave",
        summary="Garden membership deletion.",
        description="Removes one's own Garden Membership from a garden.",
        operation_id=commands.GardenMembershipDeleteCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def leave(
        self,
        data: commands.GardenMembershipDeleteCommand,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden membership deletion application command.

        Args:
            request (Request): Litestar incoming request object.
            data (GardenMembershipAcceptCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        await asgi_processor.handle_effect(
            effect=data, svcs_container=svcs_container, client=request.user
        )

    @post(
        path="revoke",
        summary="Removes a user from a garden.",
        description="Removes another's Garden Membership from a garden.",
        operation_id=commands.GardenMembershipRevokeCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def revoke_membership(
        self,
        data: commands.GardenMembershipRevokeCommand,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden membership revoke command.

        Args:
            request (Request): Litestar incoming request object.
            data (GardenMembershipRevokeCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.

        Returns:
            Response[str]: the response with a success message.
        """
        svcs_container.register_local_value(State, state)
        await asgi_processor.handle_effect(
            effect=data, svcs_container=svcs_container, client=request.user
        )

    @post(
        path="change_role",
        summary="Garden Membership role change.",
        description="Changes the role on another's Garden Membership.",
        operation_id=commands.GardenMembershipRoleChangeCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def change_role(
        self,
        data: commands.GardenMembershipRoleChangeCommand,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden membership change role command.

        Args:
            request (Request): Litestar incoming request object.
            data (GardenMembershipRoleChangeCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.

        Returns:
            GardenMembershipFullSchema: the newly changed Garden Membership schema.
        """
        svcs_container.register_local_value(State, state)
        await asgi_processor.handle_effect(
            effect=data, svcs_container=svcs_container, client=request.user
        )
