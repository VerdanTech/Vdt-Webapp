# VerdanTech Source
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.persistence.user import AbstractUserRepository
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.exceptions import EntityNotFound

from ..schemas import auth as schemas


class UserAuthOpsController:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def login(
        self,
        data: schemas.UserLoginInput,
        user_sanitizer: UserSanitizer,
        password_crypt: AbstractPasswordCrypt,
    ) -> User | None:
        """
        User login operation.

        Returns a User object if authentication was successful.

        Args:
            data (schemas.UserLoginInput): user login input DTO.
            user_sanitizer (UserSanitizer): user object sanitizer.
            password_crypt (AbstractPasswordCrypt): password hashing interface.

        Raises:
            EntityNotFound: raised if the supplied email does not match a user.

        Returns:
            User | None: the authenticated User object, or None.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_address(
            email_address=data.email_address
        )
        if user is None:
            raise EntityNotFound("The email address does not exist.")

        # Todo: verify email is confirmed if settings.EMAIL_CONFIRMATION is REQUIRED_FOR_LOGIN

        # Verify password
        if await user.verify_password(
            password=data.password, password_crypt=password_crypt
        ):
            return user
        else:
            return None
