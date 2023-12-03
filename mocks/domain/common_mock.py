from typing import List

from src.domain.common import root_entity


@root_entity
class MockRootEntity:
    string_field: str
    float_field: float
    list_of_bools_field: List[bool]
