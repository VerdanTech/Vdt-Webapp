# External Libraries
from litestar import Controller, Request, Response, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src import settings
from src.domain.garden.sanitizers import GardenSanitizer
from src.gateway.litestar import openapi
from src.gateway.litestar.exceptions import (
    ClientError,
    ServerError,
    litestar_exception_map,
)
from src.common.interfaces.email import AbstractEmailEmitter
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.interfaces.security.crypt.crypt import AbstractPasswordCrypt
from src.ops.garden.controllers.membership import GardenMembershipOpsController
from src.ops.garden.schemas import (
    membership as membership_ops_schemas,
    read as read_ops_schemas,
)

from .. import routes, urls


class GardenMembershipApiController(Controller):
    """
    Garden membership ASGI controller.
    """

    path = urls.GARDEN_MEMBERSHIP_CONTROLLER_URL_BASE
    tags = ["gardens"]

    @post(
        path=urls.GARDEN_INVITE_URL,
        name=routes.GARDEN_INVITE_NAME,
        summary="Garden membership invitiation.",
        description="Creates a new Garden Membership and sends an email confirmation email.",
        response_description="The full newly created garden membership object",
        operation_id=routes.GARDEN_INVITE_NAME,
    )
    async def invite(
        self,
        request: Request,
        data: membership_ops_schemas.GardenInviteCreateInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> read_ops_schemas.GardenMembershipFullSchema:
        """
        Calls the garden invitation application operation.

        Args:
            request (Request): Litestar request object.
            data (GardenInviteCreateInput): input data transfer object.
            state (State): Litestar global application state.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            GardenMembershipFullSchema: full membership object schema.
        """
        svcs_container.register_local_value(State, state)
        garden_membership_ops_controller = await svcs_container.aget(
            GardenMembershipOpsController
        )
        user_repo, email_emitter = await svcs_container.aget_abstract(
            AbstractUserRepository, AbstractEmailEmitter
        )
        with litestar_exception_map():
            membership_schema = await garden_membership_ops_controller.invite(
                client=request.user,
                data=data,
                user_repo=user_repo,
                email_emitter=email_emitter,
            )
        return membership_schema

    @post(
        path=urls.GARDEN_ACCEPT_INVITE_URL,
        name=routes.GARDEN_ACCEPT_INVITE_NAME,
        summary="Garden membership invitiation acceptance.",
        description="Accepts a Garden Membership.",
        response_description="The full newly accepted garden membership object",
        operation_id=routes.GARDEN_ACCEPT_INVITE_NAME,
    )
    async def accept_invite(
        self,
        request: Request,
        garden_key: str,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> read_ops_schemas.GardenMembershipFullSchema:
        """
        Calls the garden accept invitation application operation.

        Args:
            request (Request): Litestar request object.
            garden_key (str): key of the garden to leave.
            state (State): Litestar global application state.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            GardenMembershipFullSchema: full membership object schema.
        """
        svcs_container.register_local_value(State, state)
        garden_membership_ops_controller = await svcs_container.aget(
            GardenMembershipOpsController
        )
        with litestar_exception_map():
            membership_schema = await garden_membership_ops_controller.accept_invite(
                client=request.user, garden_key=garden_key
            )
        return membership_schema

    @post(
        path=urls.GARDEN_LEAVE_URL,
        name=routes.GARDEN_LEAVE_NAME,
        summary="Garden membership .",
        description="Removes own Garden Membership from a garden.",
        response_description="Membership with Garden has been removed.",
        operation_id=routes.GARDEN_LEAVE_NAME,
    )
    async def leave(
        self,
        request: Request,
        garden_key: str,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
        """
        Calls the garden membership deletion application operation.

        Args:
            request (Request): Litestar request object.
            garden_key (str): key of the garden to leave.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            Response[str]: the response with a success message.
        """
        svcs_container.register_local_value(State, state)
        garden_membership_ops_controller = await svcs_container.aget(
            GardenMembershipOpsController
        )
        with litestar_exception_map():
            await garden_membership_ops_controller.leave(
                client=request.user, garden_key=garden_key
            )
        return Response(content="Membership with Garden has been removed.")

    @post(
        path=urls.GARDEN_REVOKE_URL,
        name=routes.GARDEN_REVOKE_NAME,
        summary="Removes a user from a garden.",
        description="Removes another's Garden Membership from a garden.",
        response_description="Membership with Garden has been removed.",
        operation_id=routes.GARDEN_REVOKE_NAME,
    )
    async def revoke_membership(
        self,
        request: Request,
        data: membership_ops_schemas.GardenRevokeMembershipInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Response[str]:
        """
        Calls the garden membership revoke operation.

        Args:
            request (Request): Litestar request object.
            data (GardenRevokeMembershipInput): input data transfer object.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            Response[str]: the response with a success message.
        """
        svcs_container.register_local_value(State, state)
        garden_membership_ops_controller = await svcs_container.aget(
            GardenMembershipOpsController
        )
        user_repo = await svcs_container.aget_abstract(AbstractUserRepository)
        with litestar_exception_map():
            await garden_membership_ops_controller.revoke_membership(
                client=request.user, data=data, user_repo=user_repo
            )
        return Response(content="Membership with Garden has been removed.")

    @post(
        path=urls.GARDEN_CHANGE_ROLE_URL,
        name=routes.GARDEN_CHANGE_ROLE_NAME,
        summary="Garden Membership role change.",
        description="Changes the role on another's Garden Membership.",
        response_description="The full newly changed Garden Membership object.",
        operation_id=routes.GARDEN_CHANGE_ROLE_NAME,
    )
    async def change_role(
        self,
        request: Request,
        data: membership_ops_schemas.GardenRoleChangeInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> read_ops_schemas.GardenMembershipFullSchema:
        """
        Calls the garden membership change role application operation.

        Args:
            request (Request): Litestar request object.
            data (GardenRoleChangeInput): input data transfer object.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            GardenMembershipFullSchema: the newly changed Garden Membership schema.
        """
        svcs_container.register_local_value(State, state)
        garden_membership_ops_controller = await svcs_container.aget(
            GardenMembershipOpsController
        )
        user_repo = await svcs_container.aget_abstract(AbstractUserRepository)
        with litestar_exception_map():
            membership_schema = await garden_membership_ops_controller.change_role(
                client=request.user, data=data, user_repo=user_repo
            )
        return membership_schema
