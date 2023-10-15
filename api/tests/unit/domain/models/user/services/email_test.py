from pytest_mock import MockerFixture
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.services.email import EmailAdditionService
from src.verdantech_api.infrastructure.persistence.repository.mock.user.repository import (
    MockUserRepository,
)


class TestEmailAdditionService:
    async def test_add_first_email_verification_required(
        self, mock_user_repo: MockUserRepository, mocker: MockerFixture
    ):
        """Ensure the key generation and user add email methods are called
            with the correct parameters

        Args:
            mock_user_repo (MockUserRepository): mock user repo
            mocker (MockerFixture): pytest-mock
        """
        mock_user = mocker.MagicMock(spec=User)
        mock_key_generation = mocker.patch(
            "src.verdantech_api.domain.models.user.services.verification.VerificationService.generate_open_email_confirmation_key",
            return_value="abc",
        )

        key = await EmailAdditionService.add_first_email_verification_required(
            user=mock_user,
            address="test@test.com",
            key_length=0,
            user_repo=mock_user_repo,
        )

        assert key == "abc"
        mock_key_generation.assert_awaited_once_with(length=0, user_repo=mock_user_repo)
        mock_user.add_email.assert_called_once_with(
            address="test@test.com", primary=True, key=key
        )

    def test_add_first_email_verification_not_required(self, mocker: MockerFixture):
        """Ensure the user add email method is called
            with the correct parameters

        Args:
            mocker (MockerFixture): pytest-mock
        """
        mock_user = mocker.MagicMock(spec=User)

        EmailAdditionService.add_first_email_verification_not_required(
            user=mock_user,
            address="test@test.com",
        )

        mock_user.add_verified_email.assert_called_once_with(
            address="test@test.com", primary=True
        )

    async def test_add_non_first_email_verification_required(
        self, mock_user_repo: MockUserRepository, mocker: MockerFixture
    ):
        """Ensure the key generation and user add email methods are called
            with the correct parameters

        Args:
            mock_user_repo (MockUserRepository): mock user repo
            mocker (MockerFixture): pytest-mock
        """
        mock_user = mocker.MagicMock(spec=User)
        mock_key_generation = mocker.patch(
            "src.verdantech_api.domain.models.user.services.verification.VerificationService.generate_open_email_confirmation_key",
            return_value="abc",
        )

        key = await EmailAdditionService.add_non_first_email_verification_required(
            user=mock_user,
            address="test@test.com",
            key_length=0,
            user_repo=mock_user_repo,
        )

        assert key == "abc"
        mock_key_generation.assert_awaited_once_with(length=0, user_repo=mock_user_repo)
        mock_user.add_email.assert_called_once_with(
            address="test@test.com", primary=False, key=key
        )

    def test_add_non_first_email_verification_not_required(self, mocker: MockerFixture):
        """Ensure the user add email method is called
            with the correct parameters

        Args:
            mocker (MockerFixture): pytest-mock
        """
        mock_user = mocker.MagicMock(spec=User)

        EmailAdditionService.add_non_first_email_verification_not_required(
            user=mock_user,
            address="test@test.com",
        )

        mock_user.add_verified_email.assert_called_once_with(
            address="test@test.com", primary=True
        )
