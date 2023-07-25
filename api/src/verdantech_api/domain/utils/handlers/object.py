from typing import Any, Dict

from .field import FieldSanitizer
from .sanitization.generic import SanitizationError


class ObjectSanitizer:
    def __init__(self, **field_sanitizers: Dict[str, FieldSanitizer]):
        self.field_sanitizers = field_sanitizers

    def sanitize(self, **input_data: Dict[str, Any]) -> Dict[str, Any]:
        output_data = {}
        error = {}

        for field_name, input in input_data.items():
            field_sanitizer = self.field_sanitizers.get(field_name)

            if not field_sanitizer:
                raise ValueError(f"No field handler found for field: {field_name}")

            try:
                field_sanitizer.sanitize(input=input)
                output_data[field_name] = field_sanitizer.normalized()
            except SanitizationError as error_raised:
                error[field_name] = str(error_raised)

        # Raise errors
        if error:
            raise SanitizationError(message=error)

        return output_data
