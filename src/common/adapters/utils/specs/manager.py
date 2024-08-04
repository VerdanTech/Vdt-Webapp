import json
from typing import Dict, Any

class SpecificationManager:
    _instance = None
    specs: Dict[str, Dict[str, Any]]
    
    def __new__(cls) -> 'SpecificationManager':
        if cls._instance is None:
            cls._instance = super(SpecificationManager, cls).__new__(cls)
            cls._instance.specs = {}
        return cls._instance

    def register_spec(self, name: str, spec: Dict[str, Any]) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(spec, dict):
            raise TypeError("Specification must be a dictionary")
        if name in self.specs:
            raise ValueError(f"Specification '{name}' already exists")
        
        self._format_descriptions(spec)
        self.specs[name] = spec

    def _format_descriptions(self, spec: Dict[str, Any]) -> None:
        for field, field_spec in spec.items():
            if isinstance(field_spec, dict):
                for key, value in field_spec.items():
                    if isinstance(value, dict) and "description" in value:
                        value["description"] = self._format_string(value["description"], field_spec)
                if "description" in field_spec:
                    field_spec["description"] = self._format_string(field_spec["description"], field_spec)

    def _format_string(self, string: str, context: Dict[str, Any]) -> str:
        try:
            return string.format(**{k: v["spec"] for k, v in context.items() if isinstance(v, dict) and "spec" in v})
        except KeyError as e:
            raise ValueError(f"Missing key in specification: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid format string: {e}")

    def get_spec(self, name: str) -> Dict[str, Any]:
        if name not in self.specs:
            raise KeyError(f"Specification '{name}' not found")
        return self.specs[name]

    def dump_to_json(self, filename: str) -> None:
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string")
        if not filename.endswith('.json'):
            raise ValueError("Filename must have a .json extension")
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.specs, f, indent=2)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

# Create a global instance
spec_manager = SpecificationManager()