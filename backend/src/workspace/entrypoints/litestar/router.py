# External Libraries
from litestar import Router

from .queries import WorkspaceQueryController


def create_workspace_router() -> Router:
    """
    Configure the workspace router.
    """
    return Router(
        path="workspaces",
        route_handlers=[WorkspaceQueryController],
    )
