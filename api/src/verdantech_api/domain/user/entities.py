from dataclasses import dataclass
from typing import List
from datetime import datetime

from ..common.entities import Entity
from .values import Email, PasswordResetConfirmation

class User(Entity):
    username: str
    hashed_password: str
    emails: List[Email]
    is_active: bool
    is_superuser: bool
    password_reset_confirmation: PasswordResetConfirmation
