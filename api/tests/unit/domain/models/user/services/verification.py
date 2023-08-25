from typing import List
import pytest
from pytest_mock import MockerFixture

from litestar.contrib.repository.abc import (
    AbstractAsyncRepository,
)


from src.verdantech_api.domain.models.user.services.verification import (
    VerificationService,
)
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.values import PasswordResetConfirmation


class TestVerificationService:
    async def test_generate_open_email_confirmation_key(self):
        pass

    async def test_generate_open_password_reset_key(
        self,
    ):
        pass

    @pytest.mark.skip
    @pytest.mark.parametrize(
        ("generated_keys", "existing_users", "field_name", "expected_output"),
        [
            (
                ["abc"],
                [],
                "password_reset_confirmation.key",
                "abc",
            ),
            (
                ["abc", "123"],
                [
                    User(
                        username="existing_user",
                        password_reset_confirmation=PasswordResetConfirmation(
                            password_hash="test_password::hash", key="abc"
                        ),
                    )
                ],
                "password_reset_confirmation.key",
                "123",
            ),
        ],
    )
    async def test_generate_open_key(
        self,
        generated_keys: List[str],
        existing_users: List[User],
        field_name: str,
        expected_output: str,
        verification_service: VerificationService,
        mock_user_repo: AbstractAsyncRepository,
        mocker: MockerFixture,
    ):
        length = 8
        mock_key_generator = mocker.patch(
            "src.verdantech_api.domain.models.user.services.verification.key_generator",
            side_effect=generated_keys,
        )

        await mock_user_repo.add_many(existing_users)

        assert (
            await verification_service.generate_open_key(
                length=length, repo=mock_user_repo, field_name=field_name
            )
            == expected_output
        )
        mock_key_generator.assert_called_with(length=length)
