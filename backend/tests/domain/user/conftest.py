# External Libraries
import factory
import pytest

# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository
from src.domain.user.entities import User
from src.domain.user.values import Email


class EmailMake(factory.Factory):
    class Meta:
        model = Email

    address = factory.Faker("email")
    primary = True


@pytest.fixture
def email():
    return EmailMake.build()


class UserMake(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker("name")

    @factory.post_generation
    def _password_hash(self, create, extracted, **kwargs):
        self._password_hash = "some_password"
        self.emails = [EmailMake.build()]


@pytest.fixture
def user():
    return UserMake.build()


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()
