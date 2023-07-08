from typing import Any, ContextManager, Dict

import pytest
from src.verdantech_api.lib.email.generic import AsyncEmailClient


class TestGenericAsyncClient:
    @pytest.mark.parametrize(
        ["input_html", "expected_output", "kwargs", "error_context"],
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
        indirect=["error_context"],
    )
    def test_template_html(
        self,
        input_html: str,
        expected_output: str,
        kwargs: Dict[str, Any],
        error_context: ContextManager,
        generic_async_client: AsyncEmailClient,
    ):
        """Ensure that output == expected given kwargs

        Args:
            input_html (str): The input after reading file
            expected_output (str): The expected output
            kwargs (Dict[str, Any]): The arguments to be inserted int input
            error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
            generic_async_client (AsyncEmailClient): The client to test on
        """
        with error_context:
            html = generic_async_client.template_html(html_content=input_html, **kwargs)
            assert html == expected_output

    # def test_html_to_plain_test(self, generic_async_client):
    # pass

    # def compile_message(self, generic_async_client):
    # pass
