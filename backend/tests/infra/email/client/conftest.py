# External Libraries
import pytest

# VerdanTech Source
from src.infra.email.client.aiosmtplib import AioSmtplibEmailClient
from src.infra.email.client.generic import BaseEmailClient


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
    return AioSmtplibEmailClient(
        client_hostname="",
        client_port=0,
        client_username="",
        client_password="",
        sender="",
    )
