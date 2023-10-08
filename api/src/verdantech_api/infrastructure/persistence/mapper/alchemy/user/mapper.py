from typing import List, Tuple

from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.values import Email

from ..generic import BaseAlchemyMapper
from .model import EmailAlchemyModel, UserAlchemyModel


class UserAlchemyMapper(BaseAlchemyMapper[User]):
    """Implementation of a model mapper interface using sqlalchemy."""

    entity: User
    model: UserAlchemyModel

    @staticmethod
    def to_model(entity: User) -> UserAlchemyModel:
        """Given a user, map into sqlalchemy model.

        Args:
            entity (User): the user to map

        Returns:
            UserAlchemyModel: the resultant sqlalchemy model
        """

        def to_email_model(
            email: Email, user_model: UserAlchemyModel, list_index: int
        ) -> EmailAlchemyModel:
            email_alchemy_model = EmailAlchemyModel(
                user_id=user_model.id,
                user=user_model,
                list_index=list_index,
                address=email.address,
                verified=email.verified,
                primary=email.primary,
                confirmation=email.confirmation,
                verified_at=email.verified_at,
            )
            return email_alchemy_model

        user_alchemy_model = UserAlchemyModel(
            id=entity.id,
            username=entity.username,
            username_norm=entity.username_norm,
            _password_hash=entity._password_hash,
            is_active=entity.is_active,
            is_superuser=entity.is_superuser,
            password_reset_confirmation=entity.password_reset_confirmation,
            created_at=entity.created_at,
        )
        user_alchemy_model.emails = [
            to_email_model(email, user_alchemy_model, list_index)
            for list_index, email in enumerate(entity.emails)
        ]

        return user_alchemy_model

    @staticmethod
    def from_model(model: UserAlchemyModel) -> User:
        """Given a user sqlalchemy model, map into user

        Args:
            UserAlchemyModel: the sqlalchemy model to map

        Returns:
            User: the resultant user
        """

        def from_email_model(email_model: EmailAlchemyModel) -> Email:
            email = Email(
                address=email_model.address,
                verified=email_model.verified,
                primary=email_model.primary,
                confirmation=email_model.confirmation,
                verified_at=email_model.verified_at,
            )
            return email

        user = User(
            username=model.username,
            username_norm=model.username_norm,
            _password_hash=model._password_hash,
            is_active=model.is_active,
            is_superuser=model.is_superuser,
            password_reset_confirmation=model.password_reset_confirmation,
            created_at=model.created_at,
        )
        user.id = model.id
        user.emails = [
            from_email_model(email_model)
            for email_model in sorted(
                model.emails, key=lambda email_model: email_model.list_index
            )
        ]
        return user
