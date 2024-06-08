# Standard Library
from datetime import datetime

# External Libraries
import factory
import pytest

# VerdanTech Source
from src.user.domain import User
from src.user.domain.email import Email


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
        self.created_at = datetime.now()


@pytest.fixture
def user():
    return UserMake.build()
