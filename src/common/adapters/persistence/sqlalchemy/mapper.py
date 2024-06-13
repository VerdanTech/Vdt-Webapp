# Standard Library
import uuid

# External Libraries
from sqlalchemy import MetaData

metadata = MetaData()

default_uuid = uuid.uuid4
