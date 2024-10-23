# Standard Library
import uuid

# External Libraries
from litestar import Controller, Request, get
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.workspace.ops import queries


class WorkspaceQueryController(Controller):
    """Workspace read operations controller"""

    path = "query"
    tags = ["workspaces"]

    @get(
        path="get_partials",
        summary="Get workspaces from a garden.",
        description="Retrieves the workspaces associated with this garden.",
        operation_id=queries.WorkspaceGetPartialsQuery.to_operation_id(),
    )
    async def get_partials(
        self,
        garden_key: str,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> list[queries.WorkspacePartialSchema]:
        """
        Calls the garden associated workspaces query.

        Args:
            garden_key (str): the key of the garden to request.
            request (Request): Litestar request object.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            list[queries.WorkspacePartialSchema]: the workspaces.
        """
        svcs_container.register_local_value(State, state)
        result = await queries.get_partials(
            query=queries.WorkspaceGetPartialsQuery(garden_key=garden_key),
            svcs_container=svcs_container,
            client=request.user,
        )
        return result

    @get(
        path="get_full",
        summary="Get a full workspace schema.",
        description="Retrieves a full workspace schema.",
        operation_id=queries.WorkspaceGetFullQuery.to_operation_id(),
    )
    async def get_full(
        self,
        garden_key: str,
        workspace_slug: str,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.WorkspaceFullSchema:
        """
        Calls the full workspace query.

        Args:
            garden_key (str): the key of the garden where the workspace is located.
            workspace_slug (str): the slug of the workspace to request.
            request (Request): Litestar request object.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            queries.WorkspaceFullSchema: the workspace.
        """
        svcs_container.register_local_value(State, state)
        result = await queries.get_full(
            query=queries.WorkspaceGetFullQuery(
                garden_key=garden_key, workspace_slug=workspace_slug
            ),
            svcs_container=svcs_container,
            client=request.user,
        )
        return result
