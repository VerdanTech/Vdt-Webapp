from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, ContextManager, Dict

import pytest
from pytest_mock import MockerFixture
from src.infrastructure.email.generic import BaseEmailClient


class TestBaseEmailClient:
    @pytest.mark.parametrize(
        ["input_html", "expected_output", "kwargs", "expected_error_context"],
        [
            # Test case: no kwargs.
            (
                "<h1>Test arg1 and {not} andarg2</h1>",
                "<h1>Test arg1 and {not} andarg2</h1>",
                {},
                None,
            ),
            # Test case: normal use case with all kwargs provided.
            (
                "<h1>Test {{kw1}} and {not} and{{kw2}}</h1>",
                "<h1>Test arg1 and {not} andarg2</h1>",
                {"kw1": "arg1", "kw2": "arg2"},
                None,
            ),
            # Test case: Single variable appearing more than once in the template.
            (
                "<p>{{kw1}}</p><p>{{kw1}}</p>",
                "<p>arg1</p><p>arg1</p>",
                {"kw1": "arg1"},
                None,
            ),
            # Test case: Exception raised when HTML content
            # has no variables and kwargs provided.
            (
                "<p>Static content</p>",
                "<p>Static content</p>",
                {"kw1": "arg1"},
                ValueError,
            ),
            # Test case: HTML escaping functionality.
            (
                "<p>{{kw1}}</p>",
                "<p>&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;</p>",
                {"kw1": "<script>alert('xss')</script>"},
                None,
            ),
            # Test case: Exception raised when no kwargs provided
            # and HTML content has variables.
            ("<p>{{kw1}}</p>", "<p></p>", {}, ValueError),
            # Test case: exception raised when kwargs doesn't contain all required keys.
            ("{{kw1}} {{kw2}}", "", {"kw1": "arg1"}, ValueError),
        ],
        indirect=["expected_error_context"],
    )
    def test_template_html(
        self,
        input_html: str,
        expected_output: str,
        kwargs: Dict[str, Any],
        expected_error_context: ContextManager,
        base_email_client: BaseEmailClient,
    ):
        """Ensure that output == expected given kwargs

        Args:
            input_html (str): The input after reading file
            expected_output (str): The expected output
            kwargs (Dict[str, Any]): The arguments to be inserted int input
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise. See: tests/conftest.py
            generic_async_client (AsyncEmailClient): provider of a AsyncEmailClient
                to test on
        """
        with expected_error_context:
            html = base_email_client.template_html(html_content=input_html, **kwargs)
            assert html == expected_output

    @pytest.mark.parametrize(["html", "expected_output"], [("<p>Test</p>", "Test")])
    def test_html_to_plain(
        self,
        html: str,
        expected_output: str,
        base_email_client: BaseEmailClient,
        mocker: MockerFixture,
    ):
        """Ensure that the html to plain text conversion function
            properly calls the conversion function it depends on

        Args:
            html (str): the input html
            expected_output (str): the expected output html
            generic_async_client (AsyncEmailClient): provider of a AsyncEmailClient
                to test on
            mocker (MockerFixture): pytest-mock
        """
        mocked_processor = mocker.patch(
            "src.infrastructure.email.generic.html2text.HTML2Text.handle",
            return_value=expected_output,
        )
        output = base_email_client.html_to_plain_text(html_content=html)
        mocked_processor.assert_called_once()
        assert output == expected_output

    @pytest.mark.parametrize(
        ["sender", "receiver", "subject", "plain_text_message", "html_message"],
        [
            (
                "sender@example.com",
                "receiver@example.com",
                "Test Subject",
                "Plain text message content",
                "<p>HTML message content</p>",
            )
        ],
    )
    def test_compile_message(
        self,
        sender: str,
        receiver: str,
        subject: str,
        plain_text_message: str,
        html_message: str,
        base_email_client: BaseEmailClient,
    ):
        """Ensure the MIMEMultipart message is compiled correctly

        Args:
            sender (str): sender address of the message
            receiver (str): recipient address of the message
            subject (str): subject line of the message
            plain_text_message (str): message in plain text
            html_message (str): message in html form
            generic_async_client (AsyncEmailClient): provider of a AsyncEmailClient
                to test on
        """
        message = base_email_client.compile_message(
            sender=sender,
            receiver=receiver,
            subject=subject,
            plain_text_message=plain_text_message,
            html_message=html_message,
        )
        parts = message.get_payload()
        plain_text_part = parts[0]
        html_part = parts[1]

        assert isinstance(message, MIMEMultipart)
        assert message["From"] == sender
        assert message["To"] == receiver
        assert message["Subject"] == subject

        assert len(parts) == 2

        assert isinstance(plain_text_part, MIMEText)
        assert plain_text_part.get_content_type() == "text/plain"
        assert isinstance(html_part, MIMEText)
        assert html_part.get_content_type() == "text/html"

    async def test_compile_and_send(
        self, base_email_client: BaseEmailClient, mocker: MockerFixture
    ):
        """Ensure that the compile_and_send method sucessfully
            calls all dependent methods

        Args:
            generic_async_client (AsyncEmailClient): provider of a AsyncEmailClient
                to test on
            mocker (MockerFixture): pytest-mock
        """
        file_mock = mocker.patch(
            "src.infrastructure.email.generic.read_file_async"
        )
        template_mock = mocker.patch.object(base_email_client, "template_html")
        plaintext_mock = mocker.patch.object(base_email_client, "html_to_plain_text")
        compile_mock = mocker.patch.object(base_email_client, "compile_message")
        send_mock = mocker.patch.object(base_email_client, "send")

        await base_email_client.compile_and_send(filepath="", receiver="", subject="")

        file_mock.assert_called_once()
        template_mock.assert_called_once()
        plaintext_mock.assert_called_once()
        compile_mock.assert_called_once()
        send_mock.assert_called_once()
