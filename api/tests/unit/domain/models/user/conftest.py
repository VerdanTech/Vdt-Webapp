import factory
import pytest
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.values import Email


class UserMake(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker("name")


@pytest.fixture
def user():
    return UserMake.build()


class EmailMake(factory.Factory):
    class Meta:
        model = Email

    address = factory.Faker("email")


@pytest.fixture
def email():
    return EmailMake.build()
