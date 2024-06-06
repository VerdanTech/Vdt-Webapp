# VerdanTech Source
from src import settings
from src.domain.user import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.exceptions import IncorrectPassword

from ..schemas import read as read_scheams, write as write_schemas
from ..services import email as email_services


class UserWriteOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def create(
        self,
        data: write_schemas.UserCreateInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
        email_emitter: AbstractEmailEmitter,
    ) -> User:
        """
        Main user creation operation.

        Args:
            data (UserCreateInput): user creation data transfer object.
            user_sanitizer (UserSanitizer): user object sanitizer.
            password_crypt (AbstractPasswordCrypt): password encryption interface.
            email_emitter (AbstractEmailEmitter): email emitter interface.

        Returns:
            User: the user model created after persistence.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Create a new user
        user = User(username=data.username)
        await user.set_password(password=data.password1, password_crypt=password_crypt)
        await email_services.email_create(
            user=user,
            address=data.email_address,
            max_emails=settings.USER_MAX_EMAILS,
            verification=settings.EMAIL_CONFIRMATION.verification_required,
            key_length=settings.VERIFICATION_KEY_MAX_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        # Persist user
        user = await self.user_repo.add(user)

        return user

    async def change(
        self,
        client: User,
        data: write_schemas.UserChangeInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
        email_emitter: AbstractEmailEmitter,
    ) -> read_scheams.UserFullSchema:
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Authenticate password
        if not await client.verify_password(
            password=data.password, password_crypt=password_crypt
        ):
            raise IncorrectPassword("Provided password is incorrect.")

        # Update the requested fields
        if data.new_username:
            client.username = data.new_username

        if data.new_email_address:
            await email_services.email_create(
                user=client,
                address=data.email_address,
                max_emails=settings.USER_MAX_EMAILS,
                verification=settings.EMAIL_CONFIRMATION.verification_required,
                key_length=settings.VERIFICATION_KEY_MAX_LENGTH,
                user_repo=self.user_repo,
                email_emitter=email_emitter,
            )

        if data.new_password1:
            await client.set_password(
                password=data.new_password1,
                password_crypt=password_crypt,
                overwrite=True,
            )

        # Persist user
        user = await self.user_repo.add(client)

        user_schema = read_scheams.UserFullSchema.from_model(user)

        return user_schema
