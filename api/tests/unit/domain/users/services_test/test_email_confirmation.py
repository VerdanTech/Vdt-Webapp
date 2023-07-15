import pytest
from src.verdantech_api.domain.users.models.models import EmailModel
from src.verdantech_api.domain.users.services.email_confirmation import (
    EmailConfirmationService,
)


class TestEmailConfirmationService:
    async def test_create_email_confirmation(
        self, email_confirmation_service: EmailConfirmationService
    ):
        input_key = "cUqncAI"
        input_email = EmailModel(address="email@email.py")
        input_email = await email_confirmation_service.email_repo.add(input_email)

        (
            email,
            email_confirmation,
        ) = await email_confirmation_service.create_email_confirmation(
            key=input_key,
            email=input_email,
        )

        assert email_confirmation in email.confirmations
        assert email_confirmation.key == input_key
