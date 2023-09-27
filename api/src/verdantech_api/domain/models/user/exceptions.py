from src.verdantech_api.domain.utils.sanitizers.sanitization.generic import (
    SanitizationError,
)


class PasswordAlreadySetError(Exception):
    """Exception for implicit password overwrite"""

    pass


class EmailAlreadyVerifiedError(SanitizationError):
    """Exception for new email confirmations on verified email"""

    pass


class EmailConfirmationKeyNotFound(SanitizationError):
    """Exception for when an email confirmation key was not found"""

    pass


class PasswordResetConfirmationNotFound(SanitizationError):
    """Exception for when a password_reset was not found"""

    pass


class EmailConfirmationExpired(SanitizationError):
    """Exception for when an email confirmation key is expired"""

    pass


class PasswordResetConfirmationExpired(SanitizationError):
    """Exception for when a password reset is expired"""

    pass


class UserNotFound(SanitizationError):
    """Exception for when a user is searched for but does not exist"""

    pass


class UserNotAuthenticated(Exception):
    """Exception for when an authentication attempt failed"""
