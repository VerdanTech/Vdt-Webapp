from typing import ContextManager

import pytest
from email_validator.exceptions_types import EmailNotValidError, ValidatedEmail
from pytest_mock import MockerFixture
from src.ops.user.services.sanitization.email import EmailSanitization
from src.utils.sanitizers.field import FieldSanitizer
from src.utils.sanitizers.sanitization.custom.email import EmailSanitizationError

pytestmark = [pytest.mark.unit]


class TestEmailSanitization:
    @pytest.mark.skip
    @pytest.mark.parametrize(
        ["error_raised", "error_message", "expected_error_context"],
        [
            # Test case: no validation exception is raised by validate_email,
            # no EmailSanitization is raised
            (None, "", None),
            # Test case: validation exception is raised by validate_email,
            # EmailSanitization is raised
            (
                EmailNotValidError("error_message"),
                "error_message",
                EmailSanitizationError,
            ),
        ],
        indirect=["expected_error_context"],
    )
    def test_base_sanitization(
        self,
        error_raised: EmailNotValidError | None,
        error_message: str,
        expected_error_context: ContextManager,
        mocker: MockerFixture,
    ) -> None:
        """Ensure that the base sanitization calls the validate_email
        function and raises the appropriate sanitization exception

        Args:
            error_raised (_type_): the error to mock raised by validate_email
            error_message (_type_): the error message to mock raised by validate_email
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            mocker (_type_): pytest-mock
        """
        validated_email = ValidatedEmail()
        validated_email.normalized = "normalized_email"
        mock_validate_email = mocker.patch(
            "src.ops.user.services.sanitization.fields.email.validate_email",
            return_value=validated_email,
            side_effect=error_raised,
        )
        sanitization = EmailSanitization()
        FieldSanitizer(sanitization)

        with expected_error_context as error:
            sanitization.base_sanitization(input=0)
            assert sanitization.field.normalized == "normalized_email"
            mock_validate_email.assert_called_once_with(0, check_deliverability=False)
            if error is not None:
                assert error.message == error_message
