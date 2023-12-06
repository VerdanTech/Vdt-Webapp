# Standard Library
import re

# External Libraries
from dns.resolver import Resolver

# VerdanTech Source
from src import settings
from src.domain.user.sanitizers import UserSanitizer, UserSanitizerConfig
from src.interfaces.persistence.user import AbstractUserRepository
from src.utils import sanitizers

banned_usernames = []
with open(settings.static_path("banned_fields/usernames.txt"), "r") as file:
    for line in file:
        # Strip any leading/trailing whitespace including newline characters
        username = line.strip()
        # Add the username to the list
        banned_usernames.append(username)


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


async def provide_user_sanitizer(user_repo: AbstractUserRepository) -> UserSanitizer:
    """Configure and return a user sanitizer with application settings for dependency injection."""
    return UserSanitizer(
        config=UserSanitizerConfig(
            username=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSpec(
                    sanitizers.basic.LengthSpecConfig(
                        params=sanitizers.basic.LengthSpecParams(
                            min=settings.USERNAME_MIN_LENGTH,
                            max=settings.USERNAME_MAX_LENGTH,
                        ),
                        error_message="Must be within {min} and {max} characters.",
                    )
                ),
                sanitizers.basic.RegexSpec(
                    sanitizers.basic.RegexSpecConfig(
                        params=sanitizers.basic.RegexSpecParams(
                            pattern=re.compile("[0-9A-Za-z]+")
                        ),
                        error_message="Must contain only alphanumeric characters.",
                    )
                ),
                sanitizers.basic.BanSpec(
                    sanitizers.basic.BanSpecConfig(
                        params=sanitizers.basic.BanSpecParams(
                            banned_inputs=banned_usernames
                        ),
                        error_message="Username unsafe or offensive.",
                        case_sensitive=False,
                    )
                ),
                sanitizers.repo.UniqueSpec(
                    sanitizers.repo.UniqueSpecConfig(
                        repo=user_repo,
                        existence_method_name="username_exists",
                        existence_method_argument_name="username",
                        error_message="Username already exists.",
                    )
                ),
            ),
            email_address=sanitizers.FieldSanitizer(
                sanitizers.repo.UniqueSpec(
                    sanitizers.repo.UniqueSpecConfig(
                        repo=user_repo,
                        existence_method_name="email_exists",
                        existence_method_argument_name="email_address",
                        error_message="Email already exists.",
                    )
                ),
                sanitizers.custom.EmailSpec(
                    config=sanitizers.custom.EmailSpecConfig(
                        dns_resolver=Resolver(),
                        params=sanitizers.custom.EmailSpecParams(
                            check_deliverability=True,
                            test_environment=True,
                            allow_smtputf8=False,
                        ),
                        error_message="Email is not valid.",
                    )
                ),
            ),
            password=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSpec(
                    sanitizers.basic.LengthSpecConfig(
                        params=sanitizers.basic.LengthSpecParams(
                            min=settings.PASSWORD_MIN_LENGTH,
                            max=settings.PASSWORD_MAX_LENGTH,
                        ),
                        error_message="Must be within {min} and {max} characters.",
                    )
                ),
                sanitizers.basic.RegexSpec(
                    sanitizers.basic.RegexSpecConfig(
                        params=sanitizers.basic.BanSpecParams(
                            pattern=re.compile(
                                """^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d~`!@#$%^&*()_\-+={[}\]|\:;"'<,>.?/]*$"""
                            )
                        ),
                        error_message="Password must contain at least one lowercase letter, one uppercase letter, and one digit.",
                    )
                ),
            ),
            confirmation_key=sanitizers.FieldSanitizer(
                sanitizers.basic.LengthSpec(
                    sanitizers.basic.LengthSpecConfig(
                        params=sanitizers.basic.LengthSpecParams(
                            min=settings.VERIFICATION_KEY_MAX_LENGTH,
                            max=settings.VERIFICATION_KEY_MAX_LENGTH,
                        ),
                        error_message="Confirmation key must be {min} characters long.",
                    )
                )
            ),
        )
    )
