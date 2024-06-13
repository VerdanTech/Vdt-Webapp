# External Libraries
from svcs import Container

from .node import NatsEventNode


def provide_nats_event_node(svcs_container: Container) -> NatsEventNode:
    return NatsEventNode()
