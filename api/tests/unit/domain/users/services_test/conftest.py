from typing import Callable

import pytest
from litestar.contrib.repository.abc import AbstractAsyncRepository
from litestar.contrib.repository.testing.generic_mock_repository import (
    GenericAsyncMockRepository,
)
from pytest_mock import MockerFixture
from src.verdantech_api.domain.users.models.models import (
    EmailConfirmationModel,
    EmailModel,
    UserModel,
)
from src.verdantech_api.domain.users.services.email_confirmation import (
    EmailConfirmationService,
)
from src.verdantech_api.domain.users.services.user import UserService
from src.verdantech_api.domain.users.services.validation import (
    UserFieldsSanitizerService,
)
from src.verdantech_api.domain.users.services.verification import VerificationService
from src.verdantech_api.lib.email.generic import AsyncEmailClient
from src.verdantech_api.lib.utils import IdFactory, key_generator
from src.verdantech_api.lib.validators.concrete.email import EmailValidator
from src.verdantech_api.lib.validators.concrete.password import PasswordValidator
from src.verdantech_api.lib.validators.concrete.username import UsernameValidator

############-------------------
############------------------- SERVICES
############-------------------


@pytest.fixture
def user_fields_sanitizer_service(mocker: MockerFixture):
    return UserFieldsSanitizerService(
        username_validator=mocker.MagicMock(spec=UsernameValidator),
        email_validator=mocker.MagicMock(spec=EmailValidator),
        password_validator=mocker.MagicMock(spec=PasswordValidator),
        user_repo=mocker.MagicMock(spec=AbstractAsyncRepository),
        email_repo=mocker.MagicMock(spec=AbstractAsyncRepository),
    )


@pytest.fixture
def verification_service(
    id_factory: Callable[[], int],
    mock_email_repo: GenericAsyncMockRepository,
    mock_email_confirmation_repo: GenericAsyncMockRepository,
    mocker: MockerFixture,
):
    return VerificationService(
        email_client=mocker.MagicMock(spec=AsyncEmailClient),
        email_repo=mock_email_repo,
        email_confirmation_repo=MockEmailConfirmationRepo(id_factory=id_factory),
        email_confirmation_service=mocker.MagicMock(spec=EmailConfirmationService),
        key_generator=mocker.Mock(spec=key_generator),
    )


############-------------------
############------------------- MODEL SERVICES
############-------------------


@pytest.fixture
def user_service(
    mock_user_repo: "MockUserRepo",
    mock_email_repo: "MockEmailRepo",
):
    return UserService(user_repo=mock_user_repo, email_repo=mock_email_repo)


@pytest.fixture
def email_confirmation_service(
    mock_email_repo: "MockEmailRepo",
    mock_email_confirmation_repo: "MockEmailConfirmationRepo",
):
    return EmailConfirmationService(
        email_repo=mock_email_repo, email_confirmation_repo=mock_email_confirmation_repo
    )


############-------------------
############------------------- REPOSITORIES
############-------------------


class MockUserRepo(GenericAsyncMockRepository[UserModel]):
    model_type = UserModel


class MockEmailRepo(GenericAsyncMockRepository[EmailModel]):
    model_type = EmailModel


class MockEmailConfirmationRepo(GenericAsyncMockRepository[EmailConfirmationModel]):
    model_type = EmailConfirmationModel


@pytest.fixture
def mock_user_repo(id_factory: Callable[[], int]):
    mock_user_repo = MockUserRepo(id_factory=id_factory)
    mock_user_repo.collection = {}
    return mock_user_repo


@pytest.fixture
def mock_email_repo(id_factory: Callable[[], int]):
    mock_email_repo = MockEmailRepo(id_factory=id_factory)
    mock_email_repo.collection = {}
    return mock_email_repo


@pytest.fixture
def mock_email_confirmation_repo(id_factory: Callable[[], int]):
    mock_email_confirmation_repo = MockEmailConfirmationRepo(id_factory=id_factory)
    mock_email_confirmation_repo.collection = {}
    return mock_email_confirmation_repo
