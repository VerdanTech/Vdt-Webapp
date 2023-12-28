# Standard Library
from typing import List, Tuple

# VerdanTech Source
from src.domain.user.entities import User
from src.domain.user.values import Email, EmailConfirmation, PasswordResetConfirmation

from ..generic import BaseAlchemyMapper
from .model import EmailAlchemyModel, UserAlchemyModel


class UserAlchemyMapper(BaseAlchemyMapper[User, UserAlchemyModel]):
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
            confirmation_key = getattr(email.confirmation, "key", None)
            confirmation_created_at = getattr(email.confirmation, "created_at", None)

            email_alchemy_model = EmailAlchemyModel(
                user_id=user_model.id,
                user=user_model,
                list_index=list_index,
                address=email.address,
                verified=email.verified,
                primary=email.primary,
                confirmation_key=confirmation_key,
                confirmation_created_at=confirmation_created_at,
                verified_at=email.verified_at,
            )
            return email_alchemy_model

        password_reset_confirmation_key = getattr(
            entity.password_reset_confirmation, "key", None
        )
        password_reset_confirmation_created_at = getattr(
            entity.password_reset_confirmation, "created_at", None
        )

        user_alchemy_model = UserAlchemyModel(
            id=entity.id,
            username=entity.username,
            _password_hash=entity._password_hash,
            is_active=entity.is_active,
            is_superuser=entity.is_superuser,
            password_reset_confirmation_key=password_reset_confirmation_key,
            password_reset_confirmation_created_at=password_reset_confirmation_created_at,
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
            confirmation_key = getattr(email_model, "confirmation_key", None)
            confirmation_created_at = getattr(
                email_model, "confirmation_created_at", None
            )
            confirmation = (
                EmailConfirmation(
                    key=confirmation_key, created_at=confirmation_created_at
                )
                if confirmation_key and confirmation_created_at
                else None
            )

            email = Email(
                address=email_model.address,
                verified=email_model.verified,
                primary=email_model.primary,
                confirmation=confirmation,
                verified_at=email_model.verified_at,
            )
            return email

        password_reset_confirmation_key = getattr(
            model, "password_reset_confirmation_key", None
        )
        password_reset_confirmation_created_at = getattr(
            model, "password_reset_confirmation_created_at", None
        )
        password_reset_confirmation = (
            PasswordResetConfirmation(
                key=password_reset_confirmation_key,
                created_at=password_reset_confirmation_created_at,
            )
            if password_reset_confirmation_key
            and password_reset_confirmation_created_at
            else None
        )

        user = User(
            username=model.username,
            _password_hash=model._password_hash,
            is_active=model.is_active,
            is_superuser=model.is_superuser,
            password_reset_confirmation=password_reset_confirmation,
        )
        user.id = model.id
        user.emails = [
            from_email_model(email_model)
            for email_model in sorted(
                model.emails, key=lambda email_model: email_model.list_index
            )
        ]
        user.created_at = model.created_at
        return user
