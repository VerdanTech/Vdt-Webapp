from contextlib import asynccontextmanager

from pymongo import errors as pymongo_errors
from src.interfaces.persistence import exceptions


@asynccontextmanager
async def motor_exception_map():
    """Map motor/pymongo exceptions to native domain equivalents"""
    try:
        yield
    except pymongo_errors.DuplicateKeyError as error:
        raise exceptions.ObjectAlreadyExists(error)
    except (
        pymongo_errors.ConnectionFailure
        or pymongo_errors.ProtocolError
        or pymongo_errors.ConfigurationError
    ) as error:
        raise exceptions.FatalRepoError(error)
    except pymongo_errors.PyMongoError as error:
        raise exceptions.RepositoryError(error)
