from src.verdantech_api import settings
from src.verdantech_api.domain.models.common.entities import EntityIDType
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter


async def emit_email_verification_email(
    email_address: str, username: str, key: str, email_emitter: EmailEmitter
) -> None:
    """Emit the email with the email verification parameters

    Args:
        email_address (str): email address to send to
        username (str): username of the user receiving
        key (str): verification key
        email_emitter (EmailEmitter): email emitter callable
    """
    await email_emitter(
        receiver=email_address,
        subject="Email verification - VerdanTech",
        filepath=settings.email_path("email_verification.html"),
        username=username,
        client_base_url=settings.CLIENT_BASE_URL,
        verification_url=settings.CLIENT_EMAIL_VERIFICATION_URL + key,
    )


async def emit_password_reset_email(
    email_address: str,
    username: str,
    user_id: EntityIDType,
    key: str,
    email_emitter: EmailEmitter,
) -> None:
    """Emit the email with the password reset parameters

    Args:
        email_address (str): email address to send to
        username (str): username of the recepient
        user_id (EntityIDType): ID of the recepiend
        key (str): verification key
        email_emitter (EmailEmitter): email emitter callable
    """
    await email_emitter(
        receiver=email_address,
        subject="Password reset - VerdanTech",
        filepath=settings.email_path("password_reset.html"),
        username=username,
        user_id=user_id,
        client_base_url=settings.CLIENT_BASE_URL,
        reset_url=settings.CLIENT_PASSWORD_RESET_URL + key,
    )
