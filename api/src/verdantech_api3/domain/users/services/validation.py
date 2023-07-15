from typing import Tuple

from litestar.exceptions import ValidationException
from src.verdantech_api.lib.validators.generic.errors import ValidationError
from src.verdantech_api.lib.validators.generic.validators import FieldValidator

from ..models.repos import EmailRepo, UserRepo


class UserFieldsSanitizerService:
    def __init__(
        self,
        username_validator: FieldValidator,
        email_validator: FieldValidator,
        password_validator: FieldValidator,
        user_repo: UserRepo,
        email_repo: EmailRepo,
    ):
        self.username_validator = username_validator
        self.email_validator = email_validator
        self.password_validator = password_validator
        self.user_repo = user_repo
        self.email_repo = email_repo

    async def sanitize_fields(
        self, username: str, email: str, password1: str, password2: str
    ) -> Tuple[str, str, str]:
        # Group exceptions
        raised_exception = False
        exception = {"detail": "Field validation failed", "extra": {}}

        # Sanitize username
        try:
            username = await self.username_sanitize(username=username)
        except ValidationError as error:
            raised_exception = True
            exception["extra"]["username"] = error.message

        # Sanitize email
        try:
            email = await self.email_sanitize(email=email)
        except ValidationError as error:
            raised_exception = True
            exception["extra"]["email"] = error.message

        # Sanitize password
        try:
            password = await self.password_sanitize(
                password1=password1, password2=password2
            )
        except ValidationError as error:
            raised_exception = True
            exception["extra"]["password1"] = error.message
            exception["extra"]["password2"] = error.message

        # Catch all exceptions
        if raised_exception:
            raise ValidationException(
                detail=exception["detail"], extra=exception["extra"]
            )

        return username, email, password

    async def username_sanitize(self, username: str) -> str:
        # Ensure username unique
        matched_username = await self.user_repo.exists(username=username)
        if matched_username:
            raise ValidationError(message="Username already in use")

        # Validate against static criteria
        self.username_validator.validate(input=username)

        return username

    async def email_sanitize(self, email: str) -> None:
        # Ensure email unique
        matched_email = await self.email_repo.exists(email=email)
        if matched_email:
            raise ValidationError(message="Email address already in use")

        # Validate against static criteria
        self.email_validator.validate(input=email)

        # Return normalized email
        email = self.email_validator.normalize(input=email)

        return email

    async def password_sanitize(self, password1: str, password2: str) -> None:
        # Ensure passwords match
        if not password1 == password2:
            raise ValidationError(message="Passwords do not match")

        # Validate against static criteria
        self.password_validator.validate(input=password1)

        return password1
