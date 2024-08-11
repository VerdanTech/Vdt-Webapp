# Standard Library
from datetime import datetime

# External Libraries
import pytest
from faker import Faker

# VerdanTech Source
from src.user.domain import Email, User

fake = Faker()


@pytest.fixture
def email():
    return Email(address=fake.email(), primary=True, verified=False)


@pytest.fixture
def user() -> User:
    user = User(username=fake.name())
    user.emails = [Email(address=fake.email(), primary=True, verified=True)]
    user._password_hash = "some_password"
    user.created_at = datetime.now()
    user.events = []
    return user
