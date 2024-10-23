# External Libraries
from litestar import Router

from .commands import WorkspaceCommandController
from .queries import WorkspaceQueryController


def create_workspace_router() -> Router:
    """
    Configure the workspace router.
    """
    return Router(
        path="workspaces",
        route_handlers=[WorkspaceQueryController, WorkspaceCommandController],
    )
