from functools import partial
from typing import Any, Callable, Dict

from litestar import Request
from litestar.events import listener

from . import provide_email_client

"""Interface for framework-agnostic email emitter callable"""
Receiver = str
Subject = str
Filepath = str
Kwargs = Dict[str, Any]
EmailEmitter = Callable[[Receiver, Subject, Filepath, Kwargs], None]


def provide_litestar_email_emitter(request: Request) -> EmailEmitter:
    """Litestar email emitter bo be injected into route handler

    Args:
        request (Request): the litestar request object,
            registered automatically when injected as
            dependency into route handler

    Returns:
        EmailEmitter: email emitter callable
    """
    return partial(request.app.emit, "emit_email")


@listener("emit_email")
async def emit_email_emitter(
    self, filepath: str, receiver: str, subject: str, **kwargs: Dict[str, Any]
):
    """Register the email send function in Litestar's event system

    Args:
        filepath (str): the path to the email file
        receiver (str): the receiver of the message
        subject (str): the subject of the message
        kwargs (Dict[str, Any]): arguments to insert into html
    """
    client = provide_email_client()
    await client.compile_and_send(
        filepath=filepath, receiver=receiver, subject=subject, **kwargs
    )
