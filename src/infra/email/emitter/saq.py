# Standard Library
from typing import Optional

# External Libraries
from saq import Queue
from saq.types import Context

# VerdanTech Source
from src.interfaces.email.client import AbstractEmailClient

from .generic import BaseEmailEmitter


async def send_email(
    ctx: Context,
    client: AbstractEmailClient,
    filepath: str,
    receiver: str,
    subject: str,
    **kwargs,
) -> None:
    """
    Email send function to register into saq's queue system.

    Args:
        ctx (Context): saq context dict.
        filepath (str): the path to the email file
        receiver (str): the receiver of the message
        subject (str): the subject of the message
        kwargs: arguments to insert into html
    """
    await client.compile_and_send(
        filepath=filepath, receiver=receiver, subject=subject, **kwargs
    )


class SaqEmailEmitter(BaseEmailEmitter):
    """Implementation of email emitter using SAQ event queue."""

    def __init__(
        self, client: AbstractEmailClient, saq_queue: Optional[Queue] = None
    ) -> None:
        self.client = client
        self.saq_queue = saq_queue

    async def _send(
        self,
        filepath: str,
        receiver: str,
        subject: str,
        queue: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """
        Send the email or emit the email send event into saq's event queue.

        Args:
            filepath (str): filepath of the email.
            receiver (str): recipient email address.
            subject (str): email subject line.
            queue (Optional[bool]): if True, emits the email send
                into litestar's event queue. If false, awaits the
                sending of the email within this method. Defaults to False.

        Raises:
            ValueError: if queue=True and no queue was supplied to the emitter.
        """
        # Todo: implement queueing
        queue = False
        if queue:
            if not self.saq_queue:
                raise ValueError(
                    "Email was queued but no SaqQueue was supplied to emitter."
                )

            await self.saq_queue.enqueue(
                "send_email",
                client=self.client,
                filepath=filepath,
                receiver=receiver,
                subject=subject,
                **kwargs,
            )
        else:
            await self.client.compile_and_send(
                filepath=filepath, receiver=receiver, subject=subject, **kwargs
            )
