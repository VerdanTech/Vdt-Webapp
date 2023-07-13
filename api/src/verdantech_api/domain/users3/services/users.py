from typing import TYPE_CHECKING, Tuple

from litestar.exceptions import ValidationException
from pydantic import SecretStr

from verdantech_api.lib.field_validators.errors import ValidationError

if TYPE_CHECKING:
    from verdantech_api.lib.crypt.generic import PasswordCrypt

from ..models import EmailModel, UserModel
from ..repos.email import EmailRepo
from ..repos.user import UserRepo


class UserService:
    """Handles database operations for users"""

    user_repo: UserRepo
    email_repo: EmailRepo
    password_crypt: PasswordCrypt

    def __init__(
        self,
        user_repo: UserRepo,
        email_repo: EmailRepo,
        password_crypt: PasswordCrypt,
    ) -> None:
        self.user_repo = user_repo
        self.email_repo = email_repo
        self.password_crypt = password_crypt

    async def create(
        self, email: str, username: str, password1: SecretStr, password2: SecretStr
    ) -> Tuple[UserModel, EmailModel]:
        """Sanitize data and register user

        Args:
            email (str): email of the user
            username (str): username of the user
            password1 (SecretStr): password1 of the user
            password2 (SecretStr): password2 of the user

        Returns:
            UserModel: The added instance
        """
        raised_exception = False
        exception = {"detail": "Field validation failed", "extra": {}}

        # Sanitize email
        try:
            email = self.email_repo.email_sanitize(email=email)
        except ValidationError as error:
            raised_exception = True
            exception["extra"]["email"] = str(error)

        # Sanitize username
        try:
            username = self.user_repo.username_sanitize(username=username)
        except ValidationError as error:
            raised_exception = True
            exception["extra"]["username"] = str(error)

        # Sanitize password
        try:
            self.user_repo.password_sanitize(password1=password1, password2=password2)
        except ValidationError as error:
            raised_exception = True
            exception["extra"]["password1"] = str(error)
            exception["extra"]["password2"] = str(error)

        if raised_exception:
            raise ValidationException(
                detail=exception["detail"], extra=exception["extra"]
            )

        # Generate hashed password
        hashed_password: SecretStr = await self.password_crypt.get_password_hash(
            password1
        )

        # Construct models
        new_user = UserModel(username=username, password=hashed_password)
        new_email = EmailModel(email=email)
        new_user.emails = {new_email}

        # Add to repos
        user = await self.user_repo.add(new_user)
        email = await self.email_repo.add(new_email)

        return user, email

    async def change_email():
        pass

    async def change_password():
        pass

    async def change_username():
        pass
