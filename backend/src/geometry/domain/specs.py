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
    "rectangle_width": {
        Specs.MAX: 1000,
    },
    "rectangle_height": {
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
    "rectangle_width": {
        Specs.MAX: f"Must not be more than {values['rectangle_width'][Specs.MAX]} meters.",
        "field": (
            "The width of the rectangular geometry in meters. "
            f"Must not be more than {values['rectangle_width'][Specs.MAX]} meters."
        ),
    },
    "rectangle_height": {
        Specs.MAX: f"Must not be more than {values['rectangle_height'][Specs.MAX]} meters.",
        "field": (
            "The height of the rectangular geometry in meters. "
            "If set to null, the width value will be used instead. "
            f"Must not be more than {values['rectangle_height'][Specs.MAX]} meters."
        ),
    },
    "polygon_coordinates": {
        Specs.MIN: f"Must contain at least {values['polygon_coordinates'][Specs.MIN]} points and form a closed shape.",
        Specs.MAX: f"May contain a maximum of {values['polygon_coordinates'][Specs.MAX]} points.",
        "field": (
            "A list of points which form a closed polygonal shape. "
            f"Must contain at least {values['polygon_coordinates'][Specs.MIN]} points and form a closed shape. "
            f"May contain a maximum of {values['polygon_coordinates'][Specs.MAX]} points."
        ),
    },
    "ellipse_width": {
        Specs.MAX: f"Must not be more than {values['ellipse_width'][Specs.MAX]} meters.",
        "field": (
            "The width of the ellpse shape in meters. "
            f"Must not be more than {values['ellipse_width'][Specs.MAX]} meters."
        ),
    },
    "ellipse_height": {
        Specs.MAX: f"Must not be more than {values['ellipse_height'][Specs.MAX]} meters.",
        "field": (
            "The height of the ellipse shape in meters. "
            "If set to null, the width value will be used instead. "
            f"Must not be more than {values['ellipse_height'][Specs.MAX]} meters."
        ),
    },
    "lines_coordinates": {
        Specs.MAX: f"May contain a maximum of {values['lines_coordinates'][Specs.MAX]} points.",
        "field": (
            "A list of points whihch form a segmented line. May be unclosed. "
            f"May contain a maximum of {values['lines_coordinates'][Specs.MAX]} points."
        ),
    },
}
specs = SpecCollection("geometry", values, descriptions)

