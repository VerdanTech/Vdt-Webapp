from typing import TYPE_CHECKING, List

from litestar.contrib.repository.filters import CollectionFilter, OrderBy
from src.verdantech_api import settings

from ..models.repos import EmailConfirmationRepo, EmailRepo

if TYPE_CHECKING:
    from ..models.models import EmailModel


class EmailService:
    def __init__(
        self, email_repo: EmailRepo, email_confirmation_repo: EmailConfirmationRepo
    ):
        self.email_repo = email_repo
        self.email_confirmation_repo = email_confirmation_repo

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
            user_emails, count = await self.email_repo.list_and_count(
                CollectionFilter(field_name="user_id", values=[user_id]),
                OrderBy(field_name="set_at"),
            )
            if count > settings.USER_MAX_EMAILS:
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
