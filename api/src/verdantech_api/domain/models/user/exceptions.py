class PasswordAlreadySetError(Exception):
    """Exception for implicit password overwrite"""

    pass


class EmailAlreadyVerifiedError(Exception):
    """Exception for new email confirmations on verified email"""

    pass
