# VerdanTech Source
from src.common.adapters.utils.spec_manager import (
    SpecCollection,
    SpecDescriptions,
    Specs,
    SpecValues,
)

values: SpecValues = {
    "username": {
        Specs.MIN_LENGTH: 3,
        Specs.MAX_LENGTH: 50,
        Specs.PATTERN: r"^[a-zA-Z0-9_]*$",
    },
    "password": {
        Specs.MIN_LENGTH: 6,
        Specs.MAX_LENGTH: 255,
        Specs.PATTERN: r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W).*$",
    },
}
descriptions: SpecDescriptions = {
    "username": {
        Specs.MIN_LENGTH: f"Must be at least {values['username'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['username'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain only alphanumeric characters and underscores",
        "field": f"Must be between {values['username'][Specs.MIN_LENGTH]} and {values['username'][Specs.MAX_LENGTH]} characters long and contain only alphanumeric characters and underscores. Must be unique.",
    },
    "password": {
        Specs.MIN_LENGTH: f"Must be at least {values['password'][Specs.MIN_LENGTH]} characters",
        Specs.MAX_LENGTH: f"Must be at most {values['password'][Specs.MAX_LENGTH]} characters",
        Specs.PATTERN: "Must contain at least one lowercase letter, one uppercase letter, one digit, and one special character",
        "field": f"Must be between {values['password'][Specs.MIN_LENGTH]} and {values['password'][Specs.MAX_LENGTH]} characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character",
    },
}
specs = SpecCollection("user", values, descriptions)