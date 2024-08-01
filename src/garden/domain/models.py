# Standard Library
import random
import string
from datetime import datetime

# External Libraries
from attrs import field

# VerdanTech Source
from src import settings
from src.common.domain import (
    Ref,
    RootEntity,
    Value,
    root_entity_transform,
    value_transform,
)
from src.common.domain.exceptions import FieldNotFound
from src.user.domain import User
from src.utils import key_generator

from .enums import OperationEnum, PermissionEnum, RoleEnum, VisibilityEnum
from .events import MembershipAccepted, MembershipRevoked
from .exceptions import GardenAuthorizationException, MembershipAlreadyConfirmed
from .permission import PermissionRouter, permission_rules
from .commands import GARDEN_KEY_MAX_LENGTH

# Load all plant names
plant_names = []
with open(settings.static_path("plant_names.txt"), "r") as file:
    """
    Load all plant names from the static file.

    1. Strip whitespace from all lines.
    2. Reject any names that are too long.
    3. Convert all names to lowercase.
    4. Replace spaces with hyphens.
    """
    for line in file:
        plant_name = line.strip()
        if len(plant_name) < GARDEN_KEY_MAX_LENGTH:
            plant_names.append(plant_name.lower().replace(" ", "-"))


def generate_garden_key(use_random_plant_name: bool) -> str:
    """
    Generate a new random garden key.

    There are two ways to generate a key:
    1. Use a random string of letters and digits
    equal to the GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_NO_PLANT_NAME in settings.
    2. Start with a random plant name, and up to GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_NO_PLANT_NAME
    random letters or digits prepended with a hyphen, up to GARDEN_KEY_MAX_LENGTH total characters.

    Args:
        use_random_plant_name (bool): whether to use a
            random plant name as the prefix of the key.

    Returns:
        str: the generated key.
    """
    key: str
    if use_random_plant_name:
        key = random.choice(plant_names)
        keygen_length = min(
            settings.GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_PLANT_NAME,
            GARDEN_KEY_MAX_LENGTH - (len(key) + 1),
        )
        # Ensure generated key starts with a number
        if keygen_length > 0:
            key = key + "-"
            keygen = key_generator.key_generator(
                1, string.digits
            ) + key_generator.key_generator(keygen_length - 1)
            key = key + keygen
    else:
        key = key_generator.key_generator(
            settings.GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_NO_PLANT_NAME
        )

    return key


@value_transform
class GardenInvite(Value):
    """
    Simple class to represent a garden invite.
    """

    user_ref: Ref[User]
    role: RoleEnum
    user_username: str | None = None
    user_email: str | None = None


@value_transform
class GardenMembership(Value):
    """
    GardenMembership domain value.

    GardenMemberships connect Users and Gardens,
    allowing conditional access with different roles.

    Attributes:
        user_ref (Ref[User]): the holder of the membership.
        inviter_ref (Ref[User] | None): the user responsible for creating the membership.
        role (RoleEnum): the persmissions of the membership.
        accepted (bool): whether the membership invitation has been accepted.
        accepted_at (datetime | None): the time the membership was accepted.
        favorite (bool): whether the membership is marked as a favorite.
        created_at (datetime): the time the membership.
    """

    user_ref: Ref[User]
    inviter_ref: Ref[User] | None
    role: RoleEnum = RoleEnum.VIEW
    accepted_at: datetime | None = None
    favorite: bool = False
    created_at: datetime = field(factory=datetime.now)

    @property
    def accepted(self) -> bool:
        """
        Whether the membership invitation has been accepted.
        """
        return self.accepted_at is not None

    def authorize(self, operation: OperationEnum) -> bool:
        """
        Compares self with an operation ID to asses the
        application of the permission rule associated with the operation.

        Args:
            operation (OperationEnum): operation to authorize.

        Returns:
            bool: true if the operation is authorized.
        """
        permission = permission_rules[operation]
        role = self.role
        return self._authorize(role=role, permission=permission)

    def assert_authorization(self, operation) -> None:
        """
        Compares self with an operation ID to asses the
        application of the permission rule associated with the operation.

        Args:
            operation (OperationEnum): operation to authorize.

        Raises:
            GardenAuthorizationException: raised if the authorization fails.
        """
        permission = permission_rules[operation]
        role = self.role
        if not self._authorize(role=self.role, permission=permission):
            raise GardenAuthorizationException(
                f"""
                The action: \"{operation}\" 
                requires the permission: \"{permission}\", 
                but this user has role: \"{role}\".
                """
            )

    def _authorize(self, role: RoleEnum, permission: PermissionEnum) -> bool:
        """
        Compares a GardenMembership's role with a permission requirement.

        Args:
            role (RoleEnum): role of the GardenMembership.
            permission (PermissionEnum): the permission level
                of the operation.

        Returns:
            bool: true if the role is authorized to peform the operation.
        """
        if permission is PermissionEnum.REQUIRES_ADMIN and role is RoleEnum.ADMIN:
            return True
        elif permission is PermissionEnum.REQUIRES_EDIT and (
            role is RoleEnum.ADMIN or role is RoleEnum.EDIT
        ):
            return True
        elif permission is PermissionEnum.REQUIRES_VIEW and (
            role is RoleEnum.ADMIN or role is RoleEnum.EDIT or role is RoleEnum.VIEW
        ):
            return True
        return False


