class DomainException(Exception):
    """
    Base class for Domain layer exceptions.
    """

    pass


class FieldNotFound(DomainException):
    """
    Raised when a field is provided as an input
    to a function but does not exist on the object.
    """

    pass


class EntityIntegrityException(DomainException):
    """
    Raised when an Entity fails an assertion of integrity,
    such as the assert_persisted() method.
    """

    pass
