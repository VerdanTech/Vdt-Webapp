class ValidationError(ValueError):
    """Base class for handling validation errors"""

    def __str__(self):
        return __name__
