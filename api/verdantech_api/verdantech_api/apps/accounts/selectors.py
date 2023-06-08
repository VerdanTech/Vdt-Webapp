from django.db.models import Q

from .models import User


def user_detail(fetched_by: User, username: str) -> User:
    """
    Return the user requested by the user
    """

    query = Q(username=username)

    user = User.objects.filter(query).first()

    if user is None:
        raise ApplicationError(message="User does not exist")

    return user
