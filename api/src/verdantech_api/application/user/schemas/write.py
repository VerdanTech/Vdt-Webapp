from dataclasses import dataclass


@dataclass
class UserCreateInput:
    email_address: str
    username: str
    password1: str
    password2: str
