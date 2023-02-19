from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class AccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation) -> str:
        """Override for Allauth's email confirmation link,
        to point to the client instead of the API
        """
        return settings.CLIENT_EMAIL_VERIFY_URL + emailconfirmation.key

    def respond_email_verification_sent(self, request, user):
        """Override for Allauth's post-registration redirect,
        as this will be handled in the client
        """
        return None
