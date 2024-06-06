# VerdanTech Source
from src.domain.user import UserSanitizer
from src.ops.common import schema
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum as specs


@schema
class UserLoginInput:
    """
    Input for logging a user in.
    """

    email_address: str
    password: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "email_address": self.email_address,
            },
            spec_select={
                "email_address": [
                    specs.LENGTH,
                    specs.EMAIL,
                ],
            },
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.email_address = sanitized_data["email_address"]
