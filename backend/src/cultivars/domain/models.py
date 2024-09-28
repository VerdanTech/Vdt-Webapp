# Standard Library
import uuid

# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import (
    Entity,
    Ref,
    RootEntity,
    entity_transform,
    root_entity_transform,
)
from src.garden.domain import Garden
from src.user.domain import User

from .attributes import CultivarAttributeSet
from .enums import CultivarCollectionVisibilityEnum


@entity_transform
class Cultivar(Entity):
    """
    Represents a species/variety of plant.

    Attributes:
        name (list[str]): the common names of the plant.
            Example: ["Zucchini", "Summer Squash", "Courgette"]
        key (str) a short, few character representation.
            Used for visual representation of plants
            when simple circular shapes are used.
            Example: "Le"
        scientific_name (str): an optional scientific name.
            Example: "Solanum lycopersicum"
        description (str): an optional description.
        _attributes (CultivarAttributeSet): the attribute data
            describing the behavior of the plant.
        parent_id (UUID | None): an optional ID referring to a Cultivar
            contained in the same CultivarCollection. If included,
            the cultivar's properties will be inherited from
            the parent, and the new data will be overlaid.
    """

    names: list[str]  # type: ignore
    key: str  # type: ignore
    scientific_name: str = ""  # type: ignore
    description: str = ""
    _attributes: CultivarAttributeSet = CultivarAttributeSet()
    parent_id: uuid.UUID | None = None

    @property
    def name(self) -> str:
        """
        Returns a single name for purposes of labelling.
        """
        return self.names[0] or ""

    @property
    def attributes(self) -> CultivarAttributeSet:
        return self._attributes


@root_entity_transform
class CultivarCollection(RootEntity):
    """
    Contains a set of related Cultivars for use by a Garden.
    Allows inherticance and duplication/re-use.

    Attributes:
        name (str): the name of the collection.
            Example: "West Coast Seeds"
        slug (str): a unique, URL-friendly version of the name.
            Example: "west-coast-seeds-11"
        visibility (CultivarCollectionVisibilityEnum):
            the visibility of the CultivarCollection.
            If owned by a user, the PRIVATE setting will allow
            only that user to access the collection. If owned by
            a garden, the PRIVATE setting will allow only those with
            read-access to the garden access.
        description (str): an optional description.
        tags (set[str]): an optional list of metadata.
        _cultivars (set[Cultivars]): the cultivars in the collection.
        parent_ref (Ref[CultivarCollection]): an optional ID referring
            to another collection If included, the collection's cultivars
            will be inherited from the parent, and the new data will be overlaid.
        user_ref (Ref[User]): an optional reference to a User. For collections
            which were created outside of the context of a Garden, this
            field will refer to the creator. If no garden is referenced,
            this user is considered to own the collection.
        garden_ref (Ref[Garden]): an optional reference to a Garden.
            For collections which were created inside the context of
            a garden, this field will refer to that garden. The garden
            is consideres the owner of the collection regardless of whether
            user_ref is defined.
    """

    name: str  # type: ignore
    slug: str  # type: ignore
    visibility: CultivarCollectionVisibilityEnum = (
        CultivarCollectionVisibilityEnum.PRIVATE
    )
    description: str = ""
    tags: set[str] = field(factory=set)
    _cultivars: set[Cultivar] = field(factory=set)
    parent_ref: Ref["CultivarCollection"] | None = None
    user_ref: Ref[User] | None = None
    garden_ref: Ref[Garden] | None = None

    @property
    def cultivars(self) -> set[Cultivar]:
        return self._cultivars
