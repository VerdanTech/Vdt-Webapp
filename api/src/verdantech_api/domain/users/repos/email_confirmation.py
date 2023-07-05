from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from ..models import EmailConfirmationModel


class EmailConfirmationRepo(SQLAlchemyAsyncRepository[EmailConfirmationModel]):
    """SQLAlchemy Repository for the EmailConfirmationModel"""

    model_type = EmailConfirmationModel

    async def clean_expired(self):
        pass
