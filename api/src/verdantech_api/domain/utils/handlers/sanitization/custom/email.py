from ..generic import Sanitization, SanitizationConfig, SanitizationError


class EmailSanitizationConfig(SanitizationConfig):
    pass


class EmailSanitizationError(SanitizationError):
    pass


class EmailSanitization(Sanitization):
    """Placeholder for email sanitization functionality
    to be implemented in the application layer
    """

    name = "Email"
    error: Exception = EmailSanitizationError

    async def _base_sanitization(self, input: str) -> bool:
        raise NotImplementedError
