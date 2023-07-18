from ..interfaces.field_validators import FieldValidator, NormalizationMixin


class UsernameValidator(FieldValidator, NormalizationMixin):
    field_name = "Username"
