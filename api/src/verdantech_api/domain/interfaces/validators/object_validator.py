from typing import Any, Dict, List, Type

from src.verdantech_api.domain.common.entities import EntityT

from .field_validators import FieldValidator, FieldValidatorConfig, NormalizationMixin


class AbstractObjectValidator:
    pass


class ObjectValidator:
    """Generic class for implementing validations on multiple fields"""

    object_name = "generic_object"
    object_type = Type

    def __init__(self, field_validators: List[FieldValidator]) -> None:
        self.field_validators = field_validators

    def validate(self, *fields: List[str]) -> bool:
        """Validates the input_obj against all validators.

        Args:
            input_obj (Dict[str, Any]): The input object to validate

        Returns:
            bool: Whether the validation passed for all fields
        """
        errors = {}

        for field_validator in self.field_validators:
            if field_validator.field_name not in fields:
                raise ValueError

        """
            try:
                field_value = input_obj.get(field_validator.field_name)
                if not field_value:
                    field_validator_list = [field_validator.field_name for field_validator in self.field_validators]
                    raise ValueError("ObjectValidator")
                validator.validate(field_value)
            except ValidationError as error:
                errors[field_name] = error.message

        if errors:
            raise ValidationError(message=errors)
        """

        return True

    @classmethod
    def factory(cls, field_validator_configs: List[FieldValidatorConfig]):
        pass
