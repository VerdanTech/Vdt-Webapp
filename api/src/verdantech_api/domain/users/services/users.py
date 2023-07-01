from typing import Tuple, TypeVar

from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.exceptions import ValidationException
from pydantic import SecretStr

from verdantech_api.lib.crypt import GeneratePasswordHashAwaitable
from verdantech_api.lib.validators.email import EmailValidatorCallableType
from verdantech_api.lib.validators.password import PasswordValidatorCallableType
from verdantech_api.lib.validators.username import UsernameValidatorCallableType

from ..models import EmailModel, UserModel

UserRepoT = TypeVar("UserRepoT", bound="UserRepo")
EmailRepoT = TypeVar("EmailRepoT", bound="EmailRepo")


class UserRepo(SQLAlchemyAsyncRepository[UserModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = UserModel


class EmailRepo(SQLAlchemyAsyncRepository[EmailModel]):
    """SQLAlchemy Repository for the EmailModel"""

    model_type = EmailModel


class UserService:
    """Handles database operations for users"""

    user_repo: SQLAlchemyAsyncRepository[UserModel]
    email_repo: SQLAlchemyAsyncRepository[EmailModel]
    email_validator: EmailValidatorCallableType
    username_validator: UsernameValidatorCallableType
    password_validator: PasswordValidatorCallableType
    password_hasher: GeneratePasswordHashAwaitable

    def __init__(
        self,
        user_repo: SQLAlchemyAsyncRepository[UserModel],
        email_repo: SQLAlchemyAsyncRepository[EmailModel],
        email_validator: EmailValidatorCallableType,
        username_validator: UsernameValidatorCallableType,
        password_validator: PasswordValidatorCallableType,
        password_hasher: GeneratePasswordHashAwaitable,
    ) -> None:
        self.user_repo = user_repo
        self.email_repo = email_repo
        self.email_validator = email_validator
        self.username_validator = username_validator
        self.password_validator = password_validator
        self.password_hasher = password_hasher

    async def create(
        self, email: str, username: str, password1: SecretStr, password2: SecretStr
    ) -> Tuple[str, str]:
        """Sanitize data and register user

        Args:
            email (str): email of the user
            username (str): username of the user
            password1 (SecretStr): password1 of the user
            password2 (SecretStr): password2 of the user

        Returns:
            Tuple[UserModel, EmailModel]: _description_
        """
        # Validate and normalize email
        email = self.email_validator(email)
        matched_email = await self.user_repo.get_one_or_none(email=email)
        if matched_email:
            raise ValidationException()

        # Validate username
        self.username_validator(username)
        matched_username = await self.user_repo.get_one_or_none(username=username)
        if matched_username:
            raise ValidationException()

        # Validate password
        self.password_validator(password1, password2)

        # Generate hashed password
        hashed_password: SecretStr = await self.password_hasher(password1)

        # Construct models
        new_user = UserModel(username=username, password=hashed_password)
        new_email = EmailModel(email=email)
        new_user.emails = {new_email}

        # Add to repos
        await self.user_repo.add(new_user)
        await self.new_email.add(new_email)

        return email, username

    async def change_password():
        pass

    async def change_username():
        pass
