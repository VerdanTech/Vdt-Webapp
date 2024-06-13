# Standard Library
from typing import Protocol

# VerdanTech Source
from src.common.domain.events import Event


class AbstractEventNode(Protocol):
    async def emit(self, event: Event, subject: str):
        pass

    async def stream_events(self, subject: str):
        pass

    async def listen(self, subject: str):
        pass

    async def on_startup(self, subjects: list[str]) -> None:
        pass

    async def on_shutdown(self) -> None:
        pass

    async def publish(self):
        pass
