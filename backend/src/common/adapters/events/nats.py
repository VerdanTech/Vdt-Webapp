# External Libraries
from svcs import Container

# VerdanTech Source
from src.common.interfaces.events.node import AbstractEventNode


class NatsEventNode(AbstractEventNode):
    pass


def provide_nats_event_node(svcs_container: Container) -> NatsEventNode:
    return NatsEventNode()
