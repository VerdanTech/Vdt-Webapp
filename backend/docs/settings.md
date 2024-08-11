# Settings

Application configuration which isn't specifically pinned down by the domain requirements is contained within the centralized settings package, `src/settings`. This package contains three files: `base.py`, `dev.py`, and `prod.py`. All settings and their defaults are defined in `base.py` and any over-rides relevant to these environments are imported depending on the value of the environment variable `ENVIRONMENT`.

## API

This section contains settings relevant to the Litestar application and other API-related concerns.

### URLs

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| USING_HTTPS | bool | Identical to the environment variable. |False |
| API_URL_BASE | str | Base of the API URL. | "" |

### Client

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| CLIENT_DOMAIN | str | Identical to the environment variable. |`/verdantech.io` |
| CLIENT_BASE_URL | str | Base of the URL to the frontend. | `http://verdantech.io/` |
| CLIENT_EMAIL_VERIFICATION_URL | str | Frontend URL for email verification. Required to send email verification emails. | `http://verdantech.io/register/verify/` |
| CLIENT_PASSWORD_RESET_URL | str | Frontend URL for password resets. | `http://verdantech.io/password_reset/` |
| CLIENT_GARDENS_URL | str | Frontend URL to the client's list of gardens. | `http://verdantech.io/app/gardens/` |

### Allowed Hosts

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| ALLOWED_HOSTS | str or list[str] | Identical to environment the variable.  | `.localhost` |

### Cross-Origin Resource Sharing (CORS)

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| ALLOW_ORIGINS | str or list[str] | Identical to environment the variable. | `"` |

### Cross-Site Request Forgery (CSRF)

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |

### Authentication

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| JWT_SECRET | str | Identical to environment the variable. | `developmentsecret123` |

## Application

This section contains settings relevant to general application and adapter operation.

### Task Backend

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| NUM_TASK_WORKERS | int | Number of worker task threads to spawn for the task backend. | `1` |

### Database

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| POSTGRES_URI | str | Identical to the environment variable. | `postgresql+asyncpg://verdantech_db:xkrytusefhrerifuthrh@postgres:5432/dev_db` |
| ALCHEMY_CLIENT_NAME | str | The attribute name to use for the Sqlalchemy client stored in Litestar's global state. | `sqlalchemy_client` |
| ALCHEMY_TRANSACTION_COMMIT | bool | If False, no Sqlalchemytransasctions will be committed. | `True` |

### Files

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| STATIC_BASE_DIR | str | Filepath of the static files directory relative to the source directory. | `static/` |
| EMAIL_BASE_DIR | str | Filepath of the email files directory relative to the source directory. | `static/emails/` |

### Email

### Client
| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| EMAIL_CLIENT_HOSTNAME | str | Hostname of the SMTP server in use. | TODO |
| EMAIL_CLIENT_PORT | str | Port of the SMTP server in use. | TODO |
| EMAIL_CLIENT_USERNAME | str | Username of the application's account on the SMTP server. | TODO |
| EMAIL_CLIENT_PASSWORD | str | Password of the  application's account on the SMTP server. | TODO |
| EMAIL_CLIENT_SENDER | str | Email address of the application's account on the SMTP server. | TODO |

### Application
| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| EMAIL_CONFIRMATION | str (enum) | Whether email confirmation is required. | `required` |
| EMAIL_VERIFICATON_EXPIRY_TIME_HOURS | int | The number of hours after an email confirmation is created before it is expired/invalid. | `72` |

### Files
| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| EMAIL_FILEPATH_EMAIL_CONFIRMATION | str | Name of the email verification email file within the emails directory. | `email_verification.html` |
| EMAIL_SUBJECT_EMAIL_CONFIRMATION | str | Subject line of the email confirmation email. | `Email verification - VerdanTech` |
| EMAIL_FILEPATH_PASSWORD_RESET | str | Name of the password reset email file within the emails directory. | `password_reset.html` |
| EMAIL_SUBJECT_PASSWORD_RESET | str | Subject line of the password reset email. | `Password reset - VerdanTech` |
| EMAIL_FILEPATH_GARDEN_INVITE | str | Name of the garden invite email file within the emails directory. | `garden_invite.html` |
| EMAIL_SUBJECT_GARDEN_INVITE | str | Subject line of the garden invite email | `You've been invited to a Garden - VerdanTech` |

## Domain Models

This section contains settings relevant to domain models.

### User

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| USER_MAX_EMAILS | int | The maximum number of emails a user can have. While only the primary email is relevant to the user, old emails are stored up to a maximum of this number. | `3` |

### Garden

| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| GARDEN_NAME_MIN_LENGTH | int | Minimum length of a garden name | `2` |
| GARDEN_NAME_MAX_LENGTH | int | Maximum length of a garden name. | `50` |
| GARDEN_NAME_PATTERN | str (pattern) | Regex pattern used to validate garden names. | `[0-9A-Za-z ]+` |
| GARDEN_NAME_PATTERN_DESCRIPTION | str | Description of the garden name regex pattern. Returned by the API on error. | `only alphanumeric characters and spaces.` |
| GARDEN_NAME_FIELD_DESCRIPTION | str | Description of the garden name field on the OpenAPI schema. | Derived from previous 3 fields. |
| GARDEN_KEY_MIN_LENGTH | int | Minimum length of a garden key | `4` |
| GARDEN_KEY_MAX_LENGTH | int | Maximum length of a garden key. | `16` |
| GARDEN_KEY_PATTERN | str (pattern) | Regex pattern used to validate garden keys. | `[0-9A-Za-z-]+` |
| GARDEN_KEY_PATTERN_DESCRIPTION | str | Description of the garden key regex pattern. Returned by the API on error. | `only alphanumeric characters and hyphens.` |
| GARDEN_KEY_FIELD_DESCRIPTION | str | Description of the garden key field on the OpenAPI schema. | Derived from previous 3 fields. |
| GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_NO_PLANT_NAME | int | Default length of the generated portion of the garden key when generated without a plant name. | `6` |
| GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_PLANT_NAME | int | Default length of the generated portion of the garden key when generated with a plant name. | `3` |
| MAX_GARDEN_RANDOM_PLANT_KEY_GENERATION_ATTEMPTS | int | The maximum amount of times the key generator will generate an id with a random plant name before reverting to only random characters. | `4` |