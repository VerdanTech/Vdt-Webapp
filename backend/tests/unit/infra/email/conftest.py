import pytest
from backend.src.infra.email.client.generic import BaseEmailClient
from src.infra.email.aiosmtplib.client import aioSMTPLibEmailClient


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
