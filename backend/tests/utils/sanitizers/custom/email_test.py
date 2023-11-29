# External Libraries
import pytest
from dns.resolver import Resolver
from email_validator.exceptions_types import EmailNotValidError, ValidatedEmail
from pytest_mock import MockerFixture

# VerdanTech Source
from src.utils.sanitizers.custom.email import (
    EmailSpec,
    EmailSpecConfig,
    EmailSpecParams,
)
from src.utils.sanitizers.field import FieldSanitizer

pytestmark = [pytest.mark.unit]


class TestEmailSpec:
    # ======================================
    # EmailSpec._sanitize() tests
    # ======================================

    def test_email_spec_true_validation(self, mocker: MockerFixture):
        """
        Ensure that the email sanitization logic calls email_validator
        with the configured parameters and config, returns True
        when validation is successful, and updates the normalized_data
        attribute on the FieldSanitizer.

        Args:
            mocker (MockerFixture): pytest-mock
        """
        # Set SpecParams
        check_deliverability = True
        test_environment = True
        allow_smtputf8 = True
        params = EmailSpecParams(
            check_deliverability=check_deliverability,
            test_environment=test_environment,
            allow_smtputf8=allow_smtputf8,
        )

        # Set SpecConfig
        mock_dns_resolver = mocker.Mock(spec=Resolver)
        config = EmailSpecConfig(
            params=params, error_message="", dns_resolver=mock_dns_resolver
        )
        spec = EmailSpec(config=config)

        # As the EmailSpec modifies the normalized_data attribute on its FieldSanitizer,
        # mock a FieldSanitizer on the EmailSpec
        mock_field_sanitizer = mocker.Mock(spec=FieldSanitizer)
        spec.field = mock_field_sanitizer

        # Mock email_validator library
        normalized_email_address = "normalized_email"
        mock_validated_email = ValidatedEmail(normalized=normalized_email_address)
        mock_validate_email = mocker.patch(
            "src.utils.sanitizers.custom.email.validate_email",
            return_value=mock_validated_email,
        )

        input_data = "input_data"

        return_value = spec._sanitize(input_data=input_data)

        assert mock_field_sanitizer.normalized_data == normalized_email_address
        mock_validate_email.assert_called_once_with(
            input_data,
            check_deliverability=check_deliverability,
            test_environment=test_environment,
            allow_smtputf8=allow_smtputf8,
        )
        assert return_value == True

    def test_email_spec_false_validation(self, mocker: MockerFixture):
        """
        Ensure that the email sanitization logic calls email_validator
        and returns False when the validate_email function rasies an error,
        and sets the error message on self.config.error_message

        Args:
            mocker (MockerFixture): pytest-mock
        """
        # Set SpecParams
        params = EmailSpecParams(
            check_deliverability=True,
            test_environment=True,
            allow_smtputf8=True,
        )

        # Set SpecConfig
        mock_dns_resolver = mocker.Mock(spec=Resolver)
        config = EmailSpecConfig(
            params=params, error_message="", dns_resolver=mock_dns_resolver
        )
        spec = EmailSpec(config=config)

        # As the EmailSpec modifies the normalized_data attribute on its FieldSanitizer,
        # mock a FieldSanitizer on the EmailSpec
        mock_field_sanitizer = mocker.Mock(spec=FieldSanitizer)
        spec.field = mock_field_sanitizer

        # Mock email_validator library
        mock_error_message = "Error message from email_validator"
        mocker.patch(
            "src.utils.sanitizers.custom.email.validate_email",
            side_effect=EmailNotValidError(mock_error_message),
        )

        return_value = spec._sanitize(input_data="input_data")

        assert return_value == False
        assert spec.config.error_message == str(mock_error_message)
