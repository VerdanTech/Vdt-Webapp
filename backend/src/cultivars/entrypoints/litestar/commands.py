# External Libraries
from litestar import Controller, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.auth.guard import requires_account
from src.common.ops.processors import asgi_processor
from src.cultivars.domain import Cultivar, commands


class CultivarCommandController(Controller):
    """
    Cultivar ASGI controller.
    """

    path = "command"
    tags = ["cultivars"]

    @post(
        path="update",
        summary="Cultivar update.",
        description="Sets the given attributes onto the cultivar.",
        operation_id=commands.CultivarAttributeUpdateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_update(
        self,
        data: commands.CultivarAttributeUpdateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar update application command.

        Args:
            data (CultivarAttributeUpdateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...
