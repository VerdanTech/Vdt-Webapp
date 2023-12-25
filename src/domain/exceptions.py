

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