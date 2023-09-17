from typing import Dict

from src.verdantech_api.application.user.schemas.api.write import UserCreateInput
from src.verdantech_api.domain.models.user.services.sanitization import UserSanitizer

from ..fields.password import validate_password_match


def sanitize_user_create(
    data: UserCreateInput, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the object sanitizer and extra password sanitizer

    Args:
        data (UserCreateInput): user creation data transfer object
        user_sanitizer (UserSanitizer): user sanitizer

    Returns:
        Dict[str, str]: the sanitized data
    """
    validate_password_match(password1=data.password1, password2=data.password2)
    sanitized_data = user_sanitizer.sanitize(
        input={
            "username": data.username,
            "email_address": data.email_address,
            "password": data.password1,
        }
    )
    return sanitized_data
