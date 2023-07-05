from typing import TYPE_CHECKING, Any, List

from litestar.contrib.repository.filters import CollectionFilter, OrderBy
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy import Select

from verdantech_api.lib.field_validators.errors import ValidationError
from verdantech_api.settings import USER_MAX_EMAILS

if TYPE_CHECKING:
    from litestar.contrib.sqlalchemy.repository import ModelT
    from sqlalchemy.ext.asyncio import AsyncSession
    from verdantech_api.lib.field_validators.generic import FieldValidator

from ..models import EmailModel


class EmailRepo(SQLAlchemyAsyncRepository[EmailModel]):
    """SQLAlchemy Repository for the EmailModel"""

    model_type = EmailModel

    email_field_validator: FieldValidator

    def __init__(
        self,
        *,
        statement: Select[tuple[ModelT]] | None = None,
        session: AsyncSession,
        email_field_validator: FieldValidator,
        **kwargs: Any,
    ) -> None:
        self.email_field_validator = email_field_validator
        super().__init__(statement=statement, session=session, **kwargs)

    async def email_sanitize(self, email: str) -> str:
        self.email_field_validator.validate(input=email)
        email = self.email_field_validator.normalize(input=email)
        matched_email = await self.get_one_or_none(email=email)
        if matched_email:
            raise ValidationError("Email address already in use")

        return email

    async def remove_oldest_email(self, user_id: int) -> List[EmailModel]:
        """Remove the user's email with the least magnitude
        of the set_at attribute

        Args:
            user_id (int): ID of the user

        Returns:
            List[EmailModel]: the full list of user's emails
                after the operation
        """
        # Get list of user's emails and remove the one with the oldest primary_at
        user_emails, count = await self.list_and_count(
            CollectionFilter(field_name="user_id", values=[user_id]),
            OrderBy(field_name="set_at"),
        )
        if count > USER_MAX_EMAILS:
            oldest_email = user_emails.pop[0]
            await self.email_confirmation_repo.remove(oldest_email)

        return user_emails

    async def set_new_primary_email(
        self, new_primary_email: EmailModel, user_emails: List[EmailModel]
    ) -> None:
        """Set exclusive primary status to new email

        Args:
            new_primary_email (EmailModel): the email to set as primary.
                Must be contained in user_emails, and be verified
            user_emails (List[EmailModel]): list of user's emails

        Raises:
            Exception: _description_
        """
        if not new_primary_email.is_verified:
            raise Exception  # todo

        if new_primary_email not in user_emails:
            raise Exception  # todo

        # Remove primary status for all emails except new one
        for email in user_emails:
            if email.id == new_primary_email.id:
                email.set_primary_status()
            else:
                email.remove_primary_status()

        await self.update_many(user_emails)
