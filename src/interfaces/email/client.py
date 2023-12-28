# Standard Library
from typing import Any, Dict, Protocol


class AbstractEmailClient(Protocol):
    """
    The EmailClient provides an interface between an EmailEmitter and the
    functionality of reading emails from file, populating templated
    variables, and sending them to a server.
    """

    async def compile_and_send(
        self, filepath: str, receiver: str, subject: str, **kwargs
    ):
        """
        Compile email from html, and send it as html
        with a plaintext alternative.

        Args:
            filepath (str): path of the html content.
            receiver (str): recipient address.
            subject (str): subject line of the message.
            kwargs: arguments to insert into html.
        """
        ...
