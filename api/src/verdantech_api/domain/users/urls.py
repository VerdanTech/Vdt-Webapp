from verdantech_api.settings import API_URL_BASE

USERS_URL_BASE: str = API_URL_BASE + "users/"

USER_LIST_URL: str = USERS_URL_BASE + ""
USER_DETAIL_URL: str = USERS_URL_BASE + "{username:str}/"
USER_CHECK_USERNAME_AVAILABLE_URL: str = (
    USERS_URL_BASE + "{username:str}/check_available/"
)
USER_CREATE_URL: str = USERS_URL_BASE + ""
USER_CHANGE_USERNAME_URL: str = USERS_URL_BASE + "{username:str}/"
USER_DELETE_URL: str = USERS_URL_BASE + "{username:str}/"

USER_VERIFY_EMAIL_URL: str = USERS_URL_BASE + "verify_email/{key:str}"
USER_RESEND_EMAIL_VERIFICATION_URL: str = USERS_URL_BASE + "verify_email/resend/"
USER_REQUEST_EMAIL_CHANGE_URL: str = USERS_URL_BASE + "request_email_change/"

USER_RESET_PASSWORD_REQUEST_URL: str = USERS_URL_BASE + "request_password_reset/"
USER_RESET_PASSWORD_CONFIRM_URL: str = (
    USERS_URL_BASE + "confirm_password_reset/{key:str}"
)

USER_LOGIN_URL: str = USERS_URL_BASE + "login/"
USER_LOGOUT_URL: str = USERS_URL_BASE + "logout/"
