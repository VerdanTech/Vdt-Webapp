from typing import Callable

import pytest
from litestar.contrib.repository.abc import AbstractAsyncRepository
from litestar.contrib.repository.testing.generic_mock_repository import (
    GenericAsyncMockRepository,
)
from pytest_mock import MockerFixture
from src.verdantech_api.domain.users.models.models import EmailModel, UserModel
from src.verdantech_api.domain.users.services.user import UserService
from src.verdantech_api.domain.users.services.validation import (
    UserFieldsSanitizerService,
)
from src.verdantech_api.lib.utils import IdFactory
from src.verdantech_api.lib.validators.concrete.email import EmailValidator
from src.verdantech_api.lib.validators.concrete.password import PasswordValidator
from src.verdantech_api.lib.validators.concrete.username import UsernameValidator


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
def user_service(
    mock_user_repo: GenericAsyncMockRepository,
    mock_email_repo: GenericAsyncMockRepository,
    mocker: MockerFixture,
):
    return UserService(user_repo=mock_user_repo, email_repo=mock_email_repo)


class MockUserRepo(GenericAsyncMockRepository[UserModel]):
    model_type = UserModel


@pytest.fixture
def mock_user_repo(id_factory: Callable[[], int]):
    mock_user_repo = MockUserRepo(id_factory=id_factory)
    return mock_user_repo


class MockEmailRepo(GenericAsyncMockRepository[EmailModel]):
    model_type = EmailModel


@pytest.fixture
def mock_email_repo(id_factory: Callable[[], int]):
    mock_email_repo = MockEmailRepo(id_factory=id_factory)
    return mock_email_repo
