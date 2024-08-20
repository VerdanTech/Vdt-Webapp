# VerdanTech Source
from src.common.adapters.utils.spec_manager import (
    SpecCollection,
    SpecDescriptions,
    Specs,
    SpecValues,
)

values: SpecValues = {
    "garden_name": {
        Specs.MIN_LENGTH: 2,
        Specs.MAX_LENGTH: 50,
        Specs.PATTERN: r"[0-9A-Za-z ]+",
    },
    "garden_key": {
        Specs.MIN_LENGTH: 4,
        Specs.MAX_LENGTH: 16,
        Specs.PATTERN: r"[0-9A-Za-z-]+",
    },
    "garden_description": {
        Specs.MAX_LENGTH: 1400,
    },
    "user_invites_list": {
        Specs.MAX_LENGTH: 10,
    },
}
descriptions: SpecDescriptions = {
    "garden_name": {
        Specs.MIN_LENGTH: f"Must be at least {values['garden_name'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['garden_name'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters and spaces",
        "field": f"Must be between {values['garden_name'][Specs.MIN_LENGTH]} and {values['garden_name'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters and spaces",
    },
    "garden_key": {
        Specs.MIN_LENGTH: f"Must be at least {values['garden_key'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['garden_key'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters and hyphens",
        "field": f"Must be between {values['garden_key'][Specs.MIN_LENGTH]} and {values['garden_key'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters and hyphens",
    },
    "garden_description": {
        Specs.MAX_LENGTH: f"Must be at most {values['garden_description'][Specs.MAX_LENGTH]} characters",
        "field": f"Must be at most {values['garden_description'][Specs.MAX_LENGTH]} characters",
    },
    "user_invites_list": {
        Specs.MAX_LENGTH: f"A maximum of {values['user_invites_list'][Specs.MAX_LENGTH]} users can be invited at once",
        "field": f"A maximum of {values['user_invites_list'][Specs.MAX_LENGTH]} users can be invited at once",
    },
}
specs = SpecCollection("garden", values, descriptions)
