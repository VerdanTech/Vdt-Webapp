# Standard Library
import uuid
from typing import Annotated

# External Libraries
from pydantic import AfterValidator, BeforeValidator, Field

# VerdanTech Source
from src import settings
from src.common.adapters.utils.spec_manager import SpecManager, Specs
from src.common.domain import Command
from src.garden.domain.commands import GardenKey

from .specs import specs

# Load all banned workspace names
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())

# ======================================
# Fields
# ======================================

WorkspaceName = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "workspace_name")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["workspace_name"]["field"],
        json_schema_extra={
            "min_length": specs.values["workspace_name"][Specs.MIN_LENGTH],
            "max_length": specs.values["workspace_name"][Specs.MAX_LENGTH],
            "pattern": specs.values["workspace_name"][Specs.PATTERN],
        },
    ),
]
WorkspaceDescription = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "workspace_description")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["workspace_description"]["field"],
        json_schema_extra={
            "max_length": specs.values["workspace_description"][Specs.MAX_LENGTH],
        },
    ),
]
PlantingAreaName = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "planting_area_name")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["planting_area_name"]["field"],
        json_schema_extra={
            "min_length": specs.values["planting_area_name"][Specs.MIN_LENGTH],
            "max_length": specs.values["planting_area_name"][Specs.MAX_LENGTH],
            "pattern": specs.values["planting_area_name"][Specs.PATTERN],
        },
    ),
]
PlantingAreaDescription = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(
        SpecManager.get_validation_method(specs, "planting_area_description")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["planting_area_description"]["field"],
        json_schema_extra={
            "max_length": specs.values["planting_area_description"][Specs.MAX_LENGTH],
        },
    ),
]

# ======================================
# Commands
# ======================================


class WorkspaceCreateCommand(Command):
    """
    Creates a new workspace.
    """

    garden_key: GardenKey
    name: WorkspaceName
    description: WorkspaceDescription | None = None


class WorkspaceUpdateCommand(Command):
    """
    Updates a workspace.
    """

    workspace_ref: uuid.UUID
    name: WorkspaceName | None = None
    description: WorkspaceDescription | None = None


class WorkspaceDeleteCommand(Command):
    """
    Deletes a workspace.
    """

    workspace_ref: uuid.UUID


class PlantingAreaCreateCommand(Command):
    """
    Creates a new planting area on a workspace
    """

    workspace_ref: uuid.UUID
    name: PlantingAreaName
    description: PlantingAreaDescription | None = None


class PlantingAreaUpdateCommand(Command):
    """
    Updates a planting area.
    """

    workspace_ref: uuid.UUID
    planting_area_id: uuid.UUID
    name: PlantingAreaName | None = None
    description: PlantingAreaDescription | None = None


class PlantingAreaDeleteCommand(Command):
    """
    Deletes a planting area.
    """

    workspace_ref: uuid.UUID
    planting_area_id: uuid.UUID
