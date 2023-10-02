from serpyco import Serializer as SerpycoSerializer
from src.verdantech_api.domain.models.user.entities import User

from ..generic import SerpycoSerializer


class UserSerpycoSerializezr(SerpycoSerializer[User]):
    """Implementation of serializer interface for User object
    using Serpyco
    """

    entity = User
    serializer = SerpycoSerializer(User)
