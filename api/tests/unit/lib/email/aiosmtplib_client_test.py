from email.mime.multipart import MIMEMultipart
from typing import ContextManager

import pytest
from aiosmtplib.errors import SMTPException
from litestar.exceptions import InternalServerException
from pytest_mock import MockerFixture
from src.verdantech_api.lib.email.aiosmtplib import aioSMTPLibEmailClient


@pytest.mark.parametrize(
    ["exception", "error_context"],
    [(None, None), (SMTPException(""), InternalServerException)],
    indirect=["error_context"],
)
class TestAIOSMTPLibClient:
    async def test_send(
        self,
        exception: Exception,
        aiosmtplib_client: aioSMTPLibEmailClient,
        error_context: ContextManager,
        mocker: MockerFixture,
    ):
        """Ensure that the send method calls the aiosmtplib send method
            and raises an InternalServerException when it fails

        Args:
            exception (Exception): the exception for the aiosmtplib send
            method to raise
            aiosmtplib_client (aioSMTPLibEmailClient): provider of an
                aioSMTPLibEmailClient to test on
            error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
            mocker (MockerFixture): pytest-mock
        """
        aiosmtp_send_mock = mocker.patch(
            "src.verdantech_api.lib.email.aiosmtplib.aiosmtp_send"
        )
        if exception is not None:
            aiosmtp_send_mock.side_effect = exception

        message = MIMEMultipart()

        with error_context:
            await aiosmtplib_client.send(
                message=message,
                client_hostname="",
                client_port=0,
                client_username="",
                client_password="",
            )

        aiosmtp_send_mock.assert_called_once_with(
            message, hostname="", port=0, username="", password="", use_tls=True
        )
