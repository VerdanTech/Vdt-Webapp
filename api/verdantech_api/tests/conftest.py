import pytest
from rest_framework.test import APIClient

from .accounts_test.factories import UserFactory
from .gardens_test.factories import BaseGardenFactory, GardenFactory


@pytest.fixture
def csrf_client():
    csrf_client = APIClient(enforce_csrf_checks=True)
    csrf_client.defaults["HTTP_ACCEPT"] = "application/json"
    return csrf_client


@pytest.fixture
def client():
    client = APIClient(enforce_csrf_checks=False)
    client.defaults["HTTP_ACCEPT"] = "application/json"
    return client


@pytest.fixture
def UserMake():
    return UserFactory


@pytest.fixture
def BaseGardenMake():
    return BaseGardenFactory


@pytest.fixture
def GardenMake():
    return GardenFactory