@root_entity_transform
class Garden(RootEntity):
    """
    Garden entity domain model.

    A Garden is the highest level container in the application.
    It groups together multiple Users via GardenMemberships,
    and serves as a one-to-many reference point for Workspaces, Plantsets,
    and most other application models.

    Attributes:
        name (str): Nnn-unique name.
        key (str): unique shortand name for URLs - unique.
        creator (Ref[User]): user who created the Garden.
        visibility (VisibilityEnum): controls which non-member users can view this Garden.
        memberships (set[GardenMembership]): all memberships in the Garden. One per User.
        description (str): optional description.
        is_active (bool): whether the Garden is active. Marks for deletion.
    """

    name: str  # type: ignore
    key: str  # type: ignore
    creator_ref: Ref[User] | None  # type: ignore
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    memberships: set[GardenMembership] = field(factory=set)
    description: str = ""
    is_active: bool = True

    @property
    def num_memberships(self) -> int:
        """
        The number of memberships contained in the garden.

        Returns:
            int: the number of memberships.
        """
        return len(self.memberships)

    def is_user_member(self, user: User) -> bool:
        """
        Returns whether the user has a membership in the garden,
        pending acceptance or not.

        Args:
            user (User): the user to check membership for.

        Returns:
            bool: whether the user is a member of the garden.
        """
        return any(membership.user_ref.id == user.id for membership in self.memberships)

    def get_membership(self, user: User) -> GardenMembership | None:
        """
        Returns the GardenMembership belonging to a User,
        or None if no membership exists.

        Args:
            user (User): the member to return the membership for.

        Returns:
            Optional[GardenMembership]: the membership, or None if
                no membership exists.
        """
        if not user.persisted:
            return None

        for membership in self.memberships:
            if membership.user_ref.id == user.id:
                return membership

        return None

    def accept_membership(self, user: User) -> GardenMembership:
        """
        Closes a membership invitation given the User it belongs to.

        Args:
            user (User): the User with the GardenMembership invite
                to accept.

        Raises:
            MembershipAlreadyConfirmed: raised if the User does have
                an existing GardenMembership, but the invite has
                already been confirmed.
            FieldNotFound: raised if the User does not have an
                existing GardenMembership.

        Returns:
            GardenMembership: the GardenMembership after confirmation.
        """
        for membership in self.memberships:
            if membership.user_ref.id == user.id:
                if membership.accepted:
                    raise MembershipAlreadyConfirmed(
                        "The invite to this Garden has already been accepted."
                    )

                new_membership = membership.transform(
                    accepted=True, accepted_at=datetime.now()
                )
                self.memberships.remove(membership)
                self.memberships.add(new_membership)

                self.events.append(
                    MembershipAccepted(
                        user_ref=user.ref, garden_ref=self.ref, role=membership.role
                    )
                )

                return membership

        raise FieldNotFound("The User does not have an invitation to this Garden.")

    def remove_membership(self, user: User) -> None:
        """
        Removes a membership given the User is belongs to.

        Args:
            user (User): the User with the GardenMembership invite
                to remove.

        Raises:
            FieldNotFound: raised if the User does not have an
                existing GardenMembership.
        """
        for membership in self.memberships:
            if membership.user_ref.id == user.id:
                self.memberships.remove(membership)
        raise FieldNotFound("The User does not have a membership with this Garden.")

    def revoke_membership(self, client: User, subject: User) -> None:
        """
        Removes a User that is not the client from the Garden,
        and proper authorization from the client.

        Args:
            client (User): the User responsible for the removal.
            subject (User): the User that is subject to the removal.

        Raises:
            ValueError: raised if the client is the same as the subject.
            FieldNotFound: raised if the subject does not have a GardenMembership
                with the Garden.
            GardenAuthorizationException: raised if the client does
                not have the required permissions on their GardenMembership.
        """
        if client == subject:
            raise ValueError("A client cannot kick themselves from a Garden.")

        # Raise if subject does not exist in the garden already.
        subject_membership = self.get_membership(user=subject)
        if subject_membership is None:
            raise FieldNotFound("User does not have a membership with this Garden.")

        # Raise if client is unauthorized.
        client_membership = self.get_membership(user=client)
        if client_membership is None:
            raise GardenAuthorizationException(
                "Not authorized to perform operations in this Garden."
            )
        client_membership.assert_authorization(
            operation=PermissionRouter.revoke_membership(role=subject_membership.role),
        )

        # Remove the membership
        self.remove_membership(user=subject)

        # Add event
        self.events.append(MembershipRevoked(garden_ref=self.ref, user_ref=subject.ref))

    def change_role(
        self, client: User, subject: User, new_role: RoleEnum
    ) -> GardenMembership:
        """
        Changes the role of a membership given the subject it belongs to
        and proper authorization from the client.

        Args:
            client (User): the User responsible for the role change.
            subject (User): the User that is subject to the role change.
            new_role (RoleEnum): the new role to set on the membership.

        Raises:
            FieldNotFound: raised if the User does not have an
                existing GardenMembership.
        """
        if client == subject:
            raise ValueError("A client cannot change their own role.")

        # Raise if subject does not exist in the garden already.
        subject_membership = self.get_membership(user=subject)
        if subject_membership is None:
            raise FieldNotFound("User does not have a membership with this Garden.")

        # Raise if client is unauthorized.
        client_membership = self.get_membership(user=client)
        if client_membership is None:
            raise GardenAuthorizationException(
                "Not authorized to perform operations in this Garden."
            )
        client_membership.assert_authorization(
            operation=PermissionRouter.change_role(
                client_role=client_membership.role, new_role=new_role
            ),
        )

        # Change the role
        new_subject_membership = subject_membership.transform(role=new_role)
        self.memberships.remove(subject_membership)
        self.memberships.add(new_subject_membership)
        return new_subject_membership
