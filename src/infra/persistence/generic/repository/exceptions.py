class ClientLifecycleError(Exception):
    """Raised when a client object should exist in the app state but doesn't"""

    pass
