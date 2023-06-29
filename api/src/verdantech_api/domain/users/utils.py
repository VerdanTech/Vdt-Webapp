from email_validator import EmailNotValidError, validate_email
from litestar.exceptions import ValidationException


def validate_and_normalize_email(self, email: str) -> str:
    """Validate and normalize email address using email-validator

    Args:
        email (str): the email to operate on

    Raises:
        ValidationException: raised if email validation fails

    Returns:
        str: the normalized email address
    """

    try:
        validated_email = validate_email(email, check_deliverability=False)
        email = validated_email.normalized
    except EmailNotValidError as exc:
        raise ValidationException(detail=f"{exc}")

    return email


def validate_and_normalize_username(username: str) -> str:
    pass
