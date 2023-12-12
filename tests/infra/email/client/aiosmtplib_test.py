# Standard Library
from email.mime.multipart import MIMEMultipart
from typing import ContextManager

# External Libraries
import pytest
from aiosmtplib.errors import SMTPException
from pytest_mock import MockerFixture

# VerdanTech Source
from src.infra.email.client.aiosmtplib import AioSmtplibEmailClient
from src.interfaces.email.exceptions import EmailError

pytestmark = [pytest.mark.unit]


@pytest.mark.skip
@pytest.mark.parametrize(
    ["exception", "expected_error_context"],
    [(None, None), (SMTPException(""), EmailError)],
    indirect=["expected_error_context"],
)
class TestAioSmtplibEmailClient:
    # ======================================
    # AioSmtplibEmailClient.send() tests
    # ======================================

    async def test_send(
        self,
        exception: Exception,
        aiosmtplib_client: AioSmtplibEmailClient,
        expected_error_context: ContextManager,
        mocker: MockerFixture,
    ):
        """
        Ensure that the send method calls the aiosmtplib send method
        and raises an InternalServerException when it fails.

        Args:
            exception (Exception): the exception for the aiosmtplib send
                method to raise.
            aiosmtplib_client (aioSMTPLibEmailClient): provider of an
                aioSMTPLibEmailClient to test on.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            mocker (MockerFixture): pytest-mock.
        """
        aiosmtp_send_mock = mocker.patch(
            "src.infra.email.client.aiosmtplib.aiosmtp_send"
        )
        if exception is not None:
            aiosmtp_send_mock.side_effect = exception

        message = MIMEMultipart()

        with expected_error_context:
            await aiosmtplib_client.send(
                message=message,
            )

        aiosmtp_send_mock.assert_called_once_with(
            message, hostname="", port=0, username="", password="", use_tls=True
        )
