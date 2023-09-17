from typing import ContextManager, Dict

import pytest
from litestar.exceptions import ValidationException
from pytest_mock import MockerFixture
from src.verdantech_api.domain.users.services.validation import (
    UserFieldsSanitizerService,
)
from src.verdantech_api.lib.validators.generic.errors import ValidationError


class TestUserFieldsSanitizerService:
    @pytest.mark.parametrize(
        [
            "username_error",
            "email_error",
            "password_error",
            "expected_error_message",
            "error_context",
        ],
        [
            # Test case: no errors are raised,
            # and no exception is raised
            (None, None, None, None, None),
            # Test case: all errors are raised, and a
            # single exception is raised containing all
            # messages
            (
                ValidationError(message="username_error"),
                ValidationError(message="email_error"),
                ValidationError(message="password_error"),
                {
                    "username": "username_error",
                    "email": "email_error",
                    "password1": "password_error",
                    "password2": "password_error",
                },
                ValidationException,
            ),
        ],
        indirect=["error_context"],
    )
    async def test_sanitize_fields(
        self,
        username_error: Exception,
        email_error: Exception,
        password_error: Exception,
        expected_error_message: Dict[str, str],
        user_fields_sanitizer_service: UserFieldsSanitizerService,
        error_context: ContextManager,
        mocker: MockerFixture,
    ):
        """Ensure the function calls all child validation functions,
        and constructs the correct error message

        Args:
            username_error (Exception): mock username error
            email_error (Exception): mock email error
            password_error (Exception): mock password error
            expected_error_message (Dict[str, str]): the expected
                resultant error messate
            user_fields_sanitizer_service (UserFieldsSanitizerService):
            the service to test on
            error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
            mocker (MockerFixture): pytest-mock mocker
        """

        username = "username"
        email = "email"
        password1 = "password"
        password2 = "password"

        username_sanitize_mock = mocker.patch.object(
            user_fields_sanitizer_service,
            "username_sanitize",
            return_value=username,
            side_effect=username_error,
        )
        email_sanitize_mock = mocker.patch.object(
            user_fields_sanitizer_service,
            "email_sanitize",
            return_value=email,
            side_effect=email_error,
        )
        password_sanitize_mock = mocker.patch.object(
            user_fields_sanitizer_service,
            "password_sanitize",
            return_value=password1,
            side_effect=password_error,
        )

        with error_context as error:
            (
                sanitized_username,
                sanitized_email,
                sanitized_password,
            ) = await user_fields_sanitizer_service.sanitize_fields(
                username=username, email=email, password1=password1, password2=password2
            )

            username_sanitize_mock.assert_awaited_once_with(username=username)
            email_sanitize_mock.assert_awaited_once_with(email=email)
            password_sanitize_mock.assert_awaited_once_with(
                password1=password1, password2=password2
            )

            if error is None:
                assert sanitized_username == username
                assert sanitized_email == email
                assert sanitized_password == password1
            else:
                assert error.detail == "Field validation failed"
                assert error.extra == expected_error_message

    @pytest.mark.parametrize(
        ["username", "username_exists", "error_context"],
        [("test_username", False, None), ("test_username", True, ValidationError)],
        indirect=["error_context"],
    )
    async def test_username_sanitize(
        self,
        username: str,
        username_exists: bool,
        user_fields_sanitizer_service: UserFieldsSanitizerService,
        error_context: ContextManager,
    ):
        """Ensure that database-related validation logic works,
            and that the appropriate Validator function is called

        Args:
            username (str): username to test on
            username_exists (bool): result of username uniqueness query
            user_fields_sanitizer_service (UserFieldsSanitizerService): the service
                to test on
            error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
        """
        user_fields_sanitizer_service.user_repo.exists.return_value = username_exists

        with error_context as error:
            sanitized_username = await user_fields_sanitizer_service.username_sanitize(
                username=username
            )

            if error is None:
                user_fields_sanitizer_service.username_validator.validate.assert_called_once_with(
                    input=username
                )
                assert sanitized_username == username

    @pytest.mark.parametrize(
        ["email", "email_exists", "error_context"],
        [
            ("test_email@gmail.com", False, None),
            ("test_email@gmail.com", True, ValidationError),
        ],
        indirect=["error_context"],
    )
    async def test_email_sanitize(
        self,
        email: str,
        email_exists: bool,
        user_fields_sanitizer_service: UserFieldsSanitizerService,
        error_context: ContextManager,
    ):
        """Ensure that database-related validation logic works,
            and that the appropriate Validator function is called

        Args:
            email (str): email to test on
            email_exists (bool): result of email uniqueness query
            user_fields_sanitizer_service (UserFieldsSanitizerService): the service
                to test on
            error_context (ContextManager): error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
        """
        user_fields_sanitizer_service.email_repo.exists.return_value = email_exists

        with error_context as error:
            sanitized_email = await user_fields_sanitizer_service.email_sanitize(
                email=email
            )

            if error is None:
                user_fields_sanitizer_service.email_validator.validate.assert_called_once_with(
                    input=email
                )

    @pytest.mark.parametrize(
        ["password1", "password2", "error_context"],
        [
            ("test_password", "test_password", None),
            ("test_password", "testpassword", ValidationError),
        ],
        indirect=["error_context"],
    )
    async def test_password_sanitize(
        self,
        password1: str,
        password2: str,
        user_fields_sanitizer_service: UserFieldsSanitizerService,
        error_context: ContextManager,
    ):
        """Ensure that password equality validation logic works,
            and that the appropriate Validator function is called

        Args:
            password1 (str): password1 to test on
            password2 (str): password2 to test on
            user_fields_sanitizer_service (UserFieldsSanitizerService): the service
                to test on
            error_context (ContextManager): error_context (ContextManager): An instance of nullcontext() if
                error_context = None and pytest.raises(error_context) otherwise
                See: tests/conftest.py
        """

        with error_context as error:
            sanitized_password = await user_fields_sanitizer_service.password_sanitize(
                password1=password1, password2=password2
            )

            if error is None:
                user_fields_sanitizer_service.password_validator.validate.assert_called_once_with(
                    input=password1
                )
                assert sanitized_password == password1
