# VerdanTech Source
from src.exceptions import ApplicationException, ExceptionResponseEnum


class EntityNotFound(ApplicationException):
    """
    Raised when an entity query returns None.
    """

    response = ExceptionResponseEnum.CLIENT_ERROR


class IncorrectPassword(ApplicationException):
    """
    Raised when a password is provided that is incorrect.
    """

    response = ExceptionResponseEnum.CLIENT_ERROR
