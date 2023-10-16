from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base

IDType = Integer
Base = declarative_base()


class BaseAlchemyModel(Base):
    __abstract__ = True
