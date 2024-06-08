class RepositoryError(Exception):
    """Base repositry exception class"""

    pass


class RoutineRepositoryError(RepositoryError):
    """Raised when a repository raises an exception that is normal
    during operation of the database: for example, not finding
    an entity which does not exist.
    """

    pass


class FatalRepositoryError(RepositoryError):
    """Raised when a repository raises an exception that idicates
    a failure to interface with the database: for example,
    database connection lost.
    """

    pass


class InterfaceRepositoryError(RepositoryError):
    """Raised when an interface has failed to validate
    the repository alongside its requirements."""

    pass


class ObjectNotFound(RoutineRepositoryError):
    """Raised when an object fails to be found in a repository"""

    pass


class ObjectAlreadyExists(FatalRepositoryError):
    """Raised when an object already exists in a repository"""

    pass
