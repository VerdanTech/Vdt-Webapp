# VerdanTech Source
from src.domain.exceptions import DomainException


class GardenAuthorizationException(DomainException):
    """Raised when an operation is attempted but is unauthorized."""

    pass


class MembershipAlreadyExists(DomainException):
    """
    Raised when an attempt is made to create a GardenMembership
    invite that has already been created.
    """

    pass


class MembershipAlreadyConfirmed(DomainException):
    """
    Raised when an attempt is made to accept a GardenMembership
    invite that has already been accepted.
    """

    pass
