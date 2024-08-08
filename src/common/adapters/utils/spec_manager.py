# Standard Library
import json
import os
import re
from collections import namedtuple
from enum import Enum, auto
from typing import Any, Callable, Generator, Literal


class Specs(Enum):
    TYPE = "type"
    MIN_LENGTH = "min_length"
    MAX_LENGTH = "max_length"
    PATTERN = "pattern"


type Field = str
type SpecValues = dict[Field, dict[Specs, Any]]
type SpecDescriptions = dict[Field, dict[Specs | Literal["field"], str]]

SpecCollection = namedtuple("SpecCollection", ["domain", "values", "descriptions"])

# returns true if valid
spec_validation_methods = {
    Specs.MIN_LENGTH: lambda value, min_length: len(value) >= min_length,
    Specs.MAX_LENGTH: lambda value, max_length: len(value) <= max_length,
    Specs.PATTERN: lambda value, pattern: re.match(pattern, value),
}


class SpecManager:
    @staticmethod
    def get_validation_method(
        spec: SpecCollection, field: Field
    ) -> Callable[[Any], Any]:
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

        def validation_method(value: Any) -> Any:
            for spec in values:
                if spec not in spec_validation_methods:
                    continue

                if not spec_validation_methods[spec](value, values[spec]):
                    raise ValueError(descriptions[spec])

        return validation_method

    @staticmethod
    def to_json(spec_collection: SpecCollection) -> Generator[str, None, None]:
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
                    raise ValueError(f"Missing description for field {field} and spec {spec}")
                
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
    # Make sure to import all files so their specs are registered
    # VerdanTech Source
    from src.user.domain.specs import specs as user_specs

    os.makedirs("./schema/specs", exist_ok=True)
    output_dir = "./schema/specs/"

    for spec_collection in [user_specs]:
        file_path = os.path.join(output_dir, f"{spec_collection.domain}.ts")

        with open(file_path, "w") as file:
            for output in SpecManager.to_json(spec_collection):
                file.write(output)
