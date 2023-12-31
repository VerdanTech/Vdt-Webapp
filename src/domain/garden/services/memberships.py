from src.domain.user.entities import User
from typing import Optional
from ..entities import GardenMembership, Garden
from ..enums import RoleEnum
from src.domain.common import Ref

def invite_user(client: User, user: User, garden: Garden, role: RoleEnum = RoleEnum.VIEW) -> Optional[GardenMembership]:
    
    # Check if inviter is authorized.

    membership = GardenMembership(inviter=Ref(id=client.id), user=Ref(id=client.id), garden=Ref(id=client.id), role=role)
    
    return membership

def accept_invite(client: User, membership: GardenMembership) -> GardenMembership:
    
    membership.open_invite = False

    return membership

def set_role(client: User, subject: User):
    pass

def leave():
    pass