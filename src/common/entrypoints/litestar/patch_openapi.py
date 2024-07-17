# External Libraries
import yaml


def patch_schema(schema_filename="schema.yaml"):
    with open(schema_filename, "r") as file:
        data = yaml.safe_load(file)

    def define_extra_types(data):
        """
        Fixes the generated Litestar schema's extra section.
        """
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

    def extract_validation_exception(data):
        """
        Fixes the generated Litestar schema's to share all 400 validation 
        exception responses with a single referenced component.
        """
        # Construct the validation exception schema
        validation_exception_schema = {
            "description": "Validation Exception",
            "examples": [
                {
                    "detail": "Bad Request",
                    "extra": {},
                    "status_code": 400
                }
            ],
            "properties": {
                "detail": {
                    "type": "string"
                },
                "extra": {
                    "additionalProperties": {},
                    "type": [
                        "null",
                        "object",
                        "array"
                    ]
                },
                "status_code": {
                    "type": "integer"
                }
            },
            "required": [
                "detail",
                "status_code"
            ],
            "type": "object"
        }
        data["components"]["schemas"]["ValidationException"] = validation_exception_schema

        # Replace all inline validation exception schemas with a reference
        for path, path_item in data["paths"].items():
            for method, operation in path_item.items():
                if "responses" in operation:
                    if '400' in operation["responses"]:
                        operation["responses"]['400']["content"]["application/json"]["schema"] = {
                            "$ref": "#/components/schemas/ValidationException"
                        }
        

    extract_validation_exception(data)
    define_extra_types(data)

    with open(schema_filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False)


if __name__ == "__main__":
    patch_schema()
