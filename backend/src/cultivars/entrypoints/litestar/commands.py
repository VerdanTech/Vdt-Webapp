# External Libraries
from litestar import Controller, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.ops.processors import asgi_processor
from src.cultivars.domain import commands, Cultivar


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
        operation_id=commands.CultivarAttributeUpdateCommand.to_operation_id()
    )
    async def cultivar_update(
        self,
        data: commands.CultivarAttributeUpdateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> Cultivar:
        """
        Calls the cultivar update application command.

        Args:
            data (CultivarAttributeUpdateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...