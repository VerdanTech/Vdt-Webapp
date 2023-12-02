# Standard Library
import re

# VerdanTech Source
from src import settings
from src.domain.user.sanitizers import UserSanitizer, UserSanitizerConfig
from src.interfaces.persistence.user import AbstractUserRepository
from src.utils import sanitizers


def validate_password_match(password1: str, password2: str) -> None:
    if not password1 == password2:
        raise sanitizers.spec.SpecError({"password1": "Password inputs do not match"})


async def provide_user_sanitizer(user_repo: AbstractUserRepository) -> UserSanitizer:
    """Configure and return a user sanitizer with application settings for dependency injection."""
    return UserSanitizer(
        config=UserSanitizerConfig(
            username=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSanitization(
                    sanitizers.basic.LengthSanitizationConfig(
                        spec=sanitizers.basic.LengthSanitizationSpec(
                            min=settings.USERNAME_MIN_LENGTH,
                            max=settings.USERNAME_MAX_LENGTH,
                        ),
                        error_message="Username must be within {spec.min} and {spec.max} characters.",
                    )
                ),
                sanitizers.basic.RegexSanitization(
                    sanitizers.basic.RegexSanitizationConfig(
                        spec=re.compile, error_message=""
                    )
                ),
                sanitizers.basic.BanSanitization(
                    sanitizers.basic.BanSanitizationConfig(
                        spec=[], error_message="", extra={"case_sensitive": False}
                    )
                ),
                sanitizers.repo.UniqueSanitization(
                    sanitizers.repo.UniqueSanitizationConfig(
                        spec=sanitizers.repo.UniqueSanitizationSpec(
                            field_name="username", repo=user_repo
                        ),
                        error_message="",
                    )
                ),
            ),
            email_address=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSanitization(
                    sanitizers.basic.LengthSanitizationConfig(
                        spec=sanitizers.basic.LengthSanitizationSpec(min=0, max=0),
                        error_message="",
                    )
                ),
                sanitizers.basic.BanSanitization(
                    sanitizers.basic.BanSanitizationConfig(
                        spec=[], error_message="", extra={"case_sensitive": False}
                    )
                ),
                sanitizers.repo.UniqueSanitization(
                    sanitizers.repo.UniqueSanitizationConfig(
                        spec=sanitizers.repo.UniqueSanitizationSpec(
                            field_name="username", repo=user_repo
                        ),
                        error_message="",
                    )
                ),
                sanitizers.custom.EmailSanitization(),
            ),
            password=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSanitization(
                    sanitizers.basic.LengthSanitizationConfig(
                        spec=sanitizers.basic.LengthSanitizationSpec(min=0, max=0),
                        error_message="",
                    )
                ),
                sanitizers.basic.RegexSanitization(
                    sanitizers.basic.RegexSanitizationConfig(
                        spec=re.compile, error_message=""
                    )
                ),
                sanitizers.basic.BanSanitization(
                    sanitizers.basic.BanSanitizationConfig(
                        spec=[], error_message="", extra={"case_sensitive": False}
                    )
                ),
            ),
            confirmation_key=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSanitization(
                    sanitizers.basic.LengthSanitizationConfig(
                        spec=sanitizers.basic.LengthSanitizationSpec(min=0, max=0),
                        error_message="",
                    )
                )
            ),
        )
    )
