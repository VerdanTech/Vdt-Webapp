class ValidationError(Exception):
    """Base class for handling validation errors"""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class MinSizeValidationError(ValidationError):
    pass


class MaxSizeValidationError(ValidationError):
    pass


class MinLengthValidationError(ValidationError):
    pass


class MaxLengthValidationError(ValidationError):
    pass


class RegexValidationError(ValidationError):
    pass


class BannedInputValidationError(ValidationError):
    pass
