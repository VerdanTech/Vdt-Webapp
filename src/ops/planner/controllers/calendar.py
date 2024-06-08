# VerdanTech Source
from src import settings
from src.domain.planner.calendar import PlantingCalendar
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.exceptions import EntityNotFound

from ..schemas import calendar as schemas
from ..services import verification as verification_services


class PlannerCalendarOpsController:
    def __init__(self, cultivar_repo: AbstractCultivarRepository):
        self.cultivar_repo = cultivar_repo

    async def get_planting_calendar(self) -> PlantingCalendar:

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
            EntityNotFound: raised if no user with the email
                was found.
        """
        # Sanitize input data
        await data.sanitize(user_sanitizer=user_sanitizer)

        # Retrieve user from persistence
        user = await self.user_repo.get_user_by_email_address(
            email_address=data.email_address
        )
        if user is None:
            raise EntityNotFound("The email address does not exist.")

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