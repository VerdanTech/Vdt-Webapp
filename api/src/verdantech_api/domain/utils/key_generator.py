import random
import string
from typing import Callable

StringIDGeneratorT = (Callable[[int, str], str],)


def key_generator(
    length: int, chars: str = string.ascii_uppercase + string.digits
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
    return "".join(random.choice(chars) for _ in range(length))
