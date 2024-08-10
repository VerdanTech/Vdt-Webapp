# Standard Library
import os
import re
from collections import namedtuple
from enum import Enum, auto
from typing import Any, Callable, Generator, Literal

# External Libraries
from pydantic import SecretStr

"""
Contains utilities for composing validation with custom error messages.
"""


class Specs(Enum):
    """
    Different types of validations / specifications.
    """

    TYPE = "type"
    MIN_LENGTH = "min_length"
    MAX_LENGTH = "max_length"
    PATTERN = "pattern"


type Field = str
"""Name of a field on an object to validate."""
type SpecValues = dict[Field, dict[Specs, Any]]
"""Contains the values the field is validated against."""
type SpecDescriptions = dict[Field, dict[Specs | Literal["field"], str]]
"""Contains the error message descriptions."""

SpecCollection = namedtuple("SpecCollection", ["domain", "values", "descriptions"])


def validate_pattern(value: str | SecretStr, pattern: str | re.Pattern) -> bool:
    """
    Validate a string against a pattern.

    Returns:
        _type_: _description_
    """
    if isinstance(value, SecretStr):
        return bool(re.match(pattern, value.get_secret_value()))
    elif isinstance(value, str):
        return bool(re.match(pattern, value))


"""Validation methods. Returns true if the value is valid."""
spec_validation_methods = {
    Specs.MIN_LENGTH: lambda value, min_length: len(value) >= min_length,
    Specs.MAX_LENGTH: lambda value, max_length: len(value) <= max_length,
    Specs.PATTERN: validate_pattern,
}


class SpecManager:
    """
    Provides utilities for building validation functions
    from specs and exporting specs to JSON.
    """

    @staticmethod
    def get_validation_method[
        FieldType: Any
    ](spec: SpecCollection, field: Field) -> Callable[[FieldType], FieldType]:
        """
        Composes a validation function for a field in a spec

        Raises:
            ValueError: If the field is not found in the spec
                or it lacks descriptions.

        Returns:
            _type_: The validation function.
        """
        # Retrieve specs for field
        try:
            values = spec.values[field]
            descriptions = spec.descriptions[field]
        except KeyError:
            raise ValueError(f"Field '{field}' not found in specs")

        # Validate that all specs have descriptions
        for key in values:
            try:
                descriptions[key]
            except KeyError:
                raise ValueError(
                    f"Description for field '{field}' spec '{key}' not found"
                )

        def validation_method(value: FieldType) -> FieldType:
            for spec in values:
                if spec not in spec_validation_methods:
                    continue

                if not spec_validation_methods[spec](value, values[spec]):
                    raise ValueError(descriptions[spec])
            return value

        return validation_method

    @staticmethod
    def to_typescript(spec_collection: SpecCollection) -> Generator[str, None, None]:
        """
        Yields the spec collection as typescript code.

        Args:
            spec_collection (SpecCollection): the spec
                collection to write

        Raises:
            ValueError: Raised if a field lacks description.

        Yields:
            Generator[str, None, None]: A generator which
                yields the lines to write.
        """
        # Name of the exported typescript object.
        object_name = f"{spec_collection.domain}Fields"

        # Open the spec collection object.
        yield f"export const {object_name} = {{\n"

        # For every field in the spec collection.
        for field in spec_collection.values:
            # Open the field object.
            yield f"    {field}: {{\n"

            # For every spec in the field.
            for spec in spec_collection.values[field]:
                # Get the name of the spec
                spec_name = str(spec.value)

                # Get the value for the spec
                value = spec_collection.values[field][spec]

                # Apply strings to pattern
                if spec.value == Specs.PATTERN.value:
                    value = f"'{value}'"

                # Get the descripton for the spec.
                try:
                    description = spec_collection.descriptions[field][spec]
                except KeyError:
                    raise ValueError(
                        f"Missing description for field {field} and spec {spec}"
                    )

                # Open the spec object
                yield f"        {spec_name}: {{\n"

                # Write value and description
                yield f"            value: {value},\n"
                yield f"            message: '{description}',\n"

                # Close spec object
                yield "        },\n"

            # Add the field description
            try:
                field_description = spec_collection.descriptions[field]["field"]
            except KeyError:
                raise ValueError(f"Missing field description for field {field}")

            yield f"        description: '{field_description}'\n"

            # Close the field object
            yield "    },\n"

        # Close the spec collection object and export default
        yield "}\n"
        yield f"export default {object_name}"


if __name__ == "__main__":
    """
    Exports all specs to typescript files.
    """
    # Make sure to import all files so their specs are registered
    # VerdanTech Source
    from src.garden.domain.specs import specs as garden_specs
    from src.user.domain.specs import specs as user_specs

    os.makedirs("./schema/specs", exist_ok=True)
    output_dir = "./schema/specs/"

    for spec_collection in [user_specs, garden_specs]:
        file_path = os.path.join(output_dir, f"{spec_collection.domain}.ts")

        with open(file_path, "w") as file:
            for output in SpecManager.to_typescript(spec_collection):
                file.write(output)
