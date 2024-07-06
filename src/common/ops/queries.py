# Standard Library
from typing import Type, TypeVar, dataclass_transform
import uuid
from datetime import datetime
# External Libraries
import cattrs
from attr import attrib, define, field
from pydantic import BaseModel, ConfigDict

# VerdanTech Source
from src.common.domain.models import DomainModel

cattrs_converter = cattrs.Converter()
cattrs_converter.register_structure_hook(uuid.UUID, lambda v, _: v)
cattrs_converter.register_structure_hook(datetime, lambda v, _: v)

@dataclass_transform(field_specifiers=(attrib, field))
def query_result_transform(cls):
    """
    Attrs settings for API Data Transfer Objects.

    The @dataclass_transform decorator is required for type-checking/dataclass
    functionality. See (https://peps.python.org/pep-0681/).

    This decorator:
    - Applies attrs @define decorator with arguments:
        frozen=True: Immutability is enforced for read-only constructs.
        eq=True: Explicit enabling of __eq__() generation as value
            objects are equivalent if all their attributes are.
        slots=True: Slotted classes are preferred for performance.
    """

    cls = define(frozen=True, eq=True, slots=True)(cls)
    return cls


class Query(BaseModel):
    model_config = ConfigDict(frozen=True)


QueryResultT = TypeVar("QueryResultT")


class QueryResult[T: DomainModel | None]:
    @classmethod
    def cast(cls: Type[QueryResultT], model: T) -> "QueryResultT":
        """
        Convert an instance of a domain model to a query result.

        Args:
            model (T): an instance of a domain model.

        Returns:
            QueryResult[T]: the equivalent query result.
        """

        unstructured_model = cattrs_converter.unstructure(model)
        structured_result = cattrs_converter.structure(unstructured_model, cls)
        return structured_result
