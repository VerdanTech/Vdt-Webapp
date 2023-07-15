from typing import ContextManager

import pytest
from litestar.exceptions import ValidationException
from pytest_mock import MockerFixture
from src.verdantech_api.domain.users.models.models import (
    EmailConfirmationModel,
    EmailModel,
)
from src.verdantech_api.domain.users.services.verification import VerificationService


class TestVerificationService:
    def test_send_email_confirmation(self):
        pass

    @pytest.mark.parametrize(
        ["is_verified", "error_context"],
        [(False, None), (True, ValidationException)],
        indirect=["error_context"],
    )
    def test_email_unverified_or_exception(
        self,
        is_verified: bool,
        verification_service: VerificationService,
        error_context: ContextManager,
        mocker: MockerFixture,
    ):
        email = EmailModel(address="email@email.com", is_verified=is_verified)

        with error_context:
            verification_service.email_unverified_or_exception(email=email)

    def test_remove_active_confirmations(self):
        pass

    async def test_generate_open_key(
        self, verification_service: VerificationService, mocker: MockerFixture
    ):
        test_keys = ["nisSTNt", "cUqncAI"]

        verification_service.key_generator.side_effect = test_keys

        existing_email_confirmation = EmailConfirmationModel(key=test_keys[0])
        await verification_service.email_confirmation_repo.add(
            existing_email_confirmation
        )

        key = await verification_service.generate_open_key(
            repo=verification_service.email_confirmation_repo, length=0
        )

        assert key == test_keys[1]
        assert verification_service.key_generator.call_count == 2

    def test_send_email_confirmation_email(self):
        pass

    def test_create_password_resed(self):
        pass

    def test_send_password_reset_email(self):
        pass
