# Standard Library
from typing import Annotated

# External Libraries
from pydantic import AfterValidator, Field

# VerdanTech Source
from src.attributes.domain import AttributeProfile
from src.common.adapters.utils.spec_manager import SpecCollection, SpecManager, Specs
from src.common.domain import Command, value_transform

type LastFrostWindowOpenType = float
type LastFrostWindowCloseType = float
type FirstFrostWindowOpenType = float
type FirstFrostWindowCloseType = float

values = {"last_frost_window_open": {Specs.MIN: -200, Specs.MAX: 200}}
descriptions = {
    "frost_date_planting_window_profile": {
        "field": (
            "A planting window defines a period of time within an environment that a cultivar should be planted. "
            "These attributes define an allowed planting window of time relative to the first and last frost dates."
        ),
        "label": "Frost Date Planting Window Profile",
    },
    "last_frost_window_open": {
        Specs.MIN: f"Must be greater than {values['last_frost_window_open'][Specs.MIN]}",
        Specs.MIN: f"Must be less than {values['last_frost_window_open'][Specs.MAX]}",
        "field": (
            "The amount of days between the last frost and the beginning of the planting window. "
            "Positive values indicate the window begins after the last frost date."
            "For example, a value of -15 indicates the cultivar may be planted 15 days before the last frost date."
            f"Must be between {values['last_frost_window_open'][Specs.MIN]} and {values['last_frost_window_open'][Specs.MIN]} days long."
        ),
        "label": "Last Frost Window - Open",
        "unit": "days",
    },
}
specs = SpecCollection("frost_date_planting_window_profile", values, descriptions)


@value_transform
class FrostDatePlantingWindowProfile(AttributeProfile):
    last_frost_window_open: LastFrostWindowOpenType | None
    last_frost_window_close: LastFrostWindowCloseType | None
    first_frost_window_open: FirstFrostWindowOpenType | None
    first_frost_window_close: FirstFrostWindowCloseType | None


class FrostDatePlantingWindowProfileUpdateCommand(Command):
    last_frost_window_open: Annotated[
        LastFrostWindowOpenType,
        AfterValidator(
            SpecManager.get_validation_method(specs, "last_frost_window_open")
        ),
        # Note: Field used only for annotation, to allow custom error messages.
        Field(
            description=descriptions["last_frost_window_open"]["field"],
            json_schema_extra={
                "min": values["last_frost_window_open"][Specs.MIN],
                "max": values["last_frost_window_open"][Specs.MAX],
            },
        ),
    ] | None
