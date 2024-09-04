# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.ops.processors import asgi_processor
from src.cultivars.domain import commands
from src.user.domain import User


@asgi_processor.add_command()
async def create_cultivar(
    command: commands.CultivarCreateCommand, svcs_container: Container, client: User
) -> None:
    """
    Main cultivar creation operation.

    1. Validates the command against the database state.
    2. Creates a cultivar on the collection.
    3. Persists the collection.

    Args:
        command (commands.CultivarCreateCommand): cultivar creation command.
        svcs_container (Container): service locator.
        client (User): the client user responsible for the command.
    """
    ...


@asgi_processor.add_command()
async def update_cultivar(
    command: commands.CultivarUpdateCommand, svcs_container: Container, client: User
) -> None:
    ...


@asgi_processor.add_command()
async def delete_cultivar(
    command: commands.CultivarDeleteCommand, svcs_container: Container, client: User
) -> None:
    ...


@asgi_processor.add_command()
async def create_cultivar_collection(
    command: commands.CultivarCollectionCreateCommand,
    svcs_container: Container,
    client: User,
) -> None:
    ...


@asgi_processor.add_command()
async def update_cultivar_collection(
    command: commands.CultivarCollectionUpdateCommand,
    svcs_container: Container,
    client: User,
) -> None:
    ...


@asgi_processor.add_command()
async def delete_cultivar_collection(
    command: commands.CultivarCollectionDeleteCommand,
    svcs_container: Container,
    client: User,
) -> None:
    ...


@asgi_processor.add_command()
async def duplicate_cultivar_collection(
    command: commands.CultivarCollectionDuplicateCommand,
    svcs_container: Container,
    client: User,
) -> None:
    ...


@asgi_processor.add_command()
async def merge_cultivar_collection(
    command: commands.CultivarCollectionMergeCommand,
    svcs_container: Container,
    client: User,
) -> None:
    ...
