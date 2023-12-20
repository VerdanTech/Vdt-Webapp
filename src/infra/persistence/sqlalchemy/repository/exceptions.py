# Standard Library
from contextlib import contextmanager

# External Libraries
import sqlalchemy.exc as alchemy_exceptions

# VerdanTech Source
from src.interfaces.persistence import exceptions


@contextmanager
def alchemy_exception_map():
    """Map sqlalchemy exceptions to native domain equivalents"""
    try:
        yield
    except alchemy_exceptions.IntegrityError as error:
        raise exceptions.RepositoryError from error
    except alchemy_exceptions.SQLAlchemyError as error:
        raise exceptions.RepositoryError from error
