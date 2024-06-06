# VerdanTech Source
from src.exceptions import ApplicationException, ExceptionResponseEnum


class PasswordAlreadySetError(ApplicationException):
    """Exception for implicit password overwrite."""

    response = ExceptionResponseEnum.SERVER_ERROR


class EmailAlreadyVerifiedError(ApplicationException):
    """Exception for new email confirmations on verified email"""

    response = ExceptionResponseEnum.CLIENT_ERROR


class EmailConfirmationExpired(ApplicationException):
    """Exception for when an email confirmation key is expired"""

    response = ExceptionResponseEnum.CLIENT_ERROR


class UserNotAuthenticated(ApplicationException):
    """Exception for when an authentication attempt failed"""

    response = ExceptionResponseEnum.CLIENT_ERROR
