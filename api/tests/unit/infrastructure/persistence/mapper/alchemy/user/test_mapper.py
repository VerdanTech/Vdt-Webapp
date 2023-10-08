from datetime import datetime

from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.values import (
    Email,
    EmailConfirmation,
    PasswordResetConfirmation,
)
from src.verdantech_api.infrastructure.persistence.mapper.alchemy.model import (
    BaseAlchemyModel,
)
from src.verdantech_api.infrastructure.persistence.mapper.alchemy.user import (
    EmailAlchemyModel,
    UserAlchemyMapper,
    UserAlchemyModel,
)

from ..utils import assert_equivalent_entities, assert_equivalent_models


class TestUserAlchemyMapper:
    def test_to_model(self) -> None:
        """Ensure that the method maps a user
            domain entity into a sqlalchemy model
            with the proper attributes and relations
        """
        user = User(
            username="U",
            username_norm="u",
            _password_hash="p",
            is_active=False,
            is_superuser=True,
            password_reset_confirmation=PasswordResetConfirmation(key="2"),
            created_at=datetime(2000, 1, 1),
        )
        user.id = 0
        user.emails = [
            Email(address="e1", confirmation=EmailConfirmation(key="1")),
            Email(address="e2"),
        ]
        expected_user_model = UserAlchemyModel(
            id=user.id,
            username=user.username,
            username_norm=user.username_norm,
            _password_hash=user._password_hash,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            password_reset_confirmation=user.password_reset_confirmation,
            created_at=user.created_at,
        )
        expected_email_models = [
            EmailAlchemyModel(
                user_id=expected_user_model.id,
                user=expected_user_model,
                list_index=0,
                address=user.emails[0].address,
                verified=user.emails[0].verified,
                primary=user.emails[0].primary,
                confirmation=user.emails[0].confirmation,
                verified_at=user.emails[0].verified_at,
            ),
            EmailAlchemyModel(
                user_id=expected_user_model.id,
                user=expected_user_model,
                list_index=1,
                address=user.emails[1].address,
                verified=user.emails[1].verified,
                primary=user.emails[1].primary,
                confirmation=user.emails[1].confirmation,
                verified_at=user.emails[1].verified_at,
            ),
        ]
        expected_user_model.emails = expected_email_models

        user_model = UserAlchemyMapper.to_model(entity=user)

        assert_equivalent_models(user_model, expected_user_model)

    def test_from_model(self) -> None:
        """Ensure that the method maps a sqlalchemy user
            model into a domain entity with the proper
            attributes and nested structure        
        """
        user_model = UserAlchemyModel(
            id=0,
            username="U",
            username_norm="u",
            _password_hash="p",
            is_active=False,
            is_superuser=True,
            password_reset_confirmation=PasswordResetConfirmation(key="2"),
            created_at=datetime(2000, 1, 1),
        )
        email_models = [
            EmailAlchemyModel(
                user_id=user_model.id,
                user=user_model,
                list_index=0,
                address="e1",
                verified=False,
                primary=False,
                confirmation=EmailConfirmation(key="1"),
                verified_at=datetime(2001, 1, 1),
            ),
            EmailAlchemyModel(
                user_id=user_model.id,
                user=user_model,
                list_index=1,
                address="e2",
                verified=True,
                primary=True,
                verified_at=datetime(2002, 1, 1),
            ),
        ]
        user_model.emails = email_models
        expected_user = User(
            username=user_model.username,
            username_norm=user_model.username_norm,
            _password_hash=user_model._password_hash,
            is_active=user_model.is_active,
            is_superuser=user_model.is_superuser,
            password_reset_confirmation=user_model.password_reset_confirmation,
            created_at=user_model.created_at,
        )
        expected_user.id = user_model.id
        expected_user.emails = [
            Email(
                address=user_model.emails[0].address,
                confirmation=user_model.emails[0].confirmation,
                verified=user_model.emails[0].verified,
                primary=user_model.emails[0].primary,
                verified_at=user_model.emails[0].verified_at,
            ),
            Email(
                address=user_model.emails[1].address,
                verified=user_model.emails[1].verified,
                primary=user_model.emails[1].primary,
                verified_at=user_model.emails[1].verified_at,
            ),
        ]

        user = UserAlchemyMapper.from_model(model=user_model)

        assert_equivalent_entities(user, expected_user)
