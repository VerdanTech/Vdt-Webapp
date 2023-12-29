# Standard Library
from dataclasses import dataclass

# External Libraries
from litestar.dto.config import DTOConfig
from litestar.dto.dataclass_dto import DataclassDTO

# VerdanTech Source
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum as specs


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


@dataclass
class UserLoginInput:
    email_address: str
    password: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "email_address": self.email_address,
                "password": self.password,
            },
            spec_select={
                "email_address": [
                    specs.LENGTH,
                    specs.EMAIL,
                ],
            },
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.email_address = sanitized_data["email_address"]
