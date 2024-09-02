# Standard Library
import uuid
from typing import Annotated

# External Libraries
from pydantic import AfterValidator, BeforeValidator, Field

# VerdanTech Source
from src import settings
from src.common.adapters.utils.spec_manager import SpecManager, Specs
from src.common.domain import Command

from .attributes import CultivarAttributeUpdateCommand
from .enums import CultivarCollectionVisibilityEnum
from .specs import specs

# Load all banned cultivar names and keys
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())

# ======================================
# Fields
# ======================================

CultivarName = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "cultivar_name")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_name"]["field"],
        json_schema_extra={
            "min_length": specs.values["cultivar_name"][Specs.MIN_LENGTH],
            "max_length": specs.values["cultivar_name"][Specs.MAX_LENGTH],
            "pattern": specs.values["cultivar_name"][Specs.PATTERN],
        },
    ),
]
CultivarNames = Annotated[
    list[CultivarName],
    AfterValidator(SpecManager.get_validation_method(specs, "cultivar_names")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_names"]["field"],
        json_schema_extra={
            "max_length": specs.values["cultivar_names"][Specs.MAX_LENGTH],
        },
    ),
]
CultivarKey = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "cultivar_key")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_key"]["field"],
        json_schema_extra={
            "min_length": specs.values["cultivar_key"][Specs.MIN_LENGTH],
            "max_length": specs.values["cultivar_key"][Specs.MAX_LENGTH],
            "pattern": specs.values["cultivar_key"][Specs.PATTERN],
        },
    ),
]
CultivarScientificName = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(
        SpecManager.get_validation_method(specs, "cultivar_scientific_name")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_scientific_name"]["field"],
        json_schema_extra={
            "max_length": specs.values["cultivar_scientific_name"][Specs.MAX_LENGTH],
        },
    ),
]
CultivarDescription = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "cultivar_description")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_description"]["field"],
        json_schema_extra={
            "max_length": specs.values["cultivar_description"][Specs.MAX_LENGTH],
        },
    ),
]
CultivarCollectionName = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(
        SpecManager.get_validation_method(specs, "cultivar_collection_name")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_collection_name"]["field"],
        json_schema_extra={
            "min_length": specs.values["cultivar_collection_name"][Specs.MIN_LENGTH],
            "max_length": specs.values["cultivar_collection_name"][Specs.MAX_LENGTH],
            "pattern": specs.values["cultivar_collection_name"][Specs.PATTERN],
        },
    ),
]
CultivarCollectionDescription = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(
        SpecManager.get_validation_method(specs, "cultivar_collection_description")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_collection_description"]["field"],
        json_schema_extra={
            "max_length": specs.values["cultivar_collection_description"][
                Specs.MAX_LENGTH
            ],
        },
    ),
]
CultivarCollectionTag = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "cultivar_collection_tag")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_collection_tag"]["field"],
        json_schema_extra={
            "max_length": specs.values["cultivar_collection_tag"][Specs.MAX_LENGTH],
            "pattern": specs.values["cultivar_collection_tag"][Specs.PATTERN],
        },
    ),
]
CultivarCollectionTags = Annotated[
    set[CultivarCollectionTag],
    AfterValidator(
        SpecManager.get_validation_method(specs, "cultivar_collection_tags")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["cultivar_collection_tags"]["field"],
        json_schema_extra={
            "max_length": specs.values["cultivar_collection_tags"][Specs.MAX_LENGTH],
        },
    ),
]

# ======================================
# Commands
# ======================================


class CultivarCreateCommand(Command):
    """
    Creates a new Cultivar in a CultivarCollection.

    Attributes:
        They follow the same structure as the Cultivar model.
    """

    collection_ref: uuid.UUID
    names: CultivarNames
    key: CultivarKey | None = None
    scientific_name: CultivarScientificName | None = None
    description: CultivarDescription | None = None
    parent_id: uuid.UUID | None = None


class CultivarUpdateCommand(Command):
    """
    Updates an existing Cultivar in a CultivarCollection.
    """

    collection_ref: uuid.UUID
    cultivar_id: uuid.UUID
    names: CultivarNames | None = None
    key: CultivarKey | None = None
    scientific_name: CultivarScientificName | None = None
    description: CultivarDescription | None = None
    parent_id: uuid.UUID | None = None
    remove_parent: bool = False
    """If true, the parent_ref will be deleted regardless of the update value."""
    attributes: CultivarAttributeUpdateCommand | None = None


class CultivarDeleteCommand(Command):
    """
    Deletes a Cultivar from a CultivarCollection.
    """

    collection_ref: uuid.UUID
    cultivar_id: uuid.UUID


class CultivarCollectionCreateCommand(Command):
    """
    Creates a new Cultivar Collection.
    """

    name: CultivarCollectionName
    visibility: CultivarCollectionVisibilityEnum = (
        CultivarCollectionVisibilityEnum.PRIVATE
    )
    description: CultivarCollectionDescription = ""
    tags: CultivarCollectionTags = set()
    parent_ref: uuid.UUID | None = None
    garden_ref: uuid.UUID | None = None


class CultivarCollectionUpdateCommand(Command):
    """
    Updates an existing Cultivar Collection.
    """

    collection_ref: uuid.UUID
    name: CultivarCollectionName | None = None
    visibility: CultivarCollectionVisibilityEnum | None = None
    description: CultivarCollectionDescription | None = None
    tags: CultivarCollectionTags | None = None
    parent_ref: uuid.UUID | None = None
    remove_parent: bool = False
    """If true, the parent_ref will be deleted regardless of the update value."""


class CultivarCollectionDeleteCommand(Command):
    """
    Deletes a Cultivar Collection.
    """

    collection_ref: uuid.UUID


class CultivarCollectionDuplicateCommand(Command):
    """
    Given an existing Cultivar Collection, creates
    a new one with the same data.
    """

    source_collection_ref: uuid.UUID
    garden_ref: uuid.UUID | None = None


class CultivarCollectionMergeCommand(Command):
    """
    Given an existing Cultivar Collection, updates it
    with the data from another collection.
    """

    target_collection_ref: uuid.UUID
    source_collection_ref: uuid.UUID
