from .common import CommandHandlerDict, EventHandlerDict
from src.user.ops.command_handlers import USER_ASGI_COMMAND_HANDLERS
from src.user.ops.event_handlers import USER_ASGI_EVENT_HANDLERS
from src.user.domain import User
from svcs import Container
from typing import Awaitable, Callable
from src.common.domain import Command, Event

ASGI_COMMAND_HANDLERS: CommandHandlerDict = USER_ASGI_COMMAND_HANDLERS
ASGI_EVENT_HANDLERS: EventHandlerDict = USER_ASGI_EVENT_HANDLERS

type CommandHandler = Callable[[Command, Container, User | None], Awaitable[None]]
type CommandHandlerDict = dict[type[Command], CommandHandler]
type EventHandler = Callable[[Event, Container, User | None], Awaitable[None]]
type EventHandlerDict = dict[type[Event], list[EventHandler]]
