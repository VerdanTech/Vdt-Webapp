# External Libraries
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseAlchemyModel(Base):
    __abstract__ = True
