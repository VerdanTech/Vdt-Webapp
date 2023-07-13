from typing import TYPE_CHECKING, Callable

from litestar.exceptions import ValidationException

from verdantech_api import settings
from verdantech_api.lib.email.generic import AsyncEmailClient
from verdantech_api.lib.utils import StringIDGeneratorT

from ..models import EmailConfirmationModel, EmailModel
from ..models.repos import EmailConfirmationRepo

if TYPE_CHECKING:
    from litestar import Litestar

    from .users import EmailRepo


class VerificationService:
    def __init__(
        self,
        email_client: AsyncEmailClient,
        email_repo: EmailRepo,
        email_confirmation_repo: EmailConfirmationRepo,
        key_generator: Callable[[int, str], str],
    ):
        self.email_client = email_client
        self.email_repo = email_repo
        self.email_confirmation_repo = email_confirmation_repo
        self.key_generator = key_generator

    async def send_email_verification(self, email: EmailModel, app: Litestar) -> None:
        """Generate verification key, update database, and send email

        Args:
            email (str): the email to verify

        Raises:
            Exception: _description_
        """

        # Prevent re-verification
        if email.is_verified:
            raise ValidationException(detail="Email is already verified")

        # Remove any active email confirmations

        # Generate verification key
        key = self.key_generator(size=settings.EMAIL_VERIFICATION_KEY_LENGTH)
        while await self.email_confirmation_repo.get_one_or_none(key=key) is not None:
            key = self.key_generator(size=settings.EMAIL_VERIFICATION_KEY_LENGTH)

        # Create database object
        email_confirmation = EmailConfirmationModel(key=key)
        email.confirmations = {email_confirmation}

        # Add to repo
        await self.email_repo.update(email)
        await self.email_confirmation_repo.add(email_confirmation)

        # Emit email
        app.emit(
            "emit_email",
            receiver=email.email,
            subject="Email verification - VerdanTech",
            filepath=settings.email_path("email_verification.html"),
            username=email.user.username,
            client_base_url=settings.CLIENT_BASE_URL,
            verification_url=settings.EMAIL_VERIFICATION_CLIENT_URL + key,
        )

    async def verify_email(self, key: str) -> None:
        """Verifies the email and updates user emails

        Args:
            key (str): the email verification key

        """

        # Get email confirmation
        email_confirmation = await self.email_confirmation_repo.get_one_or_none(key=key)
        if email_confirmation is None:
            return Exception  # todo

        # Validate email confirmation expiry
        if email_confirmation.is_expired():
            self.email_confirmation_repo.remove(email_confirmation)
            return Exception  # todo

        # Update verification on email model
        email = email_confirmation.email
        email.is_verified = True
        await self.email_repo.update(email)

        user_id = email.user.id
        # Remove the oldest email
        user_emails = await self.email_service.remove_oldest_email(user_id=user_id)
        # Update primary status on the rest of the emails
        await self.email_service.set_new_primary_email(
            user_id=user_id, user_emails=user_emails
        )

        # Delete email confirmation
        await self.email_confirmation_repo.remove(email_confirmation)
