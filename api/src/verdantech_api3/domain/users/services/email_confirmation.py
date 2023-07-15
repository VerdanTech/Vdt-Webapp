from typing import TYPE_CHECKING, List

from ..models.models import EmailConfirmationModel, EmailModel
from ..models.repos import EmailConfirmationRepo, EmailRepo


class EmailConfirmationService:
    def __init__(
        self, email_repo: EmailRepo, email_confirmation_repo: EmailConfirmationRepo
    ):
        self.email_repo = email_repo
        self.email_confirmation_repo = email_confirmation_repo

    async def create_email_confirmation(self, key: str, email: EmailModel):
        # Create database object
        email_confirmation = EmailConfirmationModel(key=key)
        email.confirmations = {email_confirmation}

        await self.email_repo.update(email)
        await self.email_confirmation_repo.add(email_confirmation)

        return email, email_confirmation

    async def remove_active_confirmations(
        self,
    ):
        pass
