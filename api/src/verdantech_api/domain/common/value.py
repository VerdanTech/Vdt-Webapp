from dataclasses import dataclass
from bson.objectid import ObjectId

@dataclass(frozen=True)
class Value:
    """Base value object for all domain value objects
    """
    _id: str