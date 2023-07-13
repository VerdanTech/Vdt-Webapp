import random
import string

from aiofiles import open as async_open


def key_generator(
    size: int, chars: str = string.ascii_uppercase + string.digits
) -> str:
    """Generate a random string

    Args:
        size (int): length of the output
        chars (str, optional): number of characters
            to use for generating output. Defaults to
            string.ascii_uppercase+string.digits.

    Returns:
        str: the generated string
    """
    return "".join(random.choice(chars) for _ in range(size))


async def read_file_async(filepath: str) -> str:
    """Open file with asyncio

    Args:
        filepath (str): path of the file

    Returns:
        str: the document
    """
    with async_open(filepath, "r") as file:
        return await file.read()


class IdFactory:
    """Simple ID factory to use with mock
    repositories"""

    def __init__(self, initial=1):
        self.count = initial

    def factory(self):
        self.count += 1
        return self.count
