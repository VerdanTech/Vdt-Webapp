from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from litestar.contrib.repository.abc import AbstractAsyncRepository
from litestar.exceptions import ValidationException
from src.verdantech_api import settings
from src.verdantech_api.lib.email.generic import AsyncEmailClient
from src.verdantech_api.lib.utils import StringIDGeneratorT

from ..models.models import EmailConfirmationModel, EmailModel
from ..models.repos import EmailConfirmationRepo, EmailRepo
from .email_confirmation import EmailConfirmationService

if TYPE_CHECKING:
    from litestar import Litestar

    from .users import EmailRepo


class VerificationService:
    def __init__(
        self,
        email_client: AsyncEmailClient,
        email_repo: EmailRepo,
        email_confirmation_repo: EmailConfirmationRepo,
        email_confirmation_service: EmailConfirmationService,
        key_generator: StringIDGeneratorT,
    ):
        self.email_client = email_client
        self.email_repo = email_repo
        self.email_confirmation_repo = email_confirmation_repo
        self.email_confirmation_service = email_confirmation_service
        self.key_generator = key_generator

    async def send_email_verification(self, email: EmailModel, app: Litestar) -> None:
        """Generate verification key, update database, and send email

        Args:
            email (str): the email to verify

        Raises:
            Exception: _description_
        """

        self.email_unverified_or_exception(email=email)

        await self.email_confirmation_service.remove_active_confirmations()

        key = await self.generate_open_key(
            repo=self.email_repo, length=settings.EMAIL_VERIFICATION_KEY_LENGTH
        )

        (
            email,
            email_confirmation,
        ) = await self.email_confirmation_service.create_email_confirmation(
            key=key, email=email
        )

        # Emit email
        app.emit(
            "emit_email",
            receiver=email.address,
            subject="Email verification - VerdanTech",
            filepath=settings.email_path("email_verification.html"),
            username=email.user.username,
            client_base_url=settings.CLIENT_BASE_URL,
            verification_url=settings.EMAIL_VERIFICATION_CLIENT_URL + key,
        )

    def email_unverified_or_exception(self, email: EmailModel) -> None:
        if email.is_verified:
            raise ValidationException(detail="Email is already verified")

    async def generate_open_key(
        self, repo: AbstractAsyncRepository, length: int
    ) -> str:
        key = self.key_generator(length=length)
        while await repo.exists(key=key):
            key = self.key_generator(length=length)
        return key

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
