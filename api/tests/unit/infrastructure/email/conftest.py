import pytest
from src.verdantech_api.infrastructure.email.aiosmtplib.client import (
    aioSMTPLibEmailClient,
)
from src.verdantech_api.infrastructure.email.generic import BaseEmailClient


@pytest.fixture
def base_email_client():
    return BaseEmailClient(
        client_hostname="",
        client_port=0,
        client_username="",
        client_password="",
        sender="",
    )


@pytest.fixture
def aiosmtplib_client():
    return aioSMTPLibEmailClient(
        client_hostname="",
        client_port=0,
        client_username="",
        client_password="",
        sender="",
    )
