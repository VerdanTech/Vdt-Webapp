# External Libraries
from taskiq_nats import NatsBroker

NATS_URI = ""

broker = NatsBroker(servers=NATS_URI, queue="task_queue")


@broker.task
async def handle_message():
    pass


async def main():
    await broker.startup()
