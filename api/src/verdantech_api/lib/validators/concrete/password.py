from generic.validators import StringFieldValidator


class PasswordValidator(StringFieldValidator):
    field_name = "Password"
