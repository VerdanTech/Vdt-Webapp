# VerdanTech Source
from src.exceptions import ApplicationException, ExceptionResponseEnum


class GardenAuthorizationException(ApplicationException):
    """Raised when an operation is attempted but is unauthorized."""

    response = ExceptionResponseEnum.CLIENT_ERROR


class MembershipAlreadyExists(ApplicationException):
    """
    Raised when an attempt is made to create a GardenMembership
    invite that has already been created.
    """

    pass


class MembershipAlreadyConfirmed(ApplicationException):
    """
    Raised when an attempt is made to accept a GardenMembership
    invite that has already been accepted.
    """

    pass
