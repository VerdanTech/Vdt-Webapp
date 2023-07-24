class PasswordAlreadySetException(Exception):
    """Exception for implicit password overwrite"""
    pass

class EmailAlreadyVerifiedException(Exception):
    """Exception for new email confirmations on verified email"""
    pass