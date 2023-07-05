from typing import TYPE_CHECKING, Any

from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy import Select

from verdantech_api.lib.field_validators.errors import ValidationError

if TYPE_CHECKING:
    from litestar.contrib.sqlalchemy.repository import ModelT
    from sqlalchemy.ext.asyncio import AsyncSession
    from verdantech_api.lib.field_validators.generic import FieldValidator

from ..models import UserModel


class UserRepo(SQLAlchemyAsyncRepository[UserModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = UserModel

    username_field_validator: FieldValidator
    password_field_validator: FieldValidator

    def __init__(
        self,
        *,
        statement: Select[tuple[ModelT]] | None = None,
        session: AsyncSession,
        username_field_validator: FieldValidator,
        password_field_validator: FieldValidator,
        **kwargs: Any,
    ) -> None:
        self.username_field_validator = username_field_validator
        self.password_field_validator = password_field_validator
        super().__init__(statement=statement, session=session, **kwargs)

    async def username_sanitize(self, username: str) -> str:
        self.username_field_validator.validate(input=username)
        matched_username = await self.get_one_or_none(username=username)
        if matched_username:
            raise ValidationError("Username already in use")

        return username

    async def password_sanitize(self, password1: str, password2: str) -> None:
        if not password1 == password2:
            raise ValidationError("Passwords do not match")

        self.password_field_validator.validate(password1)
