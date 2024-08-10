# Standard Library
import uuid

# External Libraries
from sqlalchemy.orm import registry

mapper_registry = registry()
default_uuid = uuid.uuid4
