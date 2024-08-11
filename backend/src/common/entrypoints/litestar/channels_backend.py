from __future__ import annotations

# External Libraries
from litestar.channels.backends.base import ChannelsBackend


class NatsChannelsBackend(ChannelsBackend):
    """An litestar channels backend to connect to a NATS server."""
