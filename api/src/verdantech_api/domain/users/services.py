from typing import Any

from email_validator import EmailNotValidError, validate_email
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.exceptions import ValidationException

from api.src.verdantech_api.lib.services import AsyncRepoService

from .models import UserModel


class UserRepo(SQLAlchemyAsyncRepository[UserModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = UserModel


class UserService(AsyncRepoService[UserModel]):
    """Handles database operations for users"""

    repo_type = UserRepo

    def __init__(self, **repo_kwargs: Any) -> None:
        self.repo: UserRepo = self.repo_type_(**repo_kwargs)
        self.model_type = self.repo.model_type

    async def register():
        
        # validate email
        # create user
        # send verification email

        pass

    async def resend_email_verification():

        # send verification email

        pass

    async def verify_email():

        # validate email 
        # update user object


        pass


    async def change_password():
        pass 

    async def reset_password():
        pass

    async def reset_password_confirm():
        pass

class EmailService:

    def validate_and_normalize_email(self, email: str) -> str:
        """Validate and normalize email address using email-validator

        Args:
            email (str): the email to operate on

        Raises:
            ValidationException: raised if email validation fails

        Returns:
            str: the normalized email address
        """

        try:
            validated_email = validate_email(email, check_deliverability=False)
            email = validated_email.normalized
        except EmailNotValidError as exc:
            raise ValidationException(detail=f"{exc}")

        return email
    
    def send_email():
        pass

class EmailVerificationService():
    pass

class PasswordResetService():
    pass

class AuthService():
    pass