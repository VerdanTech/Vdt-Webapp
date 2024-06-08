# Standard Library
import uuid

# External Libraries
from pydantic import BaseModel, ConfigDict

type EntityIdType = uuid.UUID


class Command(BaseModel):
    """
    Represents a job the system may perform.

    Pydantic is used for a feature complete validation system
    for incoming inputs.
    """

    model_config = ConfigDict(frozen=True)
