# VerdanTech Source
from src.domain.garden.garden import Garden
from src.domain.garden.membership import GardenMembership
from src.domain.garden.services import membership as membership_domain_services
from src.domain.user import User
from src.exceptions import ApplicationException, ExceptionResponseEnum
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.garden.garden import AbstractGardenRepository
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.ops.exceptions import EntityNotFound

from ..schemas import membership as membership_schemas, read as read_schemas


class GardenMembershipOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        self.garden_repo = garden_repo

    async def invite(
        self,
        client: User,
        data: membership_schemas.GardenInviteCreateInput,
        user_repo: AbstractUserRepository,
        email_emitter: AbstractEmailEmitter,
    ) -> read_schemas.GardenMembershipFullSchema:
        """
        Creates a new GardenMembership invite.
        Emits email notification.

        Args:
            client (User): the User responsible for the invitiation.
            data (schemas.GardenInviteCreateInput): input DTO.
            user_repo (AbstractUserRepository): user entity persistence interface
            email_emitter (AbstractEmailEmitter): email event interface.

        Raises:
            EntityNotFound: raised if data.user_username
                or data.garden_key do not exist.

        Returns:
            GardenMembership: the membership after persistence.
        """
        # Retrieve invitee
        invitee = await user_repo.get_user_by_username(username=data.user_username)
        if invitee is None:
            raise EntityNotFound("This User does not exist.")

        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_key(key=data.garden_key)
        if garden is None:
            raise EntityNotFound("This Garden does not exist.")

        # Create the GardenMembership object.
        membership = membership_domain_services.create_garden_membership(
            client=client, invitee=invitee, garden=garden, role=data.role
        )

        # Persist garden
        await self.garden_repo.update(garden)

        # Send the email notification.
        await email_emitter.emit_garden_invite(
            email_address=invitee.primary_email.address,
            username=invitee.username,
            garden_key_id=garden.key,
            garden_name=garden.name,
            inviter_username=client.username,
            role=str(membership.role),
        )

        membership_schema = read_schemas.GardenMembershipFullSchema.from_model(
            membership=membership
        )

        return membership_schema

    async def accept_invite(
        self, client: User, garden_key: str
    ) -> read_schemas.GardenMembershipFullSchema:
        """
        Accepts a GardenMembership invite.

        Args:
            client (User): the User responsible for the invitation acceptance.
            data (schemas.GardenInviteAcceptInput): input DTO

        Raises:
            EntityNotFound: raised if data.garden_key does not exist.

        Returns:
            GardenMembership: the membership after persistence.
        """
        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_key(garden_key)
        if garden is None:
            raise EntityNotFound("This Garden does not exist.")

        # Accept the invite - raises on failure
        membership = garden.confirm_membership(user=client)

        # Persist garden
        await self.garden_repo.update(garden)

        membership_schema = read_schemas.GardenMembershipFullSchema.from_model(
            membership=membership
        )

        return membership_schema

    async def leave(self, client: User, garden_key: str) -> None:
        """
        Removes the client from the garden.

        Args:
            client (User): the User to remove from the Garden.
            garden_key (str): the key of the Garden to remove from.

        Raises:
            EntityNotFound: raised if the garden key does not exist.
        """
        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_key(garden_key)
        if garden is None:
            raise EntityNotFound("This Garden does not exist.")

        # Remove client's membership
        garden.remove_membership(user=client)

        # Persist garden
        await self.garden_repo.update(garden)

    async def revoke_membership(
        self,
        client: User,
        data: membership_schemas.GardenRevokeMembershipInput,
        user_repo: AbstractUserRepository,
    ) -> None:
        """
        Removes a User that is not the client from a Garden.

        Args:
            client (User): the User responsible for the removal.
            data (schemas.GardenRevokeMembershipInput): input DTO.
            user_repo (AbstractUserRepository): user entity persistence interface.

        Raises:
            EntityNotFound: raised if data.user_username or
                data.garden_key do not exist.
        """
        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_key(data.garden_key)
        if garden is None:
            raise EntityNotFound("This Garden does not exist.")

        # Retrieve user
        user = await user_repo.get_user_by_username(username=data.user_username)
        if user is None:
            raise EntityNotFound("This User does not exist.")

        # Remove the membership
        membership_domain_services.revoke_membership(
            client=client, subject=user, garden=garden
        )

        # Persist garden
        await self.garden_repo.update(garden)

    async def change_role(
        self,
        client: User,
        data: membership_schemas.GardenRoleChangeInput,
        user_repo: AbstractUserRepository,
    ) -> read_schemas.GardenMembershipFullSchema:
        """
        Changes the role of a GardenMembership.

        Args:
            client (User): the User responsible for the change.
            data (schemas.GardenRevokeMembershipInput): input DTO.
            user_repo (AbstractUserRepository): user entity persistence interface.

        Raises:
            EntityNotFound: raised if data.user_username or
                data.garden_key do not exist.
        """
        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_key(data.garden_key)
        if garden is None:
            raise EntityNotFound("This Garden does not exist.")

        # Retrieve user
        user = await user_repo.get_user_by_username(username=data.user_username)
        if user is None:
            raise EntityNotFound("This User does not exist.")

        # Change the role on the membership
        membership_domain_services.change_role(
            client=client, subject=user, garden=garden, new_role=data.role
        )

        # Persist garden
        await self.garden_repo.update(garden)

        membership = garden.get_membership(user=user)
        if membership is None:
            raise ApplicationException(
                "Failed to retrieve garden membership when it should have existed.",
                response=ExceptionResponseEnum.SERVER_ERROR,
            )

        membership_schema = read_schemas.GardenMembershipFullSchema.from_model(
            membership=membership
        )

        return membership_schema
