# Standard Library
import pdb
from typing import Awaitable, Callable, Union, get_type_hints

# External Libraries
from attr import define, field
from svcs import Container

# VerdanTech Source
from src.common.domain import Command, Event
from src.common.interfaces.persistence import AbstractUow
from src.user.domain import User

from .queries import Query, QueryResult

type CommandHandler = Callable[[Command, Container, User | None], Awaitable[None]]
type EventHandler = Callable[[Event, Container], Awaitable[None]]
type QueryHandler = Callable[[Query, Container, User | None], Awaitable[QueryResult]]

Effect = Union[Command, Event]


@define
class HandlerContainer:
    """
    Contains all command and event handlers registered
    for a single message processor.

    Commands maps commands to command handlers one-to-one.
    Events maps events to event handlers one-to-many.
    Queries maps queries to query handlers one-to-one.
    """

    commands: dict[type[Command], CommandHandler] = field(factory=dict)
    events: dict[type[Event], list[EventHandler]] = field(factory=dict)
    queries: dict[type[Query], QueryHandler] = field(factory=dict)


class MessageProcessor:
    """
    Collates commands and events and provides an interface for handling them.
    """

    handlers: HandlerContainer = HandlerContainer()

    def add_command(self):
        def decorator(func):
            # Retrieve the command type
            type_hints = get_type_hints(func)
            command_type: type[Command] = type_hints.get("command", None)
            if not isinstance(command_type, type(Command)):
                # TODO
                raise Exception(
                    f"Registered command handler with invalid signature: {func}"
                )

            self.handlers.commands[command_type] = func
            return func

        return decorator

    def add_event(self):
        def decorator(func):
            # Retrieve the event type
            type_hints = get_type_hints(func)
            event_type: type[Event] = type_hints.get("event", None)
            if not isinstance(event_type, type(Event)):
                # TODO
                raise Exception(
                    f"Registered event handler with invalid signature: {func}"
                )

            self.handlers.events.setdefault(event_type, []).append(func)
            return func

        return decorator

    async def handle_effect(
        self, effect: Effect, svcs_container: Container, client: User | None = None
    ) -> None:
        """
        Handle a command or event and all resultant events.

        Args:
            effect (Effect): The effect to handle.

        Raises:
            Exception: Raises the exception of the command if any.
        """
        # Locate services
        uow = await svcs_container.aget_abstract(AbstractUow)

        self.queue = [effect]
        while self.queue:
            effect = self.queue.pop(0)
            if isinstance(effect, Command):
                await self._handle_command(effect, svcs_container, client)
            elif isinstance(effect, Event):
                await self._handle_event(effect, svcs_container)
            else:
                raise ValueError(f"{effect} was not an Event or Command")

            # Register any newly added events
            self.queue.extend(uow.collect_new_events())

    async def _handle_command(
        self, command: Command, svcs_container: Container, client: User | None = None
    ) -> None:
        """
        Handles a single command. Raises caught exceptions.

        Args:
            command (Command): the command to handle.

        Raises:
            Exception: Raises the exception of the command.
        """
        try:
            handler = self.handlers.commands[type(command)]
            if handler is None:
                raise Exception(f"{command} is unmapped to a handler")

            await handler(command, svcs_container, client)

        except Exception:
            # TODO add logging
            raise

    async def _handle_event(self, event: Event, svcs_container: Container) -> None:
        """
        Handles a single event. No exceptions are raised.

        Args:
            event (Event): the event to handle.
        """
        for handler in self.handlers.events[type(event)]:
            try:
                await handler(event, svcs_container)

            except Exception:
                # TODO add logging
                continue
