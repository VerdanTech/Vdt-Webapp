from serpyco import Serializer as SerpycoSerializer
from src.domain.user.entities import User

from ..generic import BaseSerpycoMapper


class UserSerpycoMapper(BaseSerpycoMapper[User]):
    """Implementation of serializer interface for User object
    using Serpyco
    """

    entity = User
    serializer = SerpycoSerializer(User)
