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
        path="get_by_garden",
        summary="Get workspaces from a garden.",
        description="Retrieves the workspaces associated with this garden.",
        operation_id=queries.WorkspaceGetByBardenQuery.to_operation_id(),
    )
    async def get_by_garden(
        self,
        garden_key: str,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> list[queries.WorkspaceSchema]:
        """
        Calls the garden associated workspaces query.

        Args:
            garden_key (str): the key of the garden to request.
            request (Request): Litestar request object.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            list[queries.WorkspaceSchema]: the workspaces.
        """
        svcs_container.register_local_value(State, state)
        result = await queries.get_by_garden(
            query=queries.WorkspaceGetByBardenQuery(garden_key=garden_key),
            svcs_container=svcs_container,
            client=request.user,
        )
        return result
