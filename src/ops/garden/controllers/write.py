# VerdanTech Source
from src import settings
from src.domain.garden.enums import RoleEnum
from src.domain.garden.garden import Garden
from src.domain.garden.sanitizers import GardenSanitizer
from src.domain.garden.services import create as create_domain_services
from src.domain.user import User
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.garden.garden import AbstractGardenRepository
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.ops.exceptions import EntityNotFound
from src.utils.key_generator import generate_unique_key

from ..schemas import read as read_schemas, write as write_schemas


class GardenWriteOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        self.garden_repo = garden_repo

    async def create(
        self,
        client: User,
        data: write_schemas.GardenCreateInput,
        user_repo: AbstractUserRepository,
        garden_sanitizer: GardenSanitizer,
        email_emitter: AbstractEmailEmitter,
    ) -> read_schemas.GardenFullSchema:
        """
        Creates and persists a new Garden with one GardenMembership for
        the creator and each invited user.

        Emits invitation email notifications.

        Args:
            client (User): the User that is creating the Garden.
            data (GardenCreateInput): the input DTO.
            user_repo (AbstractUserRepository): user entity persistence interface.
            garden_sanitizer (GardenSanitizer): garden entity persistence interface.
            email_emitter (AbstractEmailEmitter): email event interface.

        Raises:
            EntityNotFound: raised if any of the usernames included in
                data.admin_usernames, data.editor_usernames, and data.viewer_usernames
                do not correspond to usernames existing in the database.

        Returns:
            Garden: the created Garden after persistence.
        """
        # Sanitize input data
        await data.sanitize(garden_sanitizer=garden_sanitizer)

        # If any admins, editors, or viewers were given as invitees,
        # fetch the user objects and consolidate into a list of tuples
        invitee_role_tuples: create_domain_services.UserRoleTupleList = []
        invitee_usernames = (
            (data.admin_usernames or [])
            + (data.editor_usernames or [])
            + (data.viewer_usernames or [])
        )
        if invitee_usernames is not []:
            invitees = await user_repo.get_users_by_usernames(
                usernames=invitee_usernames, return_first_none=True
            )
            if invitees is None:
                raise EntityNotFound("A username was provided which does not exist.")

            invitee_role_tuples = [
                (user, RoleEnum.ADMIN)
                if data.admin_usernames is not None
                and user.username in data.admin_usernames
                else (user, RoleEnum.EDIT)
                if data.editor_usernames is not None
                and user.username in data.editor_usernames
                else (user, RoleEnum.VIEW)
                for user in invitees
            ]

        # Generate a unique Garden Key
        key = await generate_unique_key(
            length=settings.GARDEN_STR_ID_LENGTH,
            repo=self.garden_repo,
            existence_method_name="key_id_exists",
            existence_method_argument_name="key",
        )

        # Create the Garden and GardenMembership objects.
        garden, user_invitation_tuples = create_domain_services.garden_create(
            creator=client,
            key=key,
            name=data.name,
            visibility=data.visibility,
            description=data.description,
            invitee_role_tuples=invitee_role_tuples,
        )

        # Persist new garden
        garden = await self.garden_repo.add(garden)

        # Send out invitiation notifications.
        if user_invitation_tuples is not []:
            for user_invitation_tuple in user_invitation_tuples:
                user = user_invitation_tuple[0]
                membership = user_invitation_tuple[1]
                await email_emitter.emit_garden_invite(
                    email_address=user.primary_email.address,
                    username=user.username,
                    garden_key_id=garden.key,
                    garden_name=garden.name,
                    inviter_username=client.username,
                    role=str(membership.role),
                )

        garden_schema = read_schemas.GardenFullSchema.from_model(garden=garden)

        return garden_schema

    async def change(self):
        pass
