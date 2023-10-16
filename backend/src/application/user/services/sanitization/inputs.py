from typing import Dict

from src.application.user.schemas.api.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailRequestInput,
)
from src.application.user.schemas.api.write import UserCreateInput
from src.domain.user.services.sanitization import UserSanitizer

from .cases import (
    sanitize_all_fields_password_match,
    sanitize_only_email,
    sanitize_passwords,
)


async def sanitize_user_create(
    data: UserCreateInput, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the all fields + password match sanitization method

    Args:
        data (UserCreateInput): user creation DTO
        user_sanitizer (UserSanitizer): user sanitizer objetc

    Returns:
        Dict[str, str]: sanitized data
    """
    return await sanitize_all_fields_password_match(
        username=data.username,
        email_address=data.email_address,
        password1=data.password1,
        password2=data.password2,
        user_sanitizer=user_sanitizer,
    )


async def sanitize_verify_email_request(
    data: UserVerifyEmailRequestInput, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the email only sanitiization method

    Args:
        data (UserVerifyEmailRequestInput): email verification
            request DTO
        user_sanitizer (UserSanitizer): user sanitizer object

    Returns:
        Dict[str, str]: sanitized data
    """
    return await sanitize_only_email(
        email_address=data.email_address, user_sanitizer=user_sanitizer
    )


async def sanitize_password_reset_request(
    data: UserPasswordResetRequestInput, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the email only sanitiization method

    Args:
        data (UserVerifyEmailRequestInput): password reset
            request DTO
        user_sanitizer (UserSanitizer): user sanitizer object

    Returns:
        Dict[str, str]: sanitized data
    """
    return await sanitize_only_email(
        email_address=data.email_address, user_sanitizer=user_sanitizer
    )


async def sanitize_password_reset_confirm(
    data: UserPasswordResetConfirmInput, user_sanitizer: UserSanitizer
) -> Dict[str, str]:
    """Call the dual password sanitization method

    Args:
        data (UserPasswordResetConfirmInput): password reset
            confirmation DTO
        user_sanitizer (UserSanitizer): user sanitizer object

    Returns:
        Dict[str, str]: sanitized data
    """
    return await sanitize_passwords(
        password1=data.new_password1,
        password2=data.new_password2,
        user_sanitizer=user_sanitizer,
    )
