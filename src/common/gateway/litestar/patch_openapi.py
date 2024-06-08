# External Libraries
import yaml


def patch_schema(schema_filename="schema.yaml"):
    with open(schema_filename, "r") as file:
        data = yaml.safe_load(file)

    def define_extra_types(data):
        if "extra" in data:
            extra_section = data["extra"]

            if (
                isinstance(extra_section, dict)
                and extra_section.get("additionalProperties") == {}
                and extra_section.get("type") == ["null", "object", "array"]
            ):
                new_extra_section = {
                    "anyOf": [
                        {"type": "object", "additionalProperties": {}},
                        {"type": "array", "items": {}},
                        {"type": "null"},
                    ]
                }
                data["extra"] = new_extra_section

        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    define_extra_types(value)

    define_extra_types(data)

    with open(schema_filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False)


if __name__ == "__main__":
    patch_schema()
