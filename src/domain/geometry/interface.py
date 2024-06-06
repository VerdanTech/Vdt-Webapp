# Standard Library
from enum import Enum
from typing import Protocol


class GeometryTypeEnum(Enum):
    POLYGON = "polygon"
    LINES = "lines"
    ELLIPSE = "ellipse"


class Coordinate(Protocol):
    @property
    def x(self) -> float:
        """
        Returns:
            float: the horizontal x coordinate in meters (m).
        """
        ...

    @property
    def y(self) -> float:
        """
        Returns:
            float: the vertical y coordinate in meters (m).
        """
        ...


class Geometry(Protocol):
    name: GeometryTypeEnum
    """Geometry identifier"""

    @property
    def points(self) -> set[Coordinate]:
        """
        Returns:
            set[Coordinate]: the coordinates which make up
                the vertices of the geometry relative to
                the position attribute.
        """
        ...

    @property
    def points_absolute(self) -> set[Coordinate]:
        """
        Returns:
            set[Coordinate]: the coordinates which make up
                the vertices of the geometry relative to
                the origin.
        """
        ...

    @property
    def area(self) -> float:
        """
        Returns:
            float: the area of the geometry in meters squared (m^2).
        """
        ...

    @property
    def perimeter(self) -> float:
        """
        Returns:
            float: the length of the perimeter of the geometry in meters (m).
        """
        ...

    def translate(self, x: float, y: float) -> "Geometry":
        """
        Translate the geometry's position.

        Args:
            x (float): the horizontal x distance to move the geometry's position by in meters (m).
            y (float): the vertical y distance to move the geometry's position by in meters (m).

        Returns:
            Geometry: the translated geometry.
        """
        ...

    def distance_center(self, other: "Geometry") -> float:
        """
        Calculates the distance between self's position attribute
        and another geometry's position attribute.

        Args:
            other (Geometry): the geometry to compare with.

        Returns:
            float: the distance between the centers of the two geometries in meters (m).
        """
        ...

    def distance_boundary(self, other: "Geometry") -> float:
        """
        Calculates the distance between self's boundary
        and another geometry's boundary.

        Args:
            other (Geometry): the geometry to compare with.

        Returns:
            float: the distance between the bounded areas of the two geometries in meters (m).
        """
        ...

    def intersect(self, other: "Geometry", fuzz: float = 0) -> bool:
        """
        Calculates the intersection of two geometries.

        Args:
            other (Geometry): the geometry to compare with.
            fuzz (float, range[0-1]): the portion of the larger geometry
                that is allowed to intersect with the smaller geometry
                while False is still returned.

        Returns:
            bool: True if the overlap of the geometries is zero or less than
                a percentage of the larger geometry's area equal to fuzz.
        """
        ...

    def validate(self) -> bool:
        """
        Validates the integrity of the geometry.

        Returns:
            bool: True if the geometry is valid.
        """
        ...

    @classmethod
    def from_points(
        cls, position: Coordinate, points: set[Coordinate]
    ) -> "Geometry | None":
        """
        Constructs an instance of the geometry from a set of coordinates
        relative to the supplied position.

        Args:
            position (Coordinate): the point to construct the geometry around.
            points (set[Coordinate]): the points to use to construct the geometry.

        Returns:
            Geometry: the constructed geometry, or None if the supplied
                inputs were invalid.
        """
        ...

    @classmethod
    def from_points_absolute(cls, points: set[Coordinate]) -> "Geometry":
        """
        Constructs an instance of the geometry from a set of coordinates
        relative to the origin.

        Args:
            points (set[Coordinate]): the points to use to construct the geometry.

        Returns:
            Geometry: the constructed geometry, or None if the supplied
                inputs were invalid.
        """
        ...


class Polygon(Geometry, Protocol):
    name = GeometryTypeEnum.POLYGON


class Lines(Geometry, Protocol):
    name = GeometryTypeEnum.LINES


class Ellipse(Geometry, Protocol):
    name = GeometryTypeEnum.ELLIPSE
