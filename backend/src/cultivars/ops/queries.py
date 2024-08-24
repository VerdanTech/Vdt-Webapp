# Standard Library
import uuid
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src import exceptions, settings
from src.common.domain import Ref
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.queries import Query, QueryResult, query_result_transform
from src.cultivars.domain import Cultivar, CultivarCollection
from src.garden.domain.commands import GardenKey

# ======================================
# QueryResults
# ======================================


@query_result_transform
class CultivarGetByGardenResult(QueryResult[None]):
    collections: set[Ref[CultivarCollection]]
    active_collection: Ref[CultivarCollection]


# ======================================
# Queries
# ======================================

class CultivarGetByGarden(Query):
    garden_key: GardenKey



# ======================================
# Query handlers
# ======================================


