# VerdanTech Source
from src.common.adapters.utils.spec_manager import (
    SpecCollection,
    SpecDescriptions,
    Specs,
    SpecValues,
)

values: SpecValues = {
    "workspace_name": {
        Specs.MIN_LENGTH: 3,
        Specs.MAX_LENGTH: 30,
        Specs.PATTERN: r"[0-9A-Za-z _-]+",
    },
    "workspace_description": {
        Specs.MAX_LENGTH: 700,
    },
    "workspace_planting_areas": {
        Specs.MAX: 100,
    },
    "planting_area_name": {
        Specs.MIN_LENGTH: 3,
        Specs.MAX_LENGTH: 30,
        Specs.PATTERN: r"[0-9A-Za-z _-]+",
    },
    "planting_area_description": {
        Specs.MAX_LENGTH: 700,
    },
}
descriptions: SpecDescriptions = {
    "workspace_name": {
        Specs.MIN_LENGTH: f"Must be at least {values['workspace_name'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['workspace_name'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters, spaces, hyphens, and underscores",
        "field": (
            "A descriptive name for this workspace. "
            f"Must be between {values['workspace_name'][Specs.MIN_LENGTH]} and {values['workspace_name'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters, spaces, hyphens, and underscores."
        ),
    },
    "workspace_description": {
        Specs.MAX_LENGTH: f"Must be at most {values['workspace_description'][Specs.MAX_LENGTH]} characters",
        "field": (
            "A description of this workspace. "
            f"Must be at most {values['workspace_description'][Specs.MAX_LENGTH]} characters"
        ),
    },
    "workspace_planting_areas": {
        Specs.MAX: f"Must contain at most {values['workspace_planting_areas'][Specs.MAX]} planting areas.",
        "field": (
            "The planting areas contained within this workspace. "
            "Planting areas describe an area in a workspace where plants may be placed. "
            f"May not contain more than {values['workspace_planting_areas'][Specs.MAX]} planting areas in a workplace."
        ),
    },
    "planting_area_name": {
        Specs.MIN_LENGTH: f"Must be at least {values['planting_area_name'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['planting_area_name'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters, spaces, hyphens, and underscores",
        "field": (
            "A descriptive name for this planting area. "
            f"Must be between {values['planting_area_name'][Specs.MIN_LENGTH]} and {values['planting_area_name'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters, spaces, hyphens, and underscores."
        ),
    },
    "planting_area_description": {
        Specs.MAX_LENGTH: f"Must be at most {values['planting_area_description'][Specs.MAX_LENGTH]} characters",
        "field": (
            "A description of this planting area. "
            f"Must be at most {values['planting_area_description'][Specs.MAX_LENGTH]} characters"
        ),
    },
}
specs = SpecCollection("workspace", values, descriptions)
