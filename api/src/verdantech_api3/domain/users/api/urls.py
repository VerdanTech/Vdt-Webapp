from verdantech_api.settings import API_URL_BASE

USERS_URL_BASE: str = API_URL_BASE + "users/"

USER_LIST_URL: str = USERS_URL_BASE + ""
USER_DETAIL_URL: str = USERS_URL_BASE + "{username:str}/"
USER_CHECK_USERNAME_URL: str = USERS_URL_BASE + "{username:str}/check_username/"

USER_CREATE_URL: str = USERS_URL_BASE + ""
USER_CHANGE_URL: str = USERS_URL_BASE + "{username:str}/"
USER_CHANGE_EMAIL_URL: str = USERS_URL_BASE + "{username:str}/email/"
USER_DELETE_URL: str = USERS_URL_BASE + "{username:str}/"

USER_EMAIL_VERIFICATION_REQUEST_URL: str = USERS_URL_BASE + "verify_email/resend/"
USER_EMAIL_VERIFICATION_CONFIRM_URL: str = USERS_URL_BASE + "verify_email/{key:str}"

USER_PASSWORD_RESET_REQUEST_URL: str = USERS_URL_BASE + "request_password_reset/"
USER_PASSWORD_RESET_CONFIRM_URL: str = (
    USERS_URL_BASE + "confirm_password_reset/{key:str}"
)

USER_LOGIN_URL: str = USERS_URL_BASE + "login/"
USER_LOGOUT_URL: str = USERS_URL_BASE + "logout/"
