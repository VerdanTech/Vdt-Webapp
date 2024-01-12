# Standard Library
from enum import Enum


class GroupErrorsByEnum(Enum):
    """
    Enumerated options for grouping errors.

    OBJECT: An ObjectSanitizer will group together the errors
        returned by the FieldSanitizers, and raise them together
        after all FieldSanitizers have been run. FieldSanitizers and
        Sanitizations will return rather than raise errors.
    FIELD: A FieldSanitizer will group together the errors returned
        by the Sanitizions, and raise them together after all Sanitizations
        have been run. Sanitizations will return rather than raise errors.
    SPEC: A Spec will raise an exception and return no error.
        No errors will be grouped together, and Specs will be run until one
        fails to sanitize.
    """

    OBJECT = 0
    FIELD = 1
    SPEC = 2


class SelectEnum(Enum):
    """
    Enumerated aliases for selecting Sanitizations.

    Options that are specific to a Sanitization type correspond
    to the id attribute defined on that type.
    """

    # Options that aren't specific to a Sanitization type.
    ENABLE_ALL = "enable_all"
    DISABLE_ALL = "disable_all"

    # Basic sanitizations.
    LENGTH = "length"
    SIZE = "size"
    REGEX = "regex"
    BAN = "ban"

    # Repo sanitizations.
    UNIQUE = "unique"
    EXISTS = "exists"

    # Custom sanitizations.
    EMAIL = "email"
