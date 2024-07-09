# External Libraries
from litestar import Controller, Request, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.exceptions import litestar_exception_map
from src.common.entrypoints.litestar.utils import url_to_route_name
from src.common.ops.processors import asgi_processor
from src.garden.domain import commands

from . import urls


class GardenCommandController(Controller):
    """
    Garden command ASGI controller.
    """

    path = urls.GARDEN_COMMAND_CONTROLLER_URL_BASE
    tags = ["gardens"]

    @post(
        path=urls.GARDEN_CREATE_URL,
        name=url_to_route_name(urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_CREATE_URL),
        summary="Garden creation.",
        description="Creates a new Garden and invites requested users.",
    )
    async def garden_create(
        self,
        data: commands.CreateGarden,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden creation command.

        Args:
            request (Request): Litestar incoming request object.
            data (CreateGarden): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container, client=request.user
            )

    @post(
        path=urls.GARDEN_INVITE_URL,
        name=url_to_route_name(urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_INVITE_URL),
        summary="Garden membership invitiation.",
        description="Creates new Garden Memberships and sends email confirmation emails.",
    )
    async def invite(
        self,
        data: commands.MembershipInvite,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden invitation application command.

        Args:
            request (Request): Litestar incoming request object.
            data (MembershipInvite): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container, client=request.user
            )

    @post(
        path=urls.GARDEN_ACCEPT_INVITE_URL,
        name=url_to_route_name(
            urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_ACCEPT_INVITE_URL
        ),
        summary="Garden membership invitiation acceptance.",
        description="Accepts a Garden Membership.",
    )
    async def accept_invite(
        self,
        data: commands.AcceptInvite,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden accept invitation application command.

        Args:
            request (Request): Litestar incoming request object.
            data (AcceptInvite): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container, client=request.user
            )

    @post(
        path=urls.GARDEN_LEAVE_URL,
        name=url_to_route_name(urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_LEAVE_URL),
        summary="Garden membership deletion.",
        description="Removes one's own Garden Membership from a garden.",
    )
    async def leave(
        self,
        data: commands.DeleteMembership,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden membership deletion application command.

        Args:
            request (Request): Litestar incoming request object.
            data (AcceptInvite): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container, client=request.user
            )

    @post(
        path=urls.GARDEN_REVOKE_URL,
        name=url_to_route_name(urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_REVOKE_URL),
        summary="Removes a user from a garden.",
        description="Removes another's Garden Membership from a garden.",
    )
    async def revoke_membership(
        self,
        data: commands.RevokeMembership,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden membership revoke command.

        Args:
            request (Request): Litestar incoming request object.
            data (RevokeMembership): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.

        Returns:
            Response[str]: the response with a success message.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container, client=request.user
            )

    @post(
        path=urls.GARDEN_CHANGE_ROLE_URL,
        name=url_to_route_name(
            urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_CHANGE_ROLE_URL
        ),
        summary="Garden Membership role change.",
        description="Changes the role on another's Garden Membership.",
    )
    async def change_role(
        self,
        data: commands.ChangeMembershipRole,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> None:
        """
        Calls the garden membership change role command.

        Args:
            request (Request): Litestar incoming request object.
            data (ChangeMembershipRole): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.

        Returns:
            GardenMembershipFullSchema: the newly changed Garden Membership schema.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            await asgi_processor.handle_effect(
                effect=data, svcs_container=svcs_container, client=request.user
            )
