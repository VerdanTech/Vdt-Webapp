from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase

IDType = Integer


class BaseAlchemyModel(DeclarativeBase):
    pass
