# External Libraries
from litestar import Controller, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.auth.guard import requires_account
from src.common.ops.processors import asgi_processor
from src.workspace.domain import commands


class WorkspaceCommandController(Controller):
    """
    Workspace ASGI controller.
    """

    path = "command"
    tags = ["workspaces"]

    @post(
        path="create_workspace",
        summary="Workspace create.",
        description="Creates a new workspace on the garden.",
        operation_id=commands.WorkspaceCreateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def workspace_create(
        self,
        data: commands.WorkspaceCreateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the workspace creation application command.

        Args:
            data (WorkspaceCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="update_workspace",
        summary="Workspace update.",
        description="Sets the given attributes onto the workspace.",
        operation_id=commands.WorkspaceUpdateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def workspace_update(
        self,
        data: commands.WorkspaceUpdateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the workspace update application command.

        Args:
            data (WorkspaceUpdateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="delete_workspace",
        summary="Workspace delete.",
        description="Deletes a given workspace from a garden.",
        operation_id=commands.WorkspaceDeleteCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def workspace_delete(
        self,
        data: commands.WorkspaceDeleteCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the workspace delete application command.

        Args:
            data (WorkspaceDeleteCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="create_planting_area",
        summary="Planting area create.",
        description="Creates a new planting area on the workspace.",
        operation_id=commands.PlantingAreaCreateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def planting_area_create(
        self,
        data: commands.PlantingAreaCreateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the planting area creation application command.

        Args:
            data (PlantingAreaCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="update_planting_area",
        summary="Planting area update.",
        description="Sets the given attributes onto the planting area.",
        operation_id=commands.PlantingAreaUpdateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def planting_area_update(
        self,
        data: commands.PlantingAreaUpdateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the planting area update application command.

        Args:
            data (PlantingAreaUpdateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="delete_planting_area",
        summary="Planting area delete.",
        description="Deletes a given planting area from a workspace.",
        operation_id=commands.PlantingAreaDeleteCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def planting_area_delete(
        self,
        data: commands.PlantingAreaDeleteCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the planting area delete application command.

        Args:
            data (PlantingAreaDeleteCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...
