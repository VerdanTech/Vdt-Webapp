# VerdanTech Source
from src.common.adapters.utils.spec_manager import (
    SpecCollection,
    SpecDescriptions,
    Specs,
    SpecValues,
)

values: SpecValues = {
    "coordinate_x": {
        Specs.MAX: 1000,
    },
    "coordinate_y": {
        Specs.MAX: 1000,
    },
    "coordinate_z": {
        Specs.MAX: 1000,
    },
    "polygon_coordinates": {
        Specs.MIN: 3,
        Specs.MAX: 500,
    },
    "ellipse_width": {
        Specs.MAX: 1000,
    },
    "ellipse_height": {
        Specs.MAX: 1000,
    },
    "lines_coordinates": {
        Specs.MAX: 500,
    },
}
descriptions: SpecDescriptions = {
    "coordinate_x": {
        Specs.MAX: f"Must not be more than {values['coordinate_x'][Specs.MAX]} meters.",
        "field": (
            "The horizontal component of this coordinate in meters. "
            f"Must not be more than {values['coordinate_x'][Specs.MAX]} meters."
        ),
    },
    "coordinate_y": {
        Specs.MAX: f"Must not be more than {values['coordinate_y'][Specs.MAX]} meters.",
        "field": (
            "The vertical component of this coordinate in meters. "
            f"Must not be more than {values['coordinate_y'][Specs.MAX]} meters."
        ),
    },
    "coordinate_z": {
        Specs.MAX: f"Must not be more than {values['coordinate_z'][Specs.MAX]} meters.",
        "field": (
            "The depth component of this coordinate in meters. "
            f"Must not be more than {values['coordinate_z'][Specs.MAX]} meters."
        ),
    },
    "polygon_coordinates": {
        Specs.MIN: f"Must contain at least {values['polygon_coordinates'][Specs.MIN]} points and form a closed shape.",
        Specs.MAX: f"May contain a maximum of {values['polygon_coordinates'][Specs.MAX]} points.",
        "field": (
            "A list of points which form a clsoed polygonal shape. "
            f"Must contain at least {values['polygon_coordinates'][Specs.MIN]} points and form a closed shape. "
            f"May contain a maximum of {values['polygon_coordinates'][Specs.MAX]} points."
        ),
    },
    "ellipse_width": {
        Specs.MAX: "1000",
        "field": (
            "The depth component of this coordinate in meters. "
            f"Must not be more than {values['coordinate_z'][Specs.MAX]} meters."
        ),
    },
    "ellipse_height": {
        Specs.MAX: "1000",
        "field": (
            "The depth component of this coordinate in meters. "
            f"Must not be more than {values['coordinate_z'][Specs.MAX]} meters."
        ),
    },
    "lines_coordinates": {
        Specs.MAX: "500",
        "field": (
            "The depth component of this coordinate in meters. "
            f"Must not be more than {values['coordinate_z'][Specs.MAX]} meters."
        ),
    },
}
specs = SpecCollection("geometry", values, descriptions)
