from email_validator import validate_email
from email_validator.exceptions_types import EmailNotValidError

from ..generic.errors import ValidationError
from ..generic.validators import StringFieldValidator


class EmailValidator(StringFieldValidator):
    field_name: str = "Email"
    normalized: str

    def validate(self, input: str) -> bool:
        # Group exceptions
        error = self._validate(input=input)

        # Custom validation logic
        try:
            validated_email = validate_email(input, check_deliverability=False)
            self.normalized = validated_email.normalized
        except EmailNotValidError as exc:
            error["EmailValidator"] = str(exc)

        # Raise errors
        if error:
            raise ValidationError(error)
        return True

    def normalize(self, input: str) -> str:
        """Convert input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """

        if self.normalized:
            return self.normalized
        else:
            self.normalized = validate_email(
                input, check_deliverability=False
            ).normalized
            return self.normalized
