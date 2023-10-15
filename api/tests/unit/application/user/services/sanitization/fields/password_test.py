from typing import ContextManager

import pytest
from src.verdantech_api.application.user.services.sanitization.fields.password import (
    PasswordMismatchError,
    validate_password_match,
)


@pytest.mark.parametrize(
    ["password1", "password2", "expected_error_context"],
    (
        # Test case: passwords match, no error raised
        ["abc", "abc", None],
        # Test case: passwords don't match, error is raisd
        ["abc", "123", PasswordMismatchError],
    ),
    indirect=["expected_error_context"],
)
def test_validate_password_match(
    password1: str, password2: str, expected_error_context: ContextManager
) -> None:
    """Ensure the password match validation correctly raises the exception

    Args:
        password1 (str): password1 input
        password2 (str): password2 input
        expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
    """
    with expected_error_context:
        validate_password_match(password1=password1, password2=password2)
