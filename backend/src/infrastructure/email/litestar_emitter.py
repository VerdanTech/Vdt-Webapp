from typing import Any, Callable, Dict

from litestar import Litestar
from litestar.events import listener
from src.interfaces.email.client import AbstractEmailClient


@listener("emit_email")
async def emit_email_emitter(
    self,
    client: AbstractEmailClient,
    filepath: str,
    receiver: str,
    subject: str,
    **kwargs: Dict[str, Any],
) -> None:
    """Register the email client send function in Litestar's event system

    Args:
        filepath (str): the path to the email file
        receiver (str): the receiver of the message
        subject (str): the subject of the message
        kwargs (Dict[str, Any]): arguments to insert into html
    """
    await client.compile_and_send(
        filepath=filepath, receiver=receiver, subject=subject, **kwargs
    )


class EmailEmitter:
    """Implementation of email emitter interface defined in interfaces"""

    def __init__(self, client: AbstractEmailClient, app: Litestar):
        self.client = client
        self.app = app

    def __call__(
        self, filepath: str, receiver: str, subject: str, **kwargs: Dict[str, Any]
    ) -> None:
        """Call the email emit event using request and client configured in __init__"""
        self.app.emit(
            "emit_email",
            client=self.client,
            filepath=filepath,
            receiver=receiver,
            subject=subject,
            **kwargs,
        )
