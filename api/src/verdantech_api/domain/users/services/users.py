from typing import TYPE_CHECKING, List, Tuple, TypeVar

from litestar.contrib.repository.filters import CollectionFilter, OrderBy
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.exceptions import ValidationException
from pydantic import SecretStr

from verdantech_api.lib.validators.exceptions import ValidationError
from verdantech_api.settings import USER_MAX_EMAILS

if TYPE_CHECKING:
    from verdantech_api.lib.validators.generic import Validator
    from verdantech_api.lib.crypt.generic import PasswordCrypt

from ..models import EmailModel, UserModel

UserRepoT = TypeVar("UserRepoT", bound="UserRepo")
EmailRepoT = TypeVar("EmailRepoT", bound="EmailRepo")


class UserRepo(SQLAlchemyAsyncRepository[UserModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = UserModel


class EmailRepo(SQLAlchemyAsyncRepository[EmailModel]):
    """SQLAlchemy Repository for the EmailModel"""

    model_type = EmailModel

    async def remove_oldest_email(self, user_id: int) -> List[EmailModel]:
        """Remove the user's email with the least magnitude
        of the set_at attribute

        Args:
            user_id (int): ID of the user

        Returns:
            List[EmailModel]: the full list of user's emails
                after the operation
        """
        # Get list of user's emails and remove the one with the oldest primary_at
        user_emails, count = await self.list_and_count(
            CollectionFilter(field_name="user_id", values=[user_id]),
            OrderBy(field_name="set_at"),
        )
        if count > USER_MAX_EMAILS:
            oldest_email = user_emails.pop[0]
            await self.email_confirmation_repo.remove(oldest_email)

        return user_emails

    async def set_new_primary_email(
        self, new_primary_email: EmailModel, user_emails: List[EmailModel]
    ) -> None:
        """Set exclusive primary status to new email

        Args:
            new_primary_email (EmailModel): the email to set as primary.
                Must be contained in user_emails, and be verified
            user_emails (List[EmailModel]): list of user's emails

        Raises:
            Exception: _description_
        """
        if not new_primary_email.is_verified:
            raise Exception  # todo

        if new_primary_email not in user_emails:
            raise Exception  # todo

        # Remove primary status for all emails except new one
        for email in user_emails:
            if email.id == new_primary_email.id:
                email.set_primary_status()
            else:
                email.remove_primary_status()

        await self.update_many(user_emails)


class UserService:
    """Handles database operations for users"""

    user_repo: UserRepo
    email_repo: EmailRepo
    email_validator: Validator
    username_validator: Validator
    password_validator: Validator
    password_crypt: PasswordCrypt

    def __init__(
        self,
        user_repo: UserRepo,
        email_repo: EmailRepo,
        email_validator: Validator,
        username_validator: Validator,
        password_validator: Validator,
        password_crypt: PasswordCrypt,
    ) -> None:
        self.user_repo = user_repo
        self.email_repo = email_repo
        self.email_validator = email_validator
        self.username_validator = username_validator
        self.password_validator = password_validator
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
        # Validate and normalize email
        try:
            self.email_validator.validate(input=email)
        except ValidationError as error:
            raise ValidationException(
                detail="Email validation failed", extra={"email": error}
            )

        email = self.email_validator.normalize(input=email)
        matched_email = await self.user_repo.get_one_or_none(email=email)
        if matched_email:
            raise ValidationException(
                detail="Email validation failed",
                extra={"email": "Email address already in use"},
            )

        # Validate username
        try:
            self.username_validator.validate(input=username)
        except ValidationError as error:
            raise ValidationException(
                detail="Username validation failed", extra={"username": error}
            )
        matched_username = await self.user_repo.get_one_or_none(username=username)
        if matched_username:
            raise ValidationException(
                detail="Username validation failed",
                extra={"username": "Username already in use"},
            )

        # Validate password
        if not password1 == password2:
            raise ValidationException(
                detail="Password validation failed",
                extra={
                    "password1": "Passwords do not match",
                    "password2": "Passwords do not match",
                },
            )
        try:
            self.password_validator.validate(password1)
        except ValueError as error:
            raise ValidationException(
                detail="Password validation failed", extra={"password": error}
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
