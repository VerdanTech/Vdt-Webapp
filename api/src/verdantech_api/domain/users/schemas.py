from dataclasses import dataclass

from litestar.dto.factory import DTOConfig
from litestar.dto.factory.stdlib.dataclass import DataclassDTO

from .models import UserModel


@dataclass
class UserOutput(DataclassDTO[UserModel]):
    config = DTOConfig(include={"username"})


@dataclass
class UserCreateInput:
    email: str
    username: str
    password1: str
    password2: str
