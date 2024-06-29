# Standard Library
import uuid

# External Libraries
from sqlalchemy import MetaData
from sqlalchemy.orm import registry

metadata = MetaData()
mapper_registry = registry()
default_uuid = uuid.uuid4
