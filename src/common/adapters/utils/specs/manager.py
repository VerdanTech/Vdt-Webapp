# Standard Library
import json
from typing import Any, Dict


class SpecManager:
    def __init__(self):
        self.specs: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, spec: Dict[str, Any]):
        self.specs[name] = spec

    def get_spec(self, name: str) -> Dict[str, Any]:
        return self.specs[name]

    def get_description(self, name: str) -> str:
        spec = self.get_spec(name)
        format_dict = {
            rule: rule_spec["spec"]
            for field, rules in spec.items()
            for rule, rule_spec in rules.items()
            if isinstance(rule_spec, dict) and "spec" in rule_spec
        }
        return spec.get("description", "").format(**format_dict)

    def format_specs(self) -> Dict[str, Dict[str, Any]]:
        formatted_specs = {}
        for name, spec in self.specs.items():
            formatted_specs[name] = {}
            for field, rules in spec.items():
                formatted_specs[name][field] = {}
                for rule, rule_spec in rules.items():
                    if isinstance(rule_spec, dict) and "spec" in rule_spec:
                        formatted_specs[name][field][rule] = {
                            "spec": rule_spec["spec"],
                            "description": rule_spec["description"].format(
                                **{rule: rule_spec["spec"]}
                            ),
                        }
                    else:
                        formatted_specs[name][field][rule] = rule_spec
                if "description" in formatted_specs[name][field]:
                    formatted_specs[name][field]["description"] = self.get_description(
                        name
                    )
        return formatted_specs

    def to_json(self) -> str:
        formatted_specs = self.format_specs()
        return json.dumps(formatted_specs, indent=2)


# Create a global instance
spec_manager = SpecManager()
