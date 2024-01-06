# Standard Library
from typing import Protocol

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.user.entities import Garden

from ..generic import AbstractRepository


class AbstractUserRepository(AbstractRepository[Garden], Protocol):
    """Data persistence interface for the Garden domain model"""

    entity = Garden
