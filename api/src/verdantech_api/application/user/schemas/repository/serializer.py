from serpyco import Serializer

from src.verdantech_api.domain.models.user.entities import User

class UserPersistenceSchema(User):
    pass

UserPersistenceSerializer = Serializer(UserPersistenceSchema)
