from dataclasses import dataclass
from datetime import datetime
from typing import List

from ..common.values import Ref, Value


class UserRef(Ref):
    pass


class BaseConfirmation(Value):
    key: str
    created_at: datetime


class EmailConfirmation(BaseConfirmation):
    pass


class PasswordResetConfirmation(BaseConfirmation):
    hashed_password: str


class Email(Value):
    address: str
    verified: bool = False
    confirmation: EmailConfirmation | None
