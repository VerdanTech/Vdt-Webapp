# External Libraries
from litestar.dto.config import DTOConfig
from litestar.dto.dataclass_dto import DataclassDTO

# VerdanTech Source
from src.domain.user.entities import User


class UserSelfDetail(DataclassDTO[User]):
    config = DTOConfig(
        include={
            "id",
            "username",
            "emails",
            "created_at",
            "is_superuser",
        },
        max_nested_depth=2,
    )
