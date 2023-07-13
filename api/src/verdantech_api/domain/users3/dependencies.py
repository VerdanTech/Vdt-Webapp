from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from verdantech_api.lib.field_validators.generic import FieldValidator
    from verdantech_api.lib.crypt.generic import PasswordCrypt
    from verdantech_api.lib.email.generic import AsyncEmailClient
    from verdantech_api.lib.utils import StringIDGeneratorT

from .services.email_verification import EmailConfirmationRepo, EmailVerificationService
from .services.users import EmailRepo, UserRepo, UserService


def provide_user_repo(
    db_session: AsyncSession,
    username_field_validator: FieldValidator,
    password_field_validator: FieldValidator,
):
    return UserRepo(
        session=db_session,
        username_feild_validator=username_field_validator,
        password_field_validator=password_field_validator,
    )


def provide_email_repo(db_session: AsyncSession, email_field_validator: FieldValidator):
    return EmailRepo(session=db_session, email_field_validator=email_field_validator)


def provide_email_confirmation_repo(db_session: AsyncSession):
    return EmailConfirmationRepo(session=db_session)


def provide_password_reset_confirmation_repo(db_session: AsyncSession):
    pass


def provide_user_service(
    user_repo: UserRepo,
    email_repo: EmailRepo,
    password_crypt: PasswordCrypt,
):
    return UserService(
        user_repo=user_repo,
        email_repo=email_repo,
        password_crypt=password_crypt,
    )


def provide_email_verification_service(
    email_client: AsyncEmailClient,
    email_repo: EmailRepo,
    email_confirmation_repo: EmailConfirmationRepo,
    key_generator: StringIDGeneratorT,
):
    return EmailVerificationService(
        email_client=email_client,
        email_repo=email_repo,
        email_confirmation_repo=email_confirmation_repo,
        key_generator=key_generator,
    )


def provide_password_reset_service():
    pass


def provide_auth_service():
    pass
