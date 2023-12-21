# VerdanTech Source
from src import settings
from src.domain.user import exceptions as domain_exceptions
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt

from ..schemas import verification as schemas
from ..services import verification as verification_services


class UserVerificationOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def email_confirmation_request(
        self,
        data: schemas.UserVerifyEmailRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: AbstractEmailEmitter,
    ) -> None:
        """
        Given an unverified email, create a new email confirmation,
        and send an email confirmation email.

        Args:
            data (UserVerifyEmailRequestInput):
                verification request DTO.
            user_sanitizer (UserSanitizer): user object sanitizer.
            email_emitter (AbstractEmailEmitter): email emitter interface.

        Raises:
            UserNotFound: raised if no user with the email
                was found.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_address(
            email_address=data.email_address
        )
        if user is None:
            raise domain_exceptions.UserNotFound("The email address does not exist.")

        # Add new email verification
        await verification_services.email_confirmation_create(
            user=user,
            email_address=data.email_address,
            key_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        # Persist user
        await self.user_repo.update(user)

    async def email_confirmation_confirm(
        self,
        data: schemas.UserVerifyEmailConfirmInput,
        user_sanitizer: UserSanitizer,
    ) -> None:
        """
        Given an email confirmation key, verify the email
        if it exists and is in a verifiable state.

        Args:
            data (UserVerifyEmailConfirmInput):
                verification key DTO.
            user_sanitizer (UserSanitizer): user object sanitizer.

        Raises:
            EmailConfirmationKeyNotFound: raised if no user
                with matching email confirmation found.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_confirmation_key(
            email_confirmation_key=data.key
        )
        if user is None:
            raise domain_exceptions.UserNotFound(
                "The email verification key does not exist."
            )

        # Verify email
        user.email_confirmation_confirm(
            key=data.key,
            max_emails=settings.USER_MAX_EMAILS,
            expiry_time_hours=settings.EMAIL_VERIFICATON_EXPIRY_TIME_HOURS,
        )

        # Persist user
        await self.user_repo.update(user)

    async def password_reset_request(
        self,
        data: schemas.UserPasswordResetRequestInput,
        user_sanitizer: UserSanitizer,
        email_emitter: AbstractEmailEmitter,
    ) -> None:
        """
        Given an email, find the user associated, open up a new
        password reset request, and emit the reset email.

        Args:
            data (UserPasswordResetRequestInput): password reset
                request DTO.
            user_sanitizer (UserSanitizer): user object sanitizer.
            email_emitter (EmailEmitter): email emitter awaitable.

        Raises:
            UserNotFound: raised if a user with the email
                is nof found.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_address(
            email_address=data.email_address
        )
        if user is None:
            raise domain_exceptions.UserNotFound("The email address does not exist.")

        # Add new password reset confirmation
        await verification_services.password_reset_create(
            user=user,
            email_address=data.email_address,
            key_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        # Persist user
        await self.user_repo.update(user)

    async def password_reset_confirm(
        self,
        data: schemas.UserPasswordResetConfirmInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
    ):
        """
        Given a user ID, password confirmation key,
        and new password, find the user if it exists, validate
        the key, and set the new password.

        Args:
            data (UserPasswordResetConfirmInput): password
                reset confirm DTO.
            user_sanitizer (UserSanitizer): user object sanitizer.
            password_crypt (AbstractPasswordCrypt): password
                encryption interface.

        Raises:
            PasswordResetConfirmationNotFound: raised if the
                reset confirmation details fail to specify
                an existing user.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_password_reset_confirmation(
            user_id=data.user_id, password_reset_confirmation_key=data.key
        )
        if user is None:
            raise domain_exceptions.UserNotFound("The password reset does not exist")

        # Reset password
        await user.password_reset_confirm(
            user_id=data.user_id,
            key=data.key,
            new_password=data.new_password1,
            password_crypt=password_crypt,
        )

        # Persist user
        await self.user_repo.update(user)
