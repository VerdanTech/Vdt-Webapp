# Standard Library
from typing import Annotated

# External Libraries
from pydantic import AfterValidator, Field

# VerdanTech Source
from src.common.adapters.utils.spec_manager import SpecCollection, SpecManager, Specs
from src.common.domain import Command, value_transform

from .profile import CultivarAttributeProfile

values = {
    "seed_to_germ": {Specs.MIN: 0, Specs.MAX: 60},
    "germ_to_transplant": {Specs.MIN: 0, Specs.MAX: 200},
    "germ_to_first_harvest": {Specs.MIN: 0, Specs.MAX: 200},
    "first_to_last_harvest": {Specs.MIN: 0, Specs.MAX: 120},
}
descriptions = {
    "annual_lifecycle_profile": {
        "field": (
            "The annual lifecycle defines the length of the stages of life for annual plants."
        ),
        "label": "Annual Lifecycle Profile",
    },
    "seed_to_germ": {
        Specs.MIN: f"Must be greater than {values['seed_to_germ'][Specs.MIN]}",
        Specs.MAX: f"Must be less than {values['seed_to_germ'][Specs.MAX]}",
        "field": (
            "The expected amount of days from starting a seed to its germination. "
            f"Must be between {values['seed_to_germ'][Specs.MIN]} and {values['seed_to_germ'][Specs.MAX]} days."
        ),
        "label": "Seed to Germination Duration",
    },
    "germ_to_transplant": {
        Specs.MIN: f"Must be greater than {values['germ_to_transplant'][Specs.MIN]}",
        Specs.MAX: f"Must be less than {values['germ_to_transplant'][Specs.MAX]}",
        "field": (
            "The expected amount of days from the germination of a seed to when it will be ready for transplant. "
            "For cultivars which are not able to be transplanted, this value is unused. "
            f"Must be between {values['germ_to_transplant'][Specs.MIN]} and {values['germ_to_transplant'][Specs.MAX]} days."
        ),
        "label": "Germination to Transplant Duration",
    },
    "germ_to_first_harvest": {
        Specs.MIN: f"Must be greater than {values['germ_to_first_harvest'][Specs.MIN]}",
        Specs.MAX: f"Must be less than {values['germ_to_first_harvest'][Specs.MAX]}",
        "field": (
            "The expected amount of days the germination of a seed to when it will be ready for a harvest. "
            f"Must be between {values['germ_to_first_harvest'][Specs.MIN]} and {values['germ_to_first_harvest'][Specs.MAX]} days."
        ),
        "label": "Germination to Harvest Duration",
    },
    "first_to_last_harvest": {
        Specs.MIN: f"Must be greater than {values['first_to_last_harvest'][Specs.MIN]}",
        Specs.MAX: f"Must be less than {values['first_to_last_harvest'][Specs.MAX]}",
        "field": (
            "The expected amount of days the first and last harvest of a plant. "
            "For plants which only have one harvest, this values is zero. "
            f"Must be between {values['first_to_last_harvest'][Specs.MIN]} and {values['first_to_last_harvest'][Specs.MAX]} days."
        ),
        "label": "First to Last Harvest Duration",
    },
}
annual_lifecycle_specs = SpecCollection(
    "annual_lifecycle_profile", values, descriptions
)


@value_transform
class AnnualLifecycleProfile(CultivarAttributeProfile):
    seed_to_germ: float | None = None
    germ_to_transplant: float | None = None
    germ_to_first_harvest: float | None = None
    first_to_last_harvest: float | None = None


SeedToGerm = Annotated[
    float,
    AfterValidator(
        SpecManager.get_validation_method(annual_lifecycle_specs, "seed_to_germ")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=descriptions["seed_to_germ"]["field"],
        json_schema_extra={
            "min": values["seed_to_germ"][Specs.MIN],
            "max": values["seed_to_germ"][Specs.MAX],
        },
    ),
]
GermToTransplant = Annotated[
    float,
    AfterValidator(
        SpecManager.get_validation_method(annual_lifecycle_specs, "germ_to_transplant")
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=descriptions["germ_to_transplant"]["field"],
        json_schema_extra={
            "min": values["germ_to_transplant"][Specs.MIN],
            "max": values["germ_to_transplant"][Specs.MAX],
        },
    ),
]
GermToFirstHarvest = Annotated[
    float,
    AfterValidator(
        SpecManager.get_validation_method(
            annual_lifecycle_specs, "germ_to_first_harvest"
        )
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=descriptions["germ_to_first_harvest"]["field"],
        json_schema_extra={
            "min": values["germ_to_first_harvest"][Specs.MIN],
            "max": values["germ_to_first_harvest"][Specs.MAX],
        },
    ),
]
FirstToLastHarvest = Annotated[
    float,
    AfterValidator(
        SpecManager.get_validation_method(
            annual_lifecycle_specs, "first_to_last_harvest"
        )
    ),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=descriptions["first_to_last_harvest"]["field"],
        json_schema_extra={
            "min": values["first_to_last_harvest"][Specs.MIN],
            "max": values["first_to_last_harvest"][Specs.MAX],
        },
    ),
]


class AnnualLifecycleProfileUpdateCommand(Command):
    seed_to_germ: SeedToGerm | None = None
    germ_to_transplant: GermToTransplant | None = None
    germ_to_first_harvest: GermToFirstHarvest | None = None
    first_to_last_harvest: FirstToLastHarvest | None = None
