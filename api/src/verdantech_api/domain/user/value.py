from dataclasses import dataclass
from typing import List
from datetime import datetime

from ..common.values import Value


class BaseConfirmation(Value):
    key: str
    created_at: datetime

class EmailConfirmation(BaseConfirmation):
    pass


class PasswordResetConfirmation(BaseConfirmation):
    hashed_password: str

class Email(Value):
    address: str
    verified: bool
    confirmation: EmailConfirmation