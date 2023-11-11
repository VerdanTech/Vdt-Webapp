import pytest
from pytest_mock import MockerFixture
from src.domain.user.entities import User
from src.domain.user.services import email as services
from src.infra.persistence.repository.mock.user.repository import MockUserRepository

pytestmark = [pytest.mark.unit]


async def test_email_create_verification_false_success(user: User) -> None:
    address = "test@test.com"
    # key

    # wait services.email_create(user, address=, max_emails=, verification=False, key_length= user_repo=)


async def test_email_create_verification_true_value_error() -> None:
    pass


async def test_email_create_verification_true_success() -> None:
    pass
