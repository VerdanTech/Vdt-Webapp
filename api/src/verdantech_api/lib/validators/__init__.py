from verdantech_api import settings

from .concrete.email import EmailValidator
from .concrete.password import PasswordValidator
from .concrete.username import UsernameValidator


def provide_email_validator():
    return EmailValidator(
        min_length=settings.EMAIL_MIN_LENGTH,
        max_length=settings.EMAIL_MAX_LENGTH,
        regex=None,
        blacklist=[],
        whitelist=[],
        min_length_message="Requires minimum {message} characters",
        max_length_message="Allows minimum {message} characters",
        regex_message="Must fit pattern: {message}",
        banned_input_message="Input not allowed",
    )


def provide_username_validator():
    return UsernameValidator(
        min_length=settings.USERNAME_MIN_LENGTH,
        max_length=settings.USERNAME_MAX_LENGTH,
        regex=None,
        blacklist=[],
        whitelist=[],
        min_length_message="Requires minimum {message} characters",
        max_length_message="Allows minimum {message} characters",
        regex_message="Must fit pattern: {message}",
        banned_input_message="Username unsafe or offensive",
    )


def provide_password_validator():
    return PasswordValidator(
        min_length=settings.PASSWORD_MIN_LENGTH,
        max_length=settings.PASSWORD_MAX_LENGTH,
        regex=None,
        blacklist=[],
        whitelist=[],
        min_length_message="Requires minimum {message} characters",
        max_length_message="Allows minimum {message} characters",
        regex_message="Must fit pattern: {message}",
        banned_input_message="Choose a stronger password!",
    )
