# Standard Library
from typing import Awaitable, Callable, Union

# External Libraries
from svcs import Container

# VerdanTech Source
from src.domain.common import Command, Event
from src.domain.user import User
from src.interfaces.persistence.common import AbstractUow

Message = Union[Command, Event]


type CommandHandler = Callable[[Command, Container, User], Awaitable[None]]
type CommandHandlerDict = dict[type[Command], CommandHandler]
type EventHandler = Callable[[Event, Container, User], Awaitable[None]]
type EventHandlerDict = dict[type[Event], list[EventHandler]]

class MessageBus:
    """
    Collates commands and events and provides an interface for handling them.
    """

    def __init__(
        self,
        svcs_container: Container,
        command_handlers: CommandHandlerDict,
        event_handlers: EventHandlerDict,
    ):
        self.svcs_container = svcs_container
        self.command_handlers = command_handlers
        self.event_handlers = event_handlers

        # Locate services
        self.uow = self.svcs_container.get_abstract(AbstractUow)

    async def handle(self, message: Message, client: User | None = None) -> None:
        """
        Handle a message and all resultant events.

        Args:
            message (Message): The message to handle.
        """
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, Command):
                await self.handle_command(message, client)
            elif isinstance(message, Event):
                await self.handle_event(message, client)
            else:
                raise ValueError(f"{message} was not an Event or Command")

    async def handle_command(self, command: Command, client: User | None = None) -> None:
        """
        Handles a single command. Raises caught exceptions.

        Args:
            command (Command): the command to handle.

        Raises:
            Exception: Raises the exception of the command.
        """
        try:
            handler = self.command_handlers[type(command)]
            if handler is None:
                raise Exception(f"{command} is unmapped to a handler")

            await handler(command, self.svcs_container, client)

            self.queue.extend(self.uow.collect_new_events())

        except Exception:
            # TODO add logging
            raise

    async def handle_event(self, event: Event, client: User | None = None) -> None:
        """
        Handles a single event. No exceptions are raised.

        Args:
            event (Event): the event to handle.
        """
        for handler in self.event_handlers[type(event)]:
            try:
                await handler(event, self.svcs_container, client)
                self.queue.extend(self.uow.colllect_new_events())
            except Exception:
                # TODO add logging
                continue
