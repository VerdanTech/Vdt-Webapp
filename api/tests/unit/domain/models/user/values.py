from dataclasses import replace
from typing import ContextManager

import pytest
from src.verdantech_api.domain.models.user.exceptions import EmailAlreadyVerifiedError
from src.verdantech_api.domain.models.user.values import Email


class TestEmail:
    @pytest.mark.parametrize(
        ("already_verified", "key", "expected_error_context"),
        [(False, "abc", None), (True, "abc", EmailAlreadyVerifiedError)],
        indirect=["expected_error_context"],
    )
    def test_new_confirmation(
        self,
        already_verified: bool,
        key: str,
        expected_error_context: ContextManager,
        email: Email,
    ) -> None:
        """Ensure an error is thrown if the email
        is already verified

        Args:
            already_verified (bool): whether the email is verified
            key (str): the key to create confirmation with
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            email (Email): email object to test on (pytest fixture)
        """
        if already_verified:
            email = replace(email, verified=True)

        with expected_error_context as error:
            email = email.new_confirmation(key=key)
            if error is None:
                assert email.confirmation.key == key
