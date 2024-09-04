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
        path="create_cultivar",
        summary="Cultivar create.",
        description="Creates a new cultivar on the collection.",
        operation_id=commands.CultivarCreateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_create(
        self,
        data: commands.CultivarCreateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar creation application command.

        Args:
            data (CultivarCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="update_cultivar",
        summary="Cultivar update.",
        description="Sets the given attributes onto the cultivar.",
        operation_id=commands.CultivarUpdateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_update(
        self,
        data: commands.CultivarUpdateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar update application command.

        Args:
            data (CultivarUpdateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="delete_cultivar",
        summary="Cultivar delete.",
        description="Deletes a given cultivar from a collection.",
        operation_id=commands.CultivarDeleteCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_delete(
        self,
        data: commands.CultivarDeleteCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar delete application command.

        Args:
            data (CultivarDeleteCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="create_collection",
        summary="Cultivar collection create.",
        description="Creates a new cultivar collection.",
        operation_id=commands.CultivarCollectionCreateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_collection_create(
        self,
        data: commands.CultivarCollectionCreateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar collection creation application command.

        Args:
            data (CultivarCollectionCreateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="update_collection",
        summary="Cultivar collection update.",
        description="Sets the given attributes onto the cultivar collection.",
        operation_id=commands.CultivarCollectionUpdateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_collection_update(
        self,
        data: commands.CultivarCollectionUpdateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar collection update application command.

        Args:
            data (CultivarUpdateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="delete_collection",
        summary="Cultivar collection delete.",
        description="Deletes a cultivar collection.",
        operation_id=commands.CultivarCollectionDeleteCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_collection_delete(
        self,
        data: commands.CultivarCollectionDeleteCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar collection delete application command.

        Args:
            data (CultivarCollectionDeleteCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="duplicate_collection",
        summary="Cultivar collection duplication.",
        description="Creates a new cultivar collection by copying the attributes of another.",
        operation_id=commands.CultivarCollectionDuplicateCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_collection_duplicate(
        self,
        data: commands.CultivarCollectionDuplicateCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar collection duplicate application command.

        Args:
            data (CultivarCollectionDuplicateCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...

    @post(
        path="merge_collection",
        summary="Cultivar collection merge.",
        description="Copies the data of an exising cultivar collection into a another existing collection.",
        operation_id=commands.CultivarCollectionMergeCommand.to_operation_id(),
        guards=[requires_account],
    )
    async def cultivar_collection_merge(
        self,
        data: commands.CultivarCollectionMergeCommand,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> str:
        """
        Calls the cultivar collection merge application command.

        Args:
            data (CultivarCollectionMergeCommand): input command.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.
        """
        ...
