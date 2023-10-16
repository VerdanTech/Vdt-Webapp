from typing import Dict

from src.domain.user.services.sanitization import UserSanitizer
from src.utils.sanitizers.field import DISABLE_FIELD
from src.utils.sanitizers.sanitization.basic import (
    BanSanitization,
    LengthSanitization,
    RegexSanitization,
)
from src.utils.sanitizers.sanitization.repo import (
    UniqueSanitization,
)

from .fields.password import validate_password_match


async def sanitize_all_fields_password_match(
    username: str,
    email_address: str,
    password1: str,
    password2: str,
    user_sanitizer: UserSanitizer,
) -> Dict[str, str]:
    """Call the object sanitizer and extra password sanitizer

    Args:
        username (str): username to sanitize
        email_address (str): email address to sanitize
        password1 (str): password1 to sanitize
        password2 (str): password2 to sanitize
        user_sanitizer (UserSanitizer): user object sanitizer

    Returns:
        Dict[str, str]: sanitized data
    """
    validate_password_match(password1=password1, password2=password2)
    sanitized_data = await user_sanitizer.sanitize(
        input={
            "username": username,
            "email_address": email_address,
            "password": password1,
        }
    )
    return sanitized_data


async def sanitize_only_email(
    email_address: str, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the object sanitizer with the username and
        password fields disabled

    Args:
        email_address (str): email address to sanitize
        user_sanitizer (UserSanitizer): user object sanitizer

    Returns:
        Dict[str, str]: sanitized data
    """
    sanitized_data = await user_sanitizer.sanitize(
        input={"email_address": email_address},
        disabled_fields={
            "username": DISABLE_FIELD,
            "password": DISABLE_FIELD,
            "email_address": [
                UniqueSanitization,
                LengthSanitization,
                UniqueSanitization,
                RegexSanitization,
            ],
        },
    )
    return sanitized_data


async def sanitize_passwords(
    password1: str, password2: str, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the object sanitizer with the username and
        email fields disabled, and extra password matcher
        sanitizer

    Args:
        password1 (str): password1 to sanitize
        password2 (str): password2 to sanitize
        user_sanitizer (UserSanitizer): user object sanitizer

    Returns:
        Dict[str, str]: sanitized data
    """
    validate_password_match(password1=password1, password2=password2)
    sanitized_data = await user_sanitizer.sanitize(
        input={"password": password1},
        disabled_fields={"username": DISABLE_FIELD, "email_address": DISABLE_FIELD},
    )
    return sanitized_data
