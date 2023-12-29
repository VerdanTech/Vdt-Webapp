# Standard Library
from dataclasses import dataclass

# External Libraries
from dns.resolver import Resolver
from email_validator import validate_email
from email_validator.exceptions_types import EmailNotValidError

from ..options import SelectEnum
from ..spec import Spec, SpecConfig, SpecError, SpecParams


class EmailSpecParams(SpecParams):
    check_deliverability: bool
    test_environment: bool
    allow_smtputf8: bool


@dataclass(kw_only=True)
class EmailSpecConfig(SpecConfig[EmailSpecParams]):
    dns_resolver: Resolver


class EmailSpecError(SpecError):
    pass


class EmailSpec[EmailSpecConfig](Spec):
    """
    Use of the third-party email_validator library for
    validation and normalization.
    """

    id = SelectEnum.EMAIL
    name = "Email"
    error = EmailSpecError

    def _sanitize(self, input_data: str) -> bool:
        """
        Use the email_validator library's validate_email
        function to validate and normalize an email.
        Set the error message of the third party exception
        on the Spec, the normalized_data on the FieldSanitizer,
        and return a boolean.

        Args:
            input_data (str): input email address to sanitize.

        Returns:
            bool: validation result.
        """
        try:
            validated_email = validate_email(
                input_data,
                check_deliverability=self.config.params["check_deliverability"],
                test_environment=self.config.params["test_environment"],
                allow_smtputf8=self.config.params["allow_smtputf8"],
            )
            if self.field_sanitizer is not None:
                self.field_sanitizer.normalized_data = validated_email.normalized
        except EmailNotValidError as exc:
            self.config.error_message = str(exc)
            return False
        return True
