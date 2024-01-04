# Standard Library
from dataclasses import field, replace
from typing import Optional

# External Libraries
from sqlalchemy import ReturnsRows

# VerdanTech Source
from src import settings
from src.domain.common import (
    Entity,
    Ref,
    RootEntity,
    entity_dataclass,
    root_entity_dataclass,
)
from src.domain.plants.entities import PlantSet
from src.domain.user.entities import User
from src.domain.workspace.entities import Workspace
from src.utils.key_generator import key_generator

from .enums import RoleEnum, VisibilityEnum
from .values import EnvironmentAttributeProfile, GardenMembership


@root_entity_dataclass
class Garden(RootEntity):
    name: str
    creator: Ref[User] | None
    key_id: str = field(
        default_factory=lambda: key_generator(length=settings.GARDEN_STR_ID_LENGTH)
    )
    memberships: list[GardenMembership] = field(default_factory=list)
    description: str | None = None
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    plantsets: list[Ref[PlantSet]] = field(default_factory=list)
    workspaces: list[Ref[Workspace]] = field(default_factory=list)
    attributes: list[EnvironmentAttributeProfile] = field(default_factory=list)

    def get_membership(self, user: User) -> Optional[GardenMembership]:
        if user.persisted is False:
            return None

        for membership in self.memberships:
            if membership.user.id == user.id:
                return membership

        return None

    def is_user_member(self, user: User) -> bool:
        if user.persisted is False:
            return False

        if self.creator is not None and user.id == self.creator.id:
            return True

        if user.id in [membership.user.id for membership in self.memberships]:
            return True

        return False

    def is_user_confirmed_member(self, user: User) -> bool:
        if user.persisted is False:
            return False

        if self.creator is not None and user.id == self.creator.id:
            return True

        if user.id in [
            membership.user.id
            for membership in self.memberships
            if membership.open_invite is False
        ]:
            return True

        return False

    def confirm_membership(self, user: User) -> GardenMembership | None:
        self.assert_persisted()
        user.assert_persisted()

        for idx, membership in enumerate(self.memberships):
            if membership.user.id == user.id:
                if membership.open_invite is False:
                    return None
                self.memberships[idx] = replace(membership, open_invite=False)

                return membership
        return None

    def remove_membership(self, user: User):
        for idx, membership in enumerate(self.memberships):
            if membership.user.id == user.id:
                self.memberships.pop(idx)
