# VerdanTech Source
from src.utils import sanitizers


def validate_password_match(password1: str, password2: str) -> None:
    """
    Ensure that two passwords provided to a password input
    match, else a SpecError is raised.

    Args:
        password1 (str): the first password to match.
        password2 (str): the second password to match.

    Raises:
        SpecError: raised if the passwords do not match.
    """
    if not password1 == password2:
        raise sanitizers.spec.SpecError(
            {"MultiFieldError": "Password inputs do not match."}
        )
