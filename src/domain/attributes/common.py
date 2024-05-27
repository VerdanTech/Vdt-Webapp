# Standard Library
from enum import Enum

# VerdanTech Source
from src.domain.common import DomainModel, Value


class AttributeProfile[Parent: DomainModel](Value):
    """
    Represents a generic group of attributes.

    Characterized by a type of domain model "Parent"
    which is the type of model the information is attached to.
    """

    id: Enum
    """A value of an Enum which contains all possible subtypes of a subtype of AttributeCluster."""

    def sanitize(self) -> None:
        """
        Validates and normalizes attributes.

        Raises:
            SpecError: if the attributes fail validation.
        """
        return


class AttributeCluster[Profile: AttributeProfile](Value):
    """
    Acts as a container for a set of attribute profiles.

    Attribute profiles are declared as optional class members.
    The names of these members must be the same as the id attribute on the profile.
    """

    pass
