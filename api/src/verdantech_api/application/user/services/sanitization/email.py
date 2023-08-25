from email_validator import validate_email
from email_validator.exceptions_types import EmailNotValidError
from src.verdantech_api.domain.utils.sanitizers.sanitization.custom.email import (
    EmailSanitization,
)


class EmailSanitization(EmailSanitization):
    """Third party library email validation and normalization"""

    def base_sanitization(self, input: str) -> None:
        """Validate email with email_validator library

        Args:
            input (Any): Input to validate

        Raises:
            self.error(): If sanitization fails
        """

        # Custom validation logic
        try:
            validated_email = validate_email(input, check_deliverability=False)
            self.field.normalized = validated_email.normalized
        except EmailNotValidError as exc:
            raise self.error(str(exc))