# Standard Library
from typing import Literal

# Types passed into exceptions when used

# Errors shown to the user under form fields. Each error is a tuple of the field name and the error message.
type FieldErrors = list[tuple[str, str]]
# Errors shown to the user under a form.
type NonFieldErrors = list[str]
# Errors shown to the user in a seperate context, e.g. a toast.
type NonFormErrors = list[str]

# Types of the extra field in the exception
# Contains field, non_field, and non_form errors
type DetailedExtraType = list[dict[Literal["key", "message"], str]]


def errors_to_extra(
    message: str,
    field_errors: FieldErrors = [],
    non_field_errors: NonFieldErrors = [],
    non_form_errors: NonFormErrors = [],
) -> DetailedExtraType:
    """
    Converts the different types of errors into the single extra field format.

    Args:
        message (str): The non user-friendly message set on the exception.
            Used as a non_form_error when no other errors are present.
        field_errors (FieldErrors, optional): Errors related to form fields. Defaults to [].
        non_field_errors (NonFieldErrors, optional): Errors related to forms. Defaults to [].
        non_form_errors (NonFormErrors, optional): Errors related to non-forms. Defaults to [].

    Returns:
        DetailedExtraType: The errors in the extra field format.
    """
    print(field_errors)
    extra = []
    if field_errors:
        extra.extend(
            [{"key": key, "message": message} for key, message in field_errors]
        )
    if non_field_errors:
        extra.extend(
            [
                {"key": "non_field_error", "message": message}
                for message in non_field_errors
            ]
        )
    if non_field_errors:
        extra.extend(
            [
                {"key": "non_form_error", "message": message}
                for message in non_form_errors
            ]
        )
    if not field_errors and not non_field_errors and not non_form_errors:
        extra.extend([{"key": "non_form_error", "message": message}])
    return extra


class ApplicationException(Exception):
    """
    Base class for all application exceptions.

    Attributes:
        status_code (int): The HTTP status code represented.
        default_message (str): The default message to set on the exception. Not user-friendly.
        message: (str): The message set on the exception:
        extra: (DetailedExtraType): The user-friendly error messages to send to the client.
    """

    status_code: int = 500
    default_message: str = "A failure has occurred"
    extra: DetailedExtraType

    def __init__(
        self,
        message: str = "",
        field_errors: FieldErrors = [],
        non_field_errors: NonFieldErrors = [],
        non_form_errors: NonFormErrors = [],
    ) -> None:
        message = message or self.default_message
        super().__init__(message)
        self.extra = errors_to_extra(
            self.default_message, field_errors, non_field_errors, non_form_errors
        )


class ValidationError(ApplicationException):
    status_code = 400
    default_message = "Request parameters failed to validate"


class AuthenticationError(ApplicationException):
    status_code = 401
    default_message = "Authentication failed"


class AuthorizationError(ApplicationException):
    status_code = 403
    default_message = "Permission denied"


class NotFoundError(ApplicationException):
    status_code = 404
    default_message = "This resource does not exist"


class ServerError(ApplicationException):
    status_code = 500
    default_message = "Something unexpected happened on the server"


class ServiceUnavailableError(ApplicationException):
    status_code = 503
    default_message = "This service is not yet functional"


# Attach logging to this one
class DomainIntegrityException(ServerError):
    """
    Indicates a failure in the application logic.
    """

    pass
