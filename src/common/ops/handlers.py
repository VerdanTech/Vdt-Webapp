# Standard Library
from typing import Awaitable, Callable, get_type_hints

# External Libraries
from attr import define, field
from svcs import Container

# VerdanTech Source
from src.common.domain import Command, Event
from src.user.domain import User

from .queries import Query, QueryResult

type CommandHandler = Callable[[Command, Container, User | None], Awaitable[None]]
type EventHandler = Callable[[Event, Container], Awaitable[None]]
type QueryHandler = Callable[[Query, Container, User | None], Awaitable[QueryResult]]


@define
class HandlerContainer:
    """
    Contains all command and event handlers registered
    for a single message processor.
    """

    commands: dict[type[Command], CommandHandler] = field(factory=dict)
    events: dict[type[Event], list[EventHandler]] = field(factory=dict)
    queries: dict[type[Query], QueryHandler] = field(factory=dict)
