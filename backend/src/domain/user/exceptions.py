class UserError(Exception):
    pass


class PasswordAlreadySetError(UserError):
    """Exception for implicit password overwrite"""

    pass


class EmailAlreadyVerifiedError(UserError):
    """Exception for new email confirmations on verified email"""

    pass


class EmailConfirmationKeyNotFound(UserError):
    """Exception for when an email confirmation key was not found"""

    pass


class PasswordResetConfirmationNotFound(UserError):
    """Exception for when a password_reset was not found"""

    pass


class EmailConfirmationExpired(UserError):
    """Exception for when an email confirmation key is expired"""

    pass


class PasswordResetConfirmationNotValid(UserError):
    """Exception for when a password reset is not valid"""

    pass


class UserNotFound(UserError):
    """Exception for when a user is searched for but does not exist"""

    pass


class EmailNotFound(UserError):
    """Exception for when a user is supposed to operate on an email address that does not exist."""

    pass


class UserNotAuthenticated(UserError):
    """Exception for when an authentication attempt failed"""

    pass


class UserIntegrityError(UserError):
    """Exception for when a user object exists in a state it isn't allowed to be in"""

    pass
