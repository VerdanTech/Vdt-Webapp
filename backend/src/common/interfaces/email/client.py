# Standard Library
from pathlib import Path
from typing import Protocol


class AbstractEmailClient(Protocol):
    """
    The EmailClient provides an interface for reading emails from file,
    populating templated variables, and sending them to a server.
    """

    async def compile_and_send(
        self, filepath: Path, receiver: str, subject: str, **kwargs
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
