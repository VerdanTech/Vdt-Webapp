from src.utils.sanitizers.sanitization.generic import SanitizationError


class PasswordMismatchError(SanitizationError):
    pass


def validate_password_match(password1: str, password2: str) -> None:
    if not password1 == password2:
        raise PasswordMismatchError(
            {
                "password1": "Password inputs do not match",
                "password2": "Password inputs do not match",
            }
        )
