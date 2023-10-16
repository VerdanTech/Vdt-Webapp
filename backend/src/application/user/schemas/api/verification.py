from dataclasses import dataclass

from src.domain.common.entities import EntityIDType


@dataclass
class UserVerifyEmailRequestInput:
    email_address: str


@dataclass
class UserVerifyEmailConfirmInput:
    key: str


@dataclass
class UserPasswordResetRequestInput:
    email_address: str


@dataclass
class UserPasswordResetConfirmInput:
    user_id: EntityIDType
    key: str
    old_password: str
    new_password1: str
    new_password2: str
