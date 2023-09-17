from src.verdantech_api import settings
from src.verdantech_api.infrastructure.email.emitter import EmailEmitter


class EmailVerificationService:
    @staticmethod
    async def emit_email_verification_email(
        email_address: str, username: str, key: str, email_emitter: EmailEmitter
    ):
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
            verification_url=settings.EMAIL_VERIFICATION_CLIENT_URL + key,
        )
