# VerdanTech Source
from src.common.adapters.utils.spec_manager import (
    SpecCollection,
    SpecDescriptions,
    Specs,
    SpecValues,
    merge_spec_collections,
)

from .attributes import specs as attributes_specs

values: SpecValues = {
    "cultivar_name": {
        Specs.MIN_LENGTH: 3,
        Specs.MAX_LENGTH: 30,
        Specs.PATTERN: r"[0-9A-Za-z _-]+",
    },
    "cultivar_names": {
        Specs.MIN_LENGTH: 1,
        Specs.MAX_LENGTH: 10,
    },
    "cultivar_key": {
        Specs.MIN_LENGTH: 1,
        Specs.MAX_LENGTH: 6,
        Specs.PATTERN: r"[0-9A-Za-z]+",
    },
    "cultivar_scientific_name": {
        Specs.MAX_LENGTH: 60,
    },
    "cultivar_description": {
        Specs.MAX_LENGTH: 1400,
    },
    "cultivar_collection_name": {
        Specs.MIN_LENGTH: 3,
        Specs.MAX_LENGTH: 50,
        Specs.PATTERN: r"[0-9A-Za-z _-]+",
    },
    "cultivar_collection_description": {
        Specs.MAX_LENGTH: 1400,
    },
    "cultivar_collection_tag": {Specs.MAX_LENGTH: 150, Specs.PATTERN: r"[0-9A-Za-z ]+"},
    "cultivar_collection_tags": {Specs.MAX_LENGTH: 150},
}
descriptions: SpecDescriptions = {
    "cultivar_name": {
        Specs.MIN_LENGTH: f"Must be at least {values['cultivar_name'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_name'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters, spaces, hyphens, and underscores",
        "field": (
            "A common name of this plant species. "
            f"Must be between {values['cultivar_name'][Specs.MIN_LENGTH]} and {values['cultivar_name'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters, spaces, hyphens, and underscores."
        ),
    },
    "cultivar_names": {
        Specs.MIN_LENGTH: f"Must contain at least {values['cultivar_names'][Specs.MIN_LENGTH]} name",
        Specs.MAX_LENGTH: f"Must contain at most {values['cultivar_names'][Specs.MAX_LENGTH]} names",
        "field": (
            "A set of common names associated with this plant species. "
            f"Each name must be between {values['cultivar_name'][Specs.MIN_LENGTH]} and {values['cultivar_name'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters and spaces. "
            f"There must be at least {values['cultivar_names'][Specs.MIN_LENGTH]} name and a maximum of {values['cultivar_names'][Specs.MAX_LENGTH]} names"
        ),
    },
    "cultivar_key": {
        Specs.MIN_LENGTH: f"Must be at least {values['cultivar_key'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_key'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters",
        "field": (
            "A very short abbreviation for this plant species. "
            f"Must be between {values['cultivar_key'][Specs.MIN_LENGTH]} and {values['cultivar_key'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters."
        ),
    },
    "cultivar_scientific_name": {
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_scientific_name'][Specs.MAX_LENGTH]} characters",
        "field": (
            "The scientific name of this plant species. "
            f"Must be at most {values['cultivar_scientific_name'][Specs.MAX_LENGTH]} characters"
        ),
    },
    "cultivar_description": {
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_description'][Specs.MAX_LENGTH]} characters",
        "field": (
            "A description of this plant species. "
            f"Must be at most {values['cultivar_description'][Specs.MAX_LENGTH]} characters"
        ),
    },
    "cultivar_collection_name": {
        Specs.MIN_LENGTH: f"Must be at least {values['cultivar_collection_name'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_collection_name'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters, spaces, hyphens, and underscores",
        "field": (
            "The name of the collection. "
            f"Must be between {values['cultivar_collection_name'][Specs.MIN_LENGTH]} and {values['cultivar_collection_name'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters, spaces, hyphens, and underscores."
        ),
    },
    "cultivar_collection_description": {
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_collection_description'][Specs.MAX_LENGTH]} characters",
        "field": (
            "The description of the collection. "
            f"Must be at most {values['cultivar_collection_description'][Specs.MAX_LENGTH]} characters"
        ),
    },
    "cultivar_collection_visibility": {
        "field": (
            "Public collections may be viewed by anyone and are publicly searchable. "
            "Unlisted collections may be viewed by anyone with the link. "
            "Private collections may only be owned by the creator, or by those in the garden if it is located within one."
        )
    },
    "cultivar_collection_tag": {
        Specs.MAX_LENGTH: f"Must be at most {values['cultivar_collection_tag'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters and spaces",
        "field": (
            "A metadata tag. "
            f"Must be at most {values['cultivar_collection_tag'][Specs.MAX_LENGTH]} characters and contain only alphanumeric characters and spaces"
        ),
    },
    "cultivar_collection_tags": {
        Specs.MAX_LENGTH: f"Must contain at most {values['cultivar_collection_tags'][Specs.MAX_LENGTH]} tags",
        "field": (
            "A set of metadata tags. "
            f"Each tag must be at most {values['cultivar_collection_tag'][Specs.MAX_LENGTH]} characters and contain only alphanumeric characters and spaces. "
            f"There may be at most {values['cultivar_collection_tags'][Specs.MAX_LENGTH]} tags."
        ),
    },
}
specs = merge_spec_collections(
    "cultivar", [SpecCollection("cultivar", values, descriptions), attributes_specs]
)
