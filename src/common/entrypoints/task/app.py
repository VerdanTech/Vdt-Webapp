# External Libraries
from svcs import Container
from taskiq_nats import NatsBroker

# VerdanTech Source
from src.common.adapters.events import NatsEventNode
from src.common.adapters.registry import create_registry
from src.common.domain import Event
from src.common.ops.processors import task_processor

broker = NatsBroker(servers=["nats://localhost:4222"])

global_state = {"sqlalchemy_client": None}


@broker.task
async def process_event(event: Event, svcs_container: Container) -> None:
    try:
        await task_processor.handle_effect(event, svcs_container)
    except Exception as e:
        # Log the error
        raise


async def main() -> None:
    svcs_registry = create_registry()
    await broker.startup()

    async for message in broker.listen():
        container = Container(svcs_registry)
        await process_event.kiq(event, container)

    await broker.startup()
