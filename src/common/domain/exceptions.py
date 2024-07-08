# VerdanTech Source
from src.exceptions import ApplicationException, ExceptionResponseEnum


class FieldNotFound(ApplicationException):
    """
    Raised when a field is provided as an input
    to a function but does not exist on the object.
    """

    response = ExceptionResponseEnum.CLIENT_ERROR


class EntityIntegrityException(ApplicationException):
    """
    Raised when an Entity fails an assertion of integrity,
    such as the assert_persisted() method.
    """

    response = ExceptionResponseEnum.SERVER_ERROR
