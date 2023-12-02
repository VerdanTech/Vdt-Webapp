# External Libraries
from litestar.dto.config import DTOConfig
from litestar.dto.dataclass_dto import DataclassDTO

# VerdanTech Source
from src.domain.user.entities import User

# class UserRef(DataclassDTO[User]):
# config = DTOConfig(include={"id", "username"})


# class UserDetail(DataclassDTO[User]):
# config = DTOConfig(include={"id", "username", "public_memberships", "created_at"})


class UserSelfDetail(DataclassDTO[User]):
    pass
    config = DTOConfig(
        include={
            "id",
            "username",
            "emails",
            "memberships",
            "created_at",
            "is_superuser",
        },
        max_nested_depth=2,
    )