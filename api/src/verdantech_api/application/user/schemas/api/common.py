from dataclasses import dataclass

from litestar.dto.factory import DTOConfig
from litestar.dto.factory.stdlib.dataclass import DataclassDTO
from src.verdantech_api.domain.models.user.entities import User


@dataclass
class UserRef(DataclassDTO[User]):
    config = DTOConfig(include={"_id", "username"})


@dataclass
class UserDetail(DataclassDTO[User]):
    config = DTOConfig(include={"_id", "username", "public_memberships", "created_at"})


@dataclass
class UserSelfDetail(DataclassDTO[User]):
    config = DTOConfig(
        include={
            "_id",
            "username",
            "emails",
            "memberships",
            "created_at",
            "is_superuser",
        }
    )
