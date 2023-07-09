import pytest
from src.verdantech_api.lib.email.aiosmtplib import aioSMTPLibEmailClient
from src.verdantech_api.lib.email.generic import AsyncEmailClient


@pytest.fixture
def generic_async_client():
    return AsyncEmailClient(
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
