# Standard Library
import re

# External Libraries
from dns.resolver import Resolver
from svcs import Container

# VerdanTech Source
from src import settings
from src.domain.garden.sanitizers import GardenSanitizer, GardenSanitizerConfig
from src.interfaces.persistence.garden.repository import AbstractGardenRepository
from src.utils import sanitizers

banned_names = []
with open(settings.static_path("banned_fields/garden_names.txt"), "r") as file:
    for line in file:
        # Strip any leading/trailing whitespace including newline characters
        name = line.strip()
        # Add the username to the list
        banned_names.append(name)


async def provide_garden_sanitizer(svcs_container: Container) -> GardenSanitizer:
    """Configure and return a garden sanitizer with application settings for dependency injection."""
    garden_repo = await svcs_container.aget_abstract(AbstractGardenRepository)
