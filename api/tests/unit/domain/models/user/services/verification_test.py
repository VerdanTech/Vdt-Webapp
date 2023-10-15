from typing import List

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services.verification import (
    EmailVerificationService,
    PasswordResetService,
    VerificationService,
)
from src.verdantech_api.domain.models.user.values import PasswordResetConfirmation
from src.verdantech_api.infrastructure.persistence.repository.mock.user.repository import (
    MockUserRepository,
)


class TestVerificationService:
    async def test_generate_open_email_confirmation_key(
        self,
        verification_service: VerificationService,
        mock_user_repo: MockUserRepository,
        mocker: MockerFixture,
    ):
        """Ensure that the generalized open key method is called
            with the right parameters, and the key is returned

        Args:
            verification_service (VerificationService): fixture providing
                verification service to test on
            mock_user_repo (MockUserRepository): fixture providing mock
                user repoistory to test on
            mocker (MockerFixture): pytest-mock
        """
        mock_generate_open_key = mocker.patch.object(
            VerificationService, "generate_open_key", return_value="abc"
        )

        assert (
            await verification_service.generate_open_email_confirmation_key(
                length=0, user_repo=mock_user_repo
            )
            == "abc"
        )
        mock_generate_open_key.assert_called_once_with(
            length=0,
            repo=mock_user_repo,
            uniqueness_method_name="email_confirmation_key_exists",
        )

    async def test_generate_open_password_reset_key(
        self,
        verification_service: VerificationService,
        mock_user_repo: MockUserRepository,
        mocker: MockerFixture,
    ):
        """Ensure that the generalized open key method is called
            with the right parameters, and the key is returned

        Args:
            verification_service (VerificationService): fixture providing
                verification service to test on
            mock_user_repo (MockUserRepository): fixture providing mock
                user repoistory to test on
            mocker (MockerFixture): pytest-mock
        """
        mock_generate_open_key = mocker.patch.object(
            VerificationService, "generate_open_key", return_value="abc"
        )

        assert (
            await verification_service.generate_open_password_reset_key(
                length=0, user_repo=mock_user_repo
            )
            == "abc"
        )
        mock_generate_open_key.assert_called_once_with(
            length=0,
            repo=mock_user_repo,
            uniqueness_method_name="password_reset_confirmation_key_exists",
        )

    @pytest.mark.parametrize(
        ("generated_keys", "existing_users", "expected_output"),
        [
            # Test case: key is unique, and it is returned
            (
                ["abc"],
                [],
                "abc",
            ),
            # Test case: key is not unique, another generated, and it is returned
            (
                ["abc", "123"],
                [
                    User(
                        username="existing_user",
                        password_reset_confirmation=PasswordResetConfirmation(
                            key="abc"
                        ),
                    )
                ],
                "123",
            ),
        ],
    )
    async def test_generate_open_key(
        self,
        generated_keys: List[str],
        existing_users: List[User],
        expected_output: str,
        verification_service: VerificationService,
        mock_user_repo: MockUserRepository,
        mocker: MockerFixture,
    ):
        """Ensure the generalized open key function generated a unique key
            given a repository uniqueness function

        Args:
            generated_keys (List[str]): mock keys to generate
            existing_users (List[User]): existing users in repository
            expected_output (str): expected unique key returned
            verification_service (VerificationService): fixture providing verification
                service object to test on
            mock_user_repo (MockUserRepository): fixture providing mock user repository
            mocker (MockerFixture): pytest-mock
        """
        mock_key_generator = mocker.patch(
            "src.verdantech_api.domain.models.user.services.verification.key_generator",
            side_effect=generated_keys,
        )

        await mock_user_repo.add_many(existing_users)

        assert (
            await verification_service.generate_open_key(
                length=0,
                repo=mock_user_repo,
                uniqueness_method_name="password_reset_confirmation_key_exists",
            )
            == expected_output
        )
        mock_key_generator.assert_called_with(length=0)


class TestEmailVerificationService:
    async def test_new_verification(self, user: User, mocker: MockerFixture) -> None:
        """Ensure the verification service is called and the generated key is
            returned, and the user new email veification method is called

        Args:
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        generated_key = "abc"
        address = "test@test.com"
        mock_user_repo = mocker.Mock()
        mock_generate_open_email_confirmation_key = mocker.patch(
            "src.verdantech_api.domain.models.user.services.verification.VerificationService.generate_open_email_confirmation_key",
            return_value=generated_key,
        )
        mock_new_email_verification = mocker.patch.object(
            user, "new_email_verification"
        )

        key = await EmailVerificationService.new_verification(
            user=user, address=address, key_length=0, user_repo=mock_user_repo
        )

        assert key == generated_key
        mock_generate_open_email_confirmation_key.assert_awaited_once_with(
            length=0, user_repo=mock_user_repo
        )
        mock_new_email_verification.assert_called_once_with(address=address, key=key)


class TestPasswordResetService:
    async def test_new_verification(self, user: User, mocker: MockerFixture) -> None:
        """Ensure the verification service is called and the generated key is
            returned, and the user new password reset method is called

        Args:
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        generated_key = "abc"
        mock_user_repo = mocker.Mock()
        mock_generate_open_password_reset_key = mocker.patch(
            "src.verdantech_api.domain.models.user.services.verification.VerificationService.generate_open_password_reset_key",
            return_value=generated_key,
        )
        mock_new_password_reset = mocker.patch.object(user, "new_password_reset")

        key = await PasswordResetService.new_password_reset(
            user=user, key_length=0, user_repo=mock_user_repo
        )

        assert key == generated_key
        mock_generate_open_password_reset_key.assert_awaited_once_with(
            length=0, user_repo=mock_user_repo
        )
        mock_new_password_reset.assert_called_once_with(key=key)
