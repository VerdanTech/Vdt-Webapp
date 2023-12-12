# External Libraries
from svcs import Container

# VerdanTech Source
from src import settings
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.domain.user.services import email as email_domain_services
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt

from ..schemas import write as schemas


class UserWriteOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def create(
        self,
        data: schemas.UserCreateInput,
        svcs_container: Container,
    ) -> User:
        """
        Main user creation operation.

        Args:
            data (UserCreateInput): user creation data transfer object.
            svcs_container (Container): svcs dependency container
                for service location.

        Returns:
            User: the user model created after persistence.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt, email_emitter = await svcs_container.aget_abstract(
            AbstractPasswordCrypt, AbstractEmailEmitter
        )

        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Create a new user
        user = User(username=data.username)
        await user.set_password(password=data.password1, password_crypt=password_crypt)
        await email_domain_services.email_create(
            user=user,
            address=data.email_address,
            max_emails=settings.USER_MAX_EMAILS,
            verification=settings.EMAIL_CONFIRMATION.verification_required(),
            key_length=settings.VERIFICATION_KEY_MAX_LENGTH,
            user_repo=self.user_repo,
            email_emitter=email_emitter,
        )

        # Persist user
        user = await self.user_repo.add(user)

        return user

    async def username_change(self):
        pass

    async def email_change(self):
        pass

    async def password_change(self):
        pass

    async def delete(self):
        pass
