# Standard Library
from dataclasses import dataclass, field

# VerdanTech Source
from src.domain.garden.enums import VisibilityEnum
from src.domain.garden.sanitizers import GardenSanitizer
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum as specs


@dataclass
class GardenCreateInput:
    """
    Garden creation DTO

    Fields:
        name (str): The name of the Garden. Non-unique across a user's
            created gardens or the application.
        description (str): The description of the Garden.
            Defaults to empty string.
        admin_usernames (str):
            A list of usernames to be invited as admins to the new garden.
            Usernames must exist or EntityNotFound is raised. Defaults to [].
        editor_usernames (str):
            A list of usernames to be invited as editors to the new garden.
            Usernames must exist or EntityNotFound is raised. Defaults to [].
        viewer_usernames (str):
            A list of usernames to be invited as viewers to the new garden.
            Usernames must exist or EntityNotFound is raised. Defaults to [].
        visibility (VisibilityEnum): The visibilty to set on the Garden. Defaults to VisibilityEnum.PRIVATE.
    """

    name: str
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    description: str = ""
    admin_usernames: list[str] = field(default_factory=list)
    editor_usernames: list[str] = field(default_factory=list)
    viewer_usernames: list[str] = field(default_factory=list)

    async def sanitize(self, garden_sanitizer: GardenSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            garden_sanitizer (GardenSanitizer): garden object sanitizer.
        """
        sanitized_data = await garden_sanitizer.sanitize(
            input_data={"name": self.name, "description": self.description},
            spec_select={
                "name": [specs.LENGTH, specs.REGEX, specs.BAN],
                "description": [specs.LENGTH, specs.REGEX],
            },
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.name = sanitized_data["name"]
        self.description = sanitized_data["description"]
