# Standard Library
from enum import Enum, auto
from typing import Optional


class ExceptionResponseEnum(Enum):
    """
    Used to track what response type an exception should trigger.
    """

    CLIENT_ERROR = auto()
    SERVER_ERROR = auto()


class ApplicationException(Exception):
    """Base class for all application exceptions."""

    response: ExceptionResponseEnum = ExceptionResponseEnum.SERVER_ERROR

    def __init__(
        self,
        message: str,
        response: Optional[ExceptionResponseEnum] = None,
    ) -> None:
        if response:
            self.response = response
        super().__init__(message)
