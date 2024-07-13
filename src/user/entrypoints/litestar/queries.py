# Standard Library
import uuid

# External Libraries
from litestar import Controller, Request, get
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.exceptions import litestar_exception_map
from src.common.entrypoints.litestar.utils import url_to_route_name
from src.user.ops import queries

from . import urls


class UserQueryController(Controller):
    """User read operations controller"""

    path = urls.USER_QUERY_CONTROLLER_BASE
    tags = ["users"]

    @get(
        path=urls.USER_PUBLIC_PROFILES_URL,
        name=url_to_route_name(
            urls.USER_ROUTER_URL_BASE, urls.USER_PUBLIC_PROFILES_URL
        ),
        summary="User public profiles view.",
        description="Returns the profiles of the user ids given.",
        response_description="The list of users requested.",
        operation_id=queries.UserPublicProfilesQuery.to_operation_id()
    )
    async def public_profiles(
        self,
        user_ids: list[uuid.UUID],
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> list[queries.UserPublicSchema]:
        """
        Calls the public profiles query.

        Args:
            data (UserPublicProfilesQuery): input query.
            request (Request): Litestar http request object.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.

        Returns:
            list[UserPublicSchema]: the retrieved public profiles.
        """
        svcs_container.register_local_value(State, state)
        data = queries.UserPublicProfilesQuery(user_ids=user_ids)
        with litestar_exception_map():
            user_schemas = await queries.public_profiles(
                query=data, svcs_container=svcs_container
            )
        return user_schemas

    @get(
        path=urls.USER_CLIENT_PROFILE_URL,
        name=url_to_route_name(urls.USER_ROUTER_URL_BASE, urls.USER_CLIENT_PROFILE_URL),
        summary="User client profile view.",
        description="Returns the profile of the authenticated user.",
        response_description="The profile of the authenticated user.",
        operation_id="UserClientProfileQuery"
    )
    async def client_profile(
        self,
        request: Request,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.UserFullSchema:
        """
        Calls the client profile query.

        Args:
            data (UserPublicProfilesQuery): input query.
            request (Request): Litestar http request object.
            state (State): Litestar global app state.
            svcs_container (Container): service locator.

        Returns:
            UserFullSchema: the retrieved client profile.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            user_schema = await queries.client_profile(client=request.user)
        return user_schema
