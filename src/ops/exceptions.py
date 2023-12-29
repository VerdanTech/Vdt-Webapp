class OpsError(Exception):
    """
    Base class for application perations exceptions.
    """

    pass


class EntityNotFound(OpsError):
    """
    Raised when an entity query returns None.
    """

    pass
