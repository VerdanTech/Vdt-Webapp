# Standard Library
import random
import string
from typing import Callable

# VerdanTech Source
from src.common.interfaces.persistence.common import AbstractRepository

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


async def generate_unique_key(
    length: int,
    repo: AbstractRepository,
    existence_method_name: str,
    existence_method_argument_name,
) -> str:
    """
    Generate a unique verification key. Keep generating keys until the
    repository's existence method returns False.

    Args:
        length (int): length of the key to generate.
        repo (AbstractRepository): any repository
            instance.
        existence_method_name (str): the name of the repository
            existence check method.
        kwargs (str): name of the argument on the existence check
            method that takes as input the value of the field
            to check the existence of.

    Returns:
        str: the unique key.
    """
    key = key_generator(length=length)
    while await repo.async_dynamic_call(
        method_name=existence_method_name,
        bypass_validation=False,
        **{existence_method_argument_name: key},
    ):
        key = key_generator(length=length)
    return key
