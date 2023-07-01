from typing import TypeVar

from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from pydantic import SecretStr

from verdantech_api.lib.crypt import (
    GeneratePasswordHashAwaitableT,
    VerifyPasswordHashAwaitableT,
)
from verdantech_api.lib.email.generic import AsyncEmailClient
from verdantech_api.lib.utils import StringIDGeneratorT
from verdantech_api.settings import CLIENT_BASE_URL, EMAIL_VERIFICATION_CLIENT_URL

from ..models import EmailConfirmationModel, EmailModel
from .users import EmailRepoT

EmailConfirmationRepoT = TypeVar("EmailConfirmationRepoT", bound="EmailConfirmationRepo")

class EmailConfirmationRepo(SQLAlchemyAsyncRepository[EmailConfirmationModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = EmailConfirmationModel


class EmailVerificationService:
    """Handles verification of email for new users
    and for adding/changing primary email address"""

    email_client: AsyncEmailClient
    email_repo: EmailRepoT
    email_confirmation_repo: EmailConfirmationRepoT
    key_generator: StringIDGeneratorT
    password_hasher: GeneratePasswordHashAwaitableT
    password_verifier: VerifyPasswordHashAwaitableT

    def __init__(
        self,
        email_client: AsyncEmailClient,
        email_repo: EmailRepoT,
        email_confirmation_repo: EmailConfirmationRepoT,
        key_generator: StringIDGeneratorT,
        password_hasher: GeneratePasswordHashAwaitableT,
        password_verifier: VerifyPasswordHashAwaitableT,
    ):
        self.email_client = email_client
        self.email_repo = email_repo
        self.email_confirmation_repo = email_confirmation_repo
        self.key_generator = key_generator
        self.password_hasher = password_hasher
        self.password_verifier = password_verifier

    async def send_email_verification(self, email: str) -> None:
        """Generate verification key, send in database, and send email

        Args:
            email (str): the email to verify

        Raises:
            Exception: _description_
        """        

        # Query email model from database
        email = await self.email_repo.get_one_or_none(email=email)
        if not email:
            raise Exception  # make application exception

        # Generate verification key
        key = self.key_generator(size=32)
        key_hash: SecretStr = await self.password_hasher(key)

        # Create database object
        email_confirmation = EmailConfirmationModel(key_hash=key_hash)
        email.confirmations = {email_confirmation}

        # Add to repo
        await self.email_repo.update(email)
        await self.email_confirmation_repo.add(email_confirmation)

        # Send email
        self.email_client

        await self.email_client.send_email(
        receiver=email.email,
        subject="Email verification - VerdanTech",
        filepath="", #todo
        username=email.user.username,
        client_base_url=CLIENT_BASE_URL,
        verification_url=EMAIL_VERIFICATION_CLIENT_URL+key,
    )


    async def verify_email():
        # validate email
        # update user object

        pass

    async def send_email_change_verification():
        pass
