from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from .models import EmailConfirmationModel, EmailModel, UserModel


class UserRepo(SQLAlchemyAsyncRepository[UserModel]):
    """SQLAlchemy Repository for the UserModel"""

    model_type = UserModel


class EmailRepo(SQLAlchemyAsyncRepository[EmailModel]):
    """SQLAlchemy Repository for the EmailModel"""

    model_type = EmailModel


class EmailConfirmationRepo(SQLAlchemyAsyncRepository[EmailConfirmationModel]):
    """SQLAlchemy Repository for the EmailConfirmationModel"""

    model_type = EmailConfirmationModel
