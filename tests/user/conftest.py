# Standard Library
from datetime import datetime

# External Libraries
import factory
import pytest
from faker import Faker

# VerdanTech Source
from src.user.domain import Email, User

fake = Faker()


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
    def post_init(self, create, extracted, **kwargs):
        self._password_hash = "some_password"
        self.emails = [EmailMake.build()]
        self.created_at = datetime.now()
        self.events = []


@pytest.fixture
def user() -> User:
    user = User(username=fake.name())
    user.emails = [Email(address=fake.email(), primary=True, verified=True)]
    user._password_hash = "some_password"
    user.created_at = datetime.now()
    user.events = []
    return user
